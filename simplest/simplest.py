import os
import random 
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

# This is the code that runs when you call the prefix "/business"
@app.route('/business', methods=['GET'])
def business():
    random_number = random.randint(0, 9)
    if random_number == 0:
        os._exit(1)
    else:
        return "business request completed", 200 # It does not do anything. Just returns immediately.

# @app.route('/crash', methods=['GET'])
# def crash():
#     os._exit(1)
#     return "lala", 501


