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

@app.get('/users/<id>')
def get_users_by_id():
    if users.id in users:
        return jsonify(users), 200

@app.post('/users')
def create_temp_users():
    placeholder = []
    currUserData = request.json
    if 'name' and 'lastname' in users:
        newUser = {
            'id' : len(users) + 1,
            "name": currUserData['name'],
            "lastname": currUserData['lastname']
        }

@app.delete
def delete_user(user_id):
    
print(users)

if __name__ == '__main__':
    app.run()