FROM python:3.8-slim-buster


WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./src /app

EXPOSE 5555
ENTRYPOINT [ "python", "-u", "ventilator.py" ]
