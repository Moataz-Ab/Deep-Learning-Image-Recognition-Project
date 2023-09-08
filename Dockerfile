FROM python:3.10.6-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

# CMD recognition.api.fast:app --host 0.0.0.0 --port $PORT
CMD ["uvicorn", "recognition.api.fast:app", "--host", "0.0.0.0"]

