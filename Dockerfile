FROM docker.io/library/python:3

COPY cloudflare_record_set.py /opt/cloudflare_record_set.py

COPY requirements.txt /opt/requirements.txt

RUN ["pip", "install", "-r", "/opt/requirements.txt"]

CMD ["python", "-u", "/opt/cloudflare_record_set.py"]
