FROM python:3.10-slim

COPY . /app
WORKDIR /app

RUN pip install pip --upgrade \
    && pip install -r requirements.txt

COPY run.sh /app/
RUN chmod +x /app/run.sh

# Use ENTRYPOINT to specify the default command and arguments
ENTRYPOINT ["/app/run.sh"]
