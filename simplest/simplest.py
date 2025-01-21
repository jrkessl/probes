import os
import random 
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

counter = 0 

# This is the code that runs when you call the prefix "/business"
@app.route('/business', methods=['GET'])
def business():
    global counter
    counter = counter + 1 
    if counter == 10:
        os._exit(1)
    else:
        return "business request completed", 200 # It does not do anything. Just returns immediately. But it crashes on every 10th request. 
