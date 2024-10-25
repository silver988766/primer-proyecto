import os
import subprocess  # Asegúrate de importar subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Carpeta para guardar los archivos subidos

# Asegúrate de que la carpeta existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return redirect(url_for('home'))

@app.route('/logs')
def show_logs():
    log_files = os.listdir('logs')  
    return render_template('logs.html', log_files=log_files)

@app.route('/restart-service')
def restart_service():
    # Reemplaza 'nombre_del_servicio' con el nombre real del servicio que deseas reiniciar.
    subprocess.run(['sudo', 'systemctl', 'restart', 'nombre_del_servicio'])
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)




