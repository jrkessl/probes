import os
import sys
import json
from flask import Flask
import time
from threading import Lock

app = Flask(__name__)
lock = Lock()

if __name__ == "__main__":
    print(f'Hello world')
    app.run(debug=True, host="0.0.0.0")

@app.route('/business', methods=['GET'])
def business():
    return "business request completed", 200

@app.route('/crash', methods=['GET'])
def crash():
    os._exit(1)
    return "lala", 501


