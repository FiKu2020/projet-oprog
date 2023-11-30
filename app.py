from flask import Flask
from flask import Response
from flask import jsonify
from flask import request



app = Flask(__name__)
users = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}
    ]