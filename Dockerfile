FROM python:3.10-slim

COPY . /app
WORKDIR /app

RUN pip install pip --upgrade
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput


RUN chmod +x run.sh

CMD ["./run.sh"]
