from flask import Flask
from flask import Response
from flask import jsonify
from flask import request
import json

app = Flask(__name__)
users = 'users.json'