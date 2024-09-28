import re
import pandas as pd

def clean_phone(phone):
    if pd.isna(phone):
        return phone
    return re.sub(r'\D', '', str(phone))

def convert_timestamps(row):
    for key, value in row.items():
        if isinstance(value, pd.Timestamp):
            row[key] = value.strftime('%Y-%m-%d %H:%M:%S')
    return row

def capitalize_columns(df):
    lowercase_columns = ['email', 'process_status', 'job_status', 'role']
    for column in df.columns:
        if column in lowercase_columns:
            df[column] = df[column].astype(str).str.lower()
        else:
            df[column] = df[column].astype(str).str.capitalize()
    return df
