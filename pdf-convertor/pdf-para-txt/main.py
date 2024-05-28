import os
import requests
from flask import Flask, flash, redirect, render_template, request, send_file
from pypdf import PdfReader

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

        if not uploaded_file.filename.endswith('.pdf'):
            raise ValueError('Arquivo deve ser .pdf.')

        output_path = os.path.join('/tmp', f"{os.path.splitext(uploaded_file.filename)[0]}.txt")
        text_content = extract_text_from_pdf(uploaded_file)
        save_text_to_file(output_path, text_content)

        log_action('pdf-to-text', uploaded_file.filename, 200)
        return send_file(output_path, as_attachment=True)
    
    except Exception as e:
        error_message = str(e)
        print(error_message, flush=True)
        log_action('pdf-to-text', error=error_message, status=500)
        return redirect('/')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ''.join(page.extract_text() for page in pdf_reader.pages)
    return extracted_text

def save_text_to_file(file_path, content):
    with open(file_path, 'w') as text_file:
        text_file.write(content)

def log_action(service, filename=None, status=None, error=None):
    log_entry = {
        'service': service,
        'filename': filename,
        'status': status,
        'error': error
    }
    headers = {'Authorization': LOG_TOKEN}
    requests.post(LOG_SERVICE_URL, json=log_entry, headers=headers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
