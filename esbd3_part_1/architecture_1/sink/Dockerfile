FROM python:3.8-slim-buster
WORKDIR /app
COPY ./ /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5556
ENTRYPOINT [ "python", "-u", "sink.py"]
