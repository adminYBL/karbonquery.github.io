from flask import Flask, jsonify, send_from_directory
import requests
from flask_cors import CORS
from netlify_lambda import lambda_handler

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# External API details
KARBON_API_URL_CONTACTS = "https://api.karbonhq.com/v3/Contacts"
KARBON_API_URL_USERS = "https://api.karbonhq.com/v3/Users"
KARBON_API_HEADERS = {
    'Accept': 'application/json',
    'AccessKey': 'your-access-key-here',
    'Authorization': 'Bearer your-bearer-token-here'
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

def handler(event, context):
    with app.app_context():
        return lambda_handler(event, context, app)
