import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

DATABASE_URI = os.getenv('DATABASE_URI')
DIRECTORY_PATH = os.getenv('DIRECTORY_PATH')
LOG_DIRECTORY_PATH = os.getenv('LOG_DIRECTORY_PATH')
COMPLETED_DIRECTORY_PATH = os.getenv('COMPLETED_DIRECTORY_PATH')
ERROR_DIRECTORY_PATH = os.getenv('ERROR_DIRECTORY_PATH')

os.makedirs(COMPLETED_DIRECTORY_PATH, exist_ok=True)
os.makedirs(ERROR_DIRECTORY_PATH, exist_ok=True)
os.makedirs(LOG_DIRECTORY_PATH, exist_ok=True)





def check_directory_creation(directory_path):
    if os.path.isdir(directory_path):
        print(f"\nDiretório '{directory_path}' já existe ou foi criado com sucesso.")
    else:
        print(f"\nFalha ao criar ou acessar o diretório '{directory_path}'.")

check_directory_creation(COMPLETED_DIRECTORY_PATH)
check_directory_creation(ERROR_DIRECTORY_PATH)
check_directory_creation(LOG_DIRECTORY_PATH)
print()
