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
    with lock:
        initialized = app.config.get('initialized')
        if not initialized:
            time.sleep(60) # Some long initialize setting...
            app.config.update(initialized=True) # Then mark it as initialized. Because it only happens the first time.
    return "business request completed", 200

@app.route('/crash', methods=['GET'])
def crash():
    with lock:
        os._exit(1)
    return "lala", 501


