from flask import jsonify

def get_registration_status(request):
    match request:
        case 200:
            return jsonify({"message": "success"}), 200
        case 520:
            return jsonify({"message": "username wrong pattern"}), 520
        case 521:
            return jsonify({"message": "username in use"}), 521
        case 522:
            return jsonify({"message": "email wrong pattern"}), 522
        case 523:
            return jsonify({"message": "email in use"}), 523
        case 524:
            return jsonify({"message": "password wrong pattern"}), 524
        case 525:
            return jsonify({"message": "passwords must match"}), 525
        case _:
            return jsonify({"message": "Invalid"}), 400
