from file_monitor import start_monitoring
from utils import remove_pycache
import os

if __name__ == "__main__":
    remove_pycache(os.getcwd())
    print('iniciando o monitoramento - arquivo atual: main.py')
    start_monitoring()

print('arquivo main.py foi chamado...')