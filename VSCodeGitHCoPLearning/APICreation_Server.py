from flask import Flask, Flask, app
import requests
import flask
from flask import request, jsonify  

app = flask.Flask(__name__)

@app.route('/api/v1/create', methods=['POST'])
def create():
    # Get the data from the POST request

    try: 
        data = request.get_json()
        # Retrieve the parameters from the data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
    except ValueError as e:
        print(f"Error: {e}")


    # Check if the parameters are missing
    if not first_name or not last_name or not email:
        return jsonify({'message': 'Missing parameters'}), 400

    # Process the data and return a response
    # For example, you can store the data in a database
    # and return a success message
    return jsonify({'message': 'Data processed successfully'}), 200
