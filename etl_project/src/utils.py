import os
import shutil

def remove_pycache(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        if '__pycache__' in dirnames:
            shutil.rmtree(os.path.join(dirpath, '__pycache__'))

