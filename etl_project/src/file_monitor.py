import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from etl.etl_processor import run_etl
from config import DIRECTORY_PATH
import time


class ExcelFileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith('.xlsx'):
            return
        run_etl(event.src_path)

def start_monitoring():
    print('arquivo atual: file_monitor.py')
    event_handler = ExcelFileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DIRECTORY_PATH, recursive=False)
    observer.start()
    print(f"Monitorando a pasta: {DIRECTORY_PATH}")

    for filename in os.listdir(DIRECTORY_PATH):
        if filename.endswith(".xlsx"):
            run_etl(os.path.join(DIRECTORY_PATH, filename))

    try:
        print("Entrando no loop de monitoramento...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoramento encerrado.")
        observer.stop()
    observer.join()