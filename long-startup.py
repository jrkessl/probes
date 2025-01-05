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
    with lock: # This ensures this block of code runs serialized, and not in parallel, if it gets called 2 times or more simultaneously.
        initialized = app.config.get('initialized') # Are we already initialized?
        if not initialized:
            time.sleep(120) # Some long initialization procedure...
            app.config.update(initialized=True) # Then mark it as initialized. So this does not take place next time this function runs.
    return "business request completed", 200

@app.route('/crash', methods=['GET'])
def crash():
    with lock: # This ensures this block of code runs serialized, and not in parallel, if it gets called 2 times or more simultaneously.
        os._exit(1) # Fakes a crash, by exiting the app with a non-zero return code. 
    return "lala", 501


