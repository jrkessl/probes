import os
import random 
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

counter1 = 10
globalerror = False
counter2 = 10

# This is the code that runs when you call the prefix "/safe"
@app.route('/safe', methods=['GET'])
def safe():
    if globalerror == True: 
        return f"App is \"broken down\" meaning the server process still runs, but the app only returns error codes.", 502
    else:
        return "Safe request completed", 200 # It does not do anything. Just returns immediately.

@app.route('/crash_tenth', methods=['GET'])
def crash_tenth():
    global counter1
    counter1 = counter1 - 1 
    if counter1 < 1:
        os._exit(1)
    else:
        if globalerror == True: 
            return f"App is \"broken down\" meaning the server process still runs, but the app only returns error codes.", 502
        else:
            return f"Crashing in {counter1}", 200 # It returns OK most of the time, because it causes the server to crash every 10th request. 

@app.route('/break_tenth', methods=['GET'])
def break_tenth():
    global counter2
    global globalerror
    counter2 = counter2 - 1 
    if counter2 < 1:
        globalerror = True
    if globalerror == True: 
        return f"App is \"broken down\" meaning the server process still runs, but the app only returns error codes.", 502
    else:
        return f"App will \"break down\" in {counter2}", 200

@app.route('/error', methods=['GET'])
def error():
    return "Here is your error!", 501 # Always returns an error. But the server process is unaffected. 
