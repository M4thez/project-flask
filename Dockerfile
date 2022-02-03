FROM python:3.10.0
ADD . /app
WORKDIR /app
RUN pip install -r req.txt