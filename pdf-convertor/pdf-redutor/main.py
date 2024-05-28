import os
import subprocess
import requests
from flask import Flask, redirect, render_template, request, send_file

LOG_SERVICE_URL = os.getenv('LOG_SERVICE_URL')
LOG_TOKEN = os.getenv('LOG_TOKEN')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    try:
        if 'file' not in request.files or request.files['file'].filename == '':
            raise ValueError('Nenhum arquivo informado.')

        uploaded_file = request.files['file']
        resolution = request.form.get('resolution')

        if not uploaded_file.filename.endswith('.pdf'):
            raise ValueError('Arquivo deve ser .pdf.')

        if not resolution:
            raise ValueError('Nenhuma resolução informada.')

        resolution_key = get_resolution_setting(resolution)
        input_path = os.path.join('/tmp', uploaded_file.filename)
        output_filename = f"{resolution}_{uploaded_file.filename}"
        output_path = os.path.join('/tmp', output_filename)
        
        uploaded_file.save(input_path)

        gs_command = [
            'gs',
            '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.4',
            f'-dPDFSETTINGS={resolution_key}',
            '-dNOPAUSE',
            '-dBATCH',
            f'-sOutputFile={output_path}',
            input_path
        ]

        subprocess.run(gs_command, check=True)

        log_action('pdf-reducer', uploaded_file.filename, resolution, 200)
        return send_file(output_path, as_attachment=True)
    
    except Exception as e:
        error_message = str(e)
        print(error_message, flush=True)
        log_action('pdf-to-text', error=error_message, status=500)
        return redirect('/')

def get_resolution_setting(resolution):
    resolution_mappings = {
        'screen': '/screen',
        'ebook': '/ebook',
        'printer': '/printer',
        'prepress': '/prepress',
        'default': '/default'
    }
    if resolution not in resolution_mappings:
        raise ValueError('Resolução informada inválida.')
    return resolution_mappings[resolution]

def log_action(service, filename=None, resolution=None, status=None, error=None):
    log_entry = {
        'service': service,
        'filename': filename,
        'resolution': resolution,
        'status': status,
        'error': error
    }
    headers = {'Authorization': LOG_TOKEN}
    requests.post(LOG_SERVICE_URL, json=log_entry, headers=headers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
