import requests
from flask import jsonify
from netlify_lambda import lambda_handler

# Base URL of the Flask app hosted on Netlify
FLASK_APP_URL = "https://your-flask-app.netlify.app"

def fetch_data(endpoint):
    try:
        response = requests.get(f"{FLASK_APP_URL}/{endpoint}")
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error: {http_err}'}), 400
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Request error: {req_err}'}), 500
    except Exception as err:
        return jsonify({'error': f'Unexpected error: {err}'}), 500

def handler(event, context):
    endpoint = event['path'].strip('/')
    return fetch_data(endpoint)
