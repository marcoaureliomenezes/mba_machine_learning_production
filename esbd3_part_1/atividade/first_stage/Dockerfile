FROM python:3


# Copiar os arquivos necessários para o contêiner
COPY train.py .
COPY predict.py .
COPY requirements.txt .
COPY Crop_recommendation.csv .

RUN pip install -r requirements.txt

CMD ["python3", "train.py"]