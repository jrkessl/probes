# Probes
This code was written to test how Kubernetes Deployment probes work, to write [this article explaining the difference between probes](https://medium.com/@jrkessl/readiness-vs-liveness-probes-what-is-the-difference-and-startup-probes-215560f043e4), and to offer code samples. 

It contains 5 Kubernetes Deployment manifests (files 01 to 05) that all deploy the same app `app.py`, and a Python app that responds to HTTP GET requests in some prefixes. Read the [article](https://medium.com/@jrkessl/readiness-vs-liveness-probes-what-is-the-difference-and-startup-probes-215560f043e4), it's all in there. 

### Running the code 
See these instructions if you for any reason wants to run the Python code locally. All but the last command is meant to be run from the project folder.

 * `python3 -m venv venv0` # just once, to create the Python virtual environment
 * `source venv0/bin/activate` # to enable the virtual environment every time you come back to it 
 * `python -m pip install -r requirements.txt` # to install requirements; do it once or if you change requirements.
 * `flask --debug --app app.py run -p 8080` # to run the app locally. 
 * `curl localhost:8080/<prefix>` # to test the app. For `<prefix>` use one of the prefixes you will see in `app.py`.
