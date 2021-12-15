FROM python:3-alpine

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./main.py .

EXPOSE 8000

CMD [ "python", "main.py" ]