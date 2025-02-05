from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

aes_key = get_random_bytes(32)

def generate_user_token(user_json):
    data = json.dumps(user_json)
    cipher = AES.new(aes_key, AES.MODE_CTR)
    encrypted_token = cipher.encrypt(data.encode())
    return (base64.b64encode(encrypted_token).decode(), # convert token to Base64 to transmit as JSON
            base64.b64encode(cipher.nonce).decode()) # convert nonce to Base64 to transmit as JSON

def validate_user_token(token, nonce):
    if nonce is not None:
        cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
        message = cipher.decrypt(token).decode() # Decrypt data
        return message