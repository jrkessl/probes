FROM python
COPY simplest/simplest.py . 
COPY requirements.txt . 
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
EXPOSE 8080
# ENTRYPOINT gunicorn --bind 0.0.0.0:8001 -w "$workers" wsgi:app
# ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8001", "-w", "$workers", "wsgi:app" ] 
# ENTRYPOINT [ "flask", "--app", "simplest.py", "run", "-p", "8080" ] # this way it only takes connections from localhost.
ENTRYPOINT [ "flask", "--app", "simplest.py", "run", "--host", "0.0.0.0", "-p", "8080" ]


# docker build . -f simplest/Dockerfile -t jrkessl/probes:simplest_v01 && docker push jrkessl/probes:simplest_v01