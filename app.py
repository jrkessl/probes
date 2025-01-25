import os
import random 
from flask import Flask
import time
from threading import Lock 

app = Flask(__name__)
lock = Lock()

if __name__ == "__main__":
    app.run()

counter1 = 10
globalerror = False
counter2 = 10
ready = False 
readycounter = os.getenv("READYCOUNTER", "10")
slowquerycounter = os.getenv("SLOWQUERYCOUNTER", "60")
slowquerygrace = os.getenv("SLOWQUERYGRACE", "3")

@app.route('/safe', methods=['GET']) # This just answers with code 200 
def safe():
    with lock: 
        global ready
        global readycounter
        if globalerror == True: 
            return f"App is \"broken down\" meaning the server process still runs, but the app only returns error codes.", 502

        if not ready:
            time.sleep(int(readycounter))
            ready = True
            return "Application is initialized. Safe request completed", 201 
            
        return "Safe request completed", 200 

@app.route('/crash_tenth', methods=['GET']) # This returns OK most of the time, because it causes the server to crash every 10th request. 
def crash_tenth():
    with lock:
        global ready
        global readycounter
        if not ready:
            time.sleep(int(readycounter))
            ready = True

        global counter1
        counter1 = counter1 - 1 
        if counter1 < 1:
            os._exit(1)
        else:
            if globalerror == True: 
                return f"App is \"broken down\" meaning the server process still runs, but the app only returns error codes.", 502
            else:
                return f"Crashing in {counter1}", 200 

@app.route('/break_tenth', methods=['GET']) # This, every 10 requests, will cause the server process to enter an invalid state, where it only responds with errors until restarted. 
def break_tenth():
    with lock:
        global ready
        global readycounter
        if not ready:
            time.sleep(int(readycounter))
            ready = True

        global counter2
        global globalerror
        counter2 = counter2 - 1 
        if counter2 < 1:
            globalerror = True
        if globalerror == True: 
            return f"App is \"broken down\" meaning the server process still runs, but the app only returns error codes.", 502
        else:
            return f"App will \"break down\" in {counter2}", 200

@app.route('/error', methods=['GET']) # This always responds with error codes. Does not affect the server process. 
def error():
    with lock:        
        global ready
        global readycounter
        if not ready:
            time.sleep(int(readycounter))
            ready = True
        return "Here is your error!", 501 

@app.route('/slowquery', methods=['GET']) # This most of the times returns quickly, but sometimes it blocks, holding down the server for a long while. 
def slowquery():
    with lock:
        global ready
        global readycounter
        if not ready:
            time.sleep(int(readycounter))
            ready = True
        
        global slowquerycounter
        global slowquerygrace
        slowquerycounter_i = int(slowquerycounter)
        slowquerygrace_i = int(slowquerygrace)
        if slowquerygrace_i > 0: # On the first 3 calls, never slow down. 
            slowquerygrace = slowquerygrace_i - 1
        else:
            random_number = random.randint(0, 2) # Have a chance of 1 in 3 of this function taking a lot of time to return. 
            print (f"random_number = {random_number}")
            if random_number == 2:
                time.sleep(int(slowquerycounter_i))
                return "Slow query call finished. This time it was slow.", 200
        return "Slow query call finished (quickly).", 200
