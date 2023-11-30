from flask import Flask
from flask import Response
from flask import jsonify
from flask import request

app = Flask(__name__)
users = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}
]


@app.get('/users')
def get_users():
    return jsonify(users), 200

@app.
def get_users_by_id():
    if users.id in users:
        return jsonify(users), 200

print(users)
