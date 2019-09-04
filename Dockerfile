FROM python:3

RUN mkdir /code \
&&apt-get update
COPY requirements.txt /code
#RUN pip install -r /code/requirements.txt 
RUN pip install --no-cache-dir -r /code/requirements.txt
WORKDIR /code

CMD ["python","app.py"]
