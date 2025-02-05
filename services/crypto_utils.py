from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json
import time

from flask import jsonify

aes_key = get_random_bytes(32)

token_time_limit = 60 * 15 # Calculate 15min in seconds

def generate_user_token(user_json):
    data = json.dumps(user_json)
    cipher = AES.new(aes_key, AES.MODE_CTR)
    encrypted_token = cipher.encrypt(data.encode())
    return (base64.b64encode(encrypted_token).decode(), # convert token to Base64 to transmit as JSON
            base64.b64encode(cipher.nonce).decode()) # convert nonce to Base64 to transmit as JSON

def validate_user_token(token, nonce):
        new_token = base64.b64decode(token)
        new_nonce = base64.b64decode(nonce)

        cipher = AES.new(aes_key, AES.MODE_CTR, nonce=new_nonce)
        decrypted_json = json.loads(cipher.decrypt(new_token).decode()) # Decrypt data

        timestamp = int(decrypted_json["timestamp"])

        if (int(time.time()) - timestamp) > token_time_limit:
            return jsonify({
                "error": "Token expired",
                "message": "Log in again for a new token"
            }), 401
        else:
            return jsonify({"status": "OK"}), 200