from flask import Flask, request
from utils import remove_pycache
from etl.etl_processor import run_etl
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def remove_pycache_from_current_directory():
    remove_pycache(os.getcwd())

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file and file.filename.endswith('.xlsx'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        run_etl(file_path)  # Executa o ETL no arquivo recebido
        return {"message": "Arquivo recebido e processamento iniciado."}, 200
    else:
        return {"error": "Por favor, envie um arquivo .xlsx válido."}, 400

if __name__ == "__main__":
    remove_pycache_from_current_directory()
    app.run(host='0.0.0.0', port=5000)
