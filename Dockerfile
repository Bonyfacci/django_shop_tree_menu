FROM python:3.10

WORKDIR ./app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./src /app
#COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
