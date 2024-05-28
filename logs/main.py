from flask import Flask, jsonify, request, send_file
import os

LOG_FILE_PATH = '/app/logs.txt'
LOG_AUTH_TOKEN = os.environ.get('LOG_TOKEN')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def download_logs():
    return send_file(LOG_FILE_PATH, as_attachment=True)

@app.route('/', methods=['POST'])
def log_message():
    try:
        auth_token = request.headers.get('Authorization')
        if auth_token != LOG_AUTH_TOKEN:
            return jsonify({'error': 'Unauthorized'}), 403

        log_data = request.json
        write_log(log_data)
        return jsonify({'status': 'logged'}), 200
    except Exception as e:
        return jsonify({'error': 'Unexpected error', 'message': str(e)}), 500

def write_log(entry):
    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(f"{entry}\n")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
