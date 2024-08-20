from flask import Flask, jsonify, send_from_directory
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# External API details
KARBON_API_URL_CONTACTS = "https://api.karbonhq.com/v3/Contacts"
KARBON_API_URL_USERS = "https://api.karbonhq.com/v3/Users"
KARBON_API_HEADERS = {
    'Accept': 'application/json',
    'AccessKey': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJLYXJib25IUSIsInJlZyI6InVzMiIsInRhayI6IjgxOUZEMUU4LTcxMTAtNDEyNC1BRTA3LUNEQzVDNzVGQkJFMiIsImlhdCI6MTcxODI5MTk2Ni4wfQ.bWrn6D02shKYPYMy9YLXXRcfhvropcRHlPbZsEPEfLQ',
    'Authorization': 'Bearer b81694a5-dae9-4593-8c06-a672d5ecd640'
}

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    try:
        response = requests.get(KARBON_API_URL_CONTACTS, headers=KARBON_API_HEADERS)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error: {http_err}'}), 400
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Request error: {req_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'Unexpected error: {err}'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        response = requests.get(KARBON_API_URL_USERS, headers=KARBON_API_HEADERS)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error: {http_err}'}), 400
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Request error: {req_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'Unexpected error: {err}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
