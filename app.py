from flask import Flask

from models.db_models import db

app = Flask(__name__)
from views import *

if __name__ == "__main__":
    app.run()