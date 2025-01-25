FROM python
COPY app.py . 
COPY requirements.txt . 
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "flask", "--app", "app.py", "run", "--host", "0.0.0.0", "-p", "8080" ]


# tag="simplest_v07" && docker build . -f Dockerfile -t jrkessl/probes:${tag} && docker push jrkessl/probes:${tag}