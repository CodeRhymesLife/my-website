FROM python:3.7.6-slim

RUN apt-get -y update
RUN apt-get -y install git

WORKDIR /my-website

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

# Build the web assets
WORKDIR /my-website/app
RUN python utils/assets.py

WORKDIR /my-website

ENTRYPOINT ["python"]
CMD ["main.py"]