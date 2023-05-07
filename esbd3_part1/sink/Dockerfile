FROM python:3.8-slim-buster



WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5556

COPY ./src /app



ENTRYPOINT [ "python", "-u", "sink.py"]
