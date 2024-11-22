import uuid
import hashlib
from flask import Flask, request, jsonify
from google.cloud import sqlcommenter

app = Flask(__name__)

@app.route('/generate_user_id', methods=['GET'])  # GET method endpoint
def generate_user_id():
    ip_address = request.remote_addr
    user_id = str(uuid.uuid4())

    #hash ip for security
    hashed_ip = hashlib.sha256(ip_address.encode()).hexdigest()

    # Store in Cloud SQL (example)
    with db.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_data (hashed_ip, user_id) VALUES (%s, %s)",
                (hashed_ip, user_id),
            )
        conn.commit()

    # Return the generated user ID in the response
    return jsonify({'user_id': user_id}), 200  

# ... (rest of your server-side code) ...
