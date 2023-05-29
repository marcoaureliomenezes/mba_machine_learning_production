FROM python:3.8-slim-buster
WORKDIR /app
COPY ./ /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5555
ENTRYPOINT [ "python", "-u", "ventilator.py" ]
