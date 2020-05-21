FROM python:3.7

COPY . /app

WORKDIR /app

COPY . /model.pkl

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD python3 app.py
