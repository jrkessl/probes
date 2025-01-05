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


def initialize_db():
    # Ver se a flag que indica que o banco já foi inicializado já foi setada
    initialized = app.config.get('initialized')
    
    if not initialized:
        # Initialize the database ... 
        
        # Then mark it as initialized.
        app.config.update(
            initialized=True
        )

# request in the root path 
@app.route("/")
def home():
    initialize_db()

    return f'olá mundo'

@app.route('/business', methods=['GET'])
def business():
    with lock:
        initialize_db()

    return "yesss", 200

@app.route('/sleep', methods=['GET'])
def sleep():
    with lock:
        time.sleep(5)
    return "done sleeping", 200

