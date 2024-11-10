import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

DATABASE_URI = os.getenv('DATABASE_URI')
DIRECTORY_PATH = os.getenv('DIRECTORY_PATH')
LOG_DIRECTORY_PATH = os.getenv('LOG_DIRECTORY_PATH')
COMPLETED_DIRECTORY_PATH = os.getenv('COMPLETED_DIRECTORY_PATH')
ERROR_DIRECTORY_PATH = os.getenv('ERROR_DIRECTORY_PATH')

print('\n\n teste teste \n\n deu certo:\n ')
print(DATABASE_URI + ' \n ' + DIRECTORY_PATH + ' \n ' + LOG_DIRECTORY_PATH + ' \n ' + COMPLETED_DIRECTORY_PATH + ' \n ' + ERROR_DIRECTORY_PATH)

os.makedirs(COMPLETED_DIRECTORY_PATH, exist_ok=True)
os.makedirs(ERROR_DIRECTORY_PATH, exist_ok=True)
os.makedirs(LOG_DIRECTORY_PATH, exist_ok=True)
