import os
import random 
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

counter = 0 

# This is the code that runs when you call the prefix "/safe"
@app.route('/safe', methods=['GET'])
def safe():
    return "Safe request completed", 200 # It does not do anything. Just returns immediately. But it crashes on every 10th request. 


@app.route('/crash_tenth', methods=['GET'])
def crash_tenth():
    global counter
    counter = counter + 1 
    if counter == 10:
        os._exit(1)
    else:
        return f"Crashing in {counter}", 200 # It returns OK most of the time; there is a random risk of crashing. 

@app.route('/error', methods=['GET'])
def error():
    return "Here is your error!", 500 # Always returns an error. But the server process is unaffected. 
