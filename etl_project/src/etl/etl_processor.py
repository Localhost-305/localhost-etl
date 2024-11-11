import pandas as pd
import json
import os
from sqlalchemy import exc
from database import engine
from config import DIRECTORY_PATH, ERROR_DIRECTORY_PATH, LOG_DIRECTORY_PATH #, COMPLETED_DIRECTORY_PATH
from .data_cleaning import clean_phone, convert_timestamps, capitalize_columns
from .error_handling import map_error_message
from tqdm import tqdm
from watchdog.events import FileSystemEventHandler
from datetime import datetime


def load_sheet_mappings(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def process_etl(file_path, sheet_name, mapping, error_logs):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df = df.rename(columns=mapping["columns"])
        df = capitalize_columns(df)

        if sheet_name == "dim_candidates":
            df['phone'] = df['phone'].apply(clean_phone)
        
        if 'qty_hirings' in df.columns:
            df['qty_hirings'] = df['qty_hirings'].fillna(0.0)


        with tqdm(total=len(df), desc=f"Processando {sheet_name}", unit="linha") as pbar:
            for idx, row in df.iterrows():
                try:
                    if 'start_date' in row and 'end_date' in row:
                        start_date = row['start_date']
                        end_date = row['end_date']
                        if pd.to_datetime(start_date) > pd.to_datetime(end_date):
                            reason = "Data inicial maior que a data final"
                            data = row.to_dict()
                            data = convert_timestamps(data)
                            error_entry = {
                                "data": data,
                                "reason": reason
                            }
                            error_logs[mapping["table"]].append(error_entry)
                            continue

                    row_df = pd.DataFrame([row])
                    row_df.to_sql(mapping["table"], con=engine, if_exists='append', index=False)

                    pbar.update(1)

                except exc.IntegrityError as e:
                    reason = map_error_message(str(e.orig))
                    data = row.to_dict()
                    data = convert_timestamps(data)
                    error_entry = {
                        "data": data,
                        "reason": reason
                    }
                    error_logs[mapping["table"]].append(error_entry)

                except Exception as e:
                    reason = map_error_message(str(e))
                    data = row.to_dict()
                    data = convert_timestamps(data)
                    error_entry = {
                        "data": data,
                        "reason": reason
                    }
                    error_logs[mapping["table"]].append(error_entry)

        success_message = f"Dados da aba '{sheet_name}' inseridos na tabela '{mapping['table']}'."
        error_logs.setdefault("logs_genericos", []).append({
            "message": success_message,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    except Exception as e:
        reason = map_error_message(str(e))
        error_logs.setdefault("logs_genericos", []).append({
            "message": f"Erro ao processar a aba '{sheet_name}'.",
            "reason": reason,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        error_file_path = os.path.join(ERROR_DIRECTORY_PATH, os.path.basename(file_path))
        os.rename(file_path, error_file_path)
        print(f"Arquivo movido para a pasta de erros: {error_file_path}")



def handle_error(e, row, table, error_logs):
    reason = map_error_message(str(e))
    data = row.to_dict() if row else {}
    error_entry = {"data": convert_timestamps(data), "reason": reason}
    error_logs.setdefault(table, []).append(error_entry)


def run_etl(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    json_file_path = os.path.join(current_dir, '..', '..', 'config', 'sheet_mappings.json')
    
    sheet_mappings = load_sheet_mappings(json_file_path)
    
    error_logs = {mapping["table"]: [] for mapping in sheet_mappings.values()}
    success_count = 0

    for sheet, mapping in sheet_mappings.items():
        process_etl(file_path, sheet, mapping, error_logs)
        success_count += 1  

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    log_file = os.path.join(LOG_DIRECTORY_PATH, f'{base_name}.json')

    with open(log_file, 'w') as f:
        json.dump(error_logs, f, ensure_ascii=False, indent=4)

    print(f"ETL finalizado. Log de erros salvo em: {log_file}")

    try:
        os.remove(file_path)
        print(f"Arquivo {file_path} removido com sucesso após o processamento.")
    except Exception as e:
        print(f"Erro ao remover o arquivo {file_path}: {e}")

    # if success_count == len(sheet_mappings):
    #     completed_path = os.path.join(COMPLETED_DIRECTORY_PATH, os.path.basename(file_path))

    #     counter = 1
    #     while os.path.exists(completed_path):
    #         completed_path = os.path.join(COMPLETED_DIRECTORY_PATH, f"{base_name}_{counter}.xlsx")
    #         counter += 1

    #     os.rename(file_path, completed_path)
    #     print(f"Arquivo {file_path} movido para a pasta de concluídos: {completed_path}")

class ExcelFileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".xlsx"):
            run_etl(event.src_path)
