from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import base64
import json
import time

aes_key = get_random_bytes(32)

class CryptoService:

    @staticmethod
    def generate_session_token(username):
        timestamp = str(int(time.time()))
        message = json.dumps({"timestamp": timestamp, "username": username})
        cipher = AES.new(aes_key, AES.MODE_CTR)
        encrypted_token = cipher.encrypt(message.encode())
        return (base64.b64encode(encrypted_token).decode(), # convert token to Base64 to transmit as JSON
                base64.b64encode(cipher.nonce).decode()) # convert nonce to Base64 to transmit as JSON

    @staticmethod
    def validate_session_token(token, nonce):
        token_time_limit = 60 * 15 # Calculate 15 minutes in seconds
        new_token = base64.b64decode(token)
        new_nonce = base64.b64decode(nonce)
        cipher = AES.new(aes_key, AES.MODE_CTR, nonce=new_nonce)
        decrypted_json = json.loads(cipher.decrypt(new_token).decode()) # Decrypt data
        timestamp = int(decrypted_json["timestamp"])
        if (int(time.time()) - timestamp) > token_time_limit:
            return False
        else:
            return True