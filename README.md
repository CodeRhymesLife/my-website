# my-website
My website

## Setup
1) Install [virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
2) Create a new virtual envrionment ```virtualenv venv```
3) Activate the virtual env ```source venv/bin/activate```
4) Install dependencies ```pip install -r requirements.txt```
5) Point flask to the correct entry point ```cp .flaskenv.example .flaskenv```

## Docker

```shell
$ docker build -t rcjames/ryan-james-health-dot-com .
```

## Heroku

```shell
$ git push heroku master
```