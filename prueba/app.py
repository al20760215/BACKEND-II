import os
from flask import Flask, request, render_template, jsonify, send_from_directory
import psycopg2
from werkzeug.utils import secure_filename
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

#Configuracion para manejo de archivos
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Limitador de consultas
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"]
)

#Coneccion a bd
conn = psycopg2.connect(
    host="bd",  
    database="bd",
    user="postgres",
    password="admin"
)

#Funcion para verificar la extension del archivo:
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Rutas
@app.route('/usuarios', methods=['GET'])
@limiter.limit("5 per minute")
def mostrar_usuarios():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios;")
    usuarios = cursor.fetchall()
    cursor.close()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/edificios', methods=['GET'])
@limiter.limit("5 per minute")
def mostrar_edificios():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM edificios;")
    edificios = cursor.fetchall()
    cursor.close()
    return render_template('edificios.html', edificios=edificios)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/uploads', methods=['POST'])
def upload_file():
    if 'file' not in request.files: #Checamos si hay una archivo en la solicitud
        return jsonify({'error': 'No se selecciono archivo'}), 400
    file = request.files['file']
    
    if file.filename == '': #Checamos si tiene nombre el archivo
        return jsonify({'error': 'No se selecciono archivo'}), 400

    # Validamos la extension
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # Guardamos el archivo en el directorio
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        return jsonify({'message': 'Archivo subido correctamente', 'file_path': file_path}), 200
    else:
        return jsonify({'error': 'Error, archivo no permitido'}), 400

@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        return jsonify({'error': 'Archivo no encontrado'}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
