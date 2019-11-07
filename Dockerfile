FROM ubuntu:16.04
RUN apt-get update -y && \
apt-get install -y python-pip python-dev build-essential net-tools
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000:5000
CMD python app/index.py
