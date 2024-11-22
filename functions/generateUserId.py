import uuid
from flask import Flask, request, jsonify
from google.cloud import sqlcommenter

app = Flask(__name__)

@app.route('/generate_user_id', methods=['GET'])  # GET method endpoint
def generate_user_id():
    ip_address = request.remote_addr
    user_id = str(uuid.uuid4())

    # Store in Cloud SQL (example)
    with db.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_data (ip_address, user_id) VALUES (%s, %s)",
                (ip_address, user_id),
            )
        conn.commit()

    # Return the generated user ID in the response
    return jsonify({'userId': user_id}), 200  

# ... (rest of your server-side code) ...
