# coffee-stock
API that allows you to control different stocks of coffees.

![coffee](coffee.jpg)

Application available at https://coffee-stock.herokuapp.com/api/

[![Python 3](https://pyup.io/repos/github/alisonamerico/coffee-stock/python-3-shield.svg)](https://pyup.io/repos/github/alisonamerico/coffee-stock/)
[![Updates](https://pyup.io/repos/github/alisonamerico/coffee-stock/shield.svg)](https://pyup.io/repos/github/alisonamerico/coffee-stock/)
[![Build Status](https://travis-ci.org/alisonamerico/coffee-stock.svg?branch=master)](https://travis-ci.org/alisonamerico/coffee-stock)
[![codecov](https://codecov.io/gh/alisonamerico/coffee-stock/branch/master/graph/badge.svg)](https://codecov.io/gh/alisonamerico/coffee-stock)

Processes used in project development:

Continuous Delivery:

 - Integration with Pipenv Travis and Pyup

 - Automatic Deploy

 - Pytest: To set up and build automated tests for Django.

 - Codecov: For Test Coverage

 - python-decouple: To decouple application instance settings.


How to install locally:
```shell script
git clone https://github.com/alisonamerico/coffee-stock
cd coffee-stock
cp contrib/env-sample .env
```
## Prerequisite Installed:
 - Docker
 - Docker Compose

For Linux(Ubuntu):
https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-engine---community-1

For Mac:
https://docs.docker.com/docker-for-mac/install/
 
For Windows:
https://docs.docker.com/docker-for-windows/install/

We can’t run a Docker container until it has an image so let’s do that by building the image for the first time.
```shell script
docker build .
```

Create migrations:
```shell script
docker-compose run web python manage.py makemigrations
```

Apply migrations:
```shell script
docker-compose run web python manage.py migrate
```

Create SuperUser:
```shell script
docker-compose run web python manage.py createsuperuser
```

Inform:
```shell script
 - username
 - email
 - password
```

We’re finally ready to run Docker itself! 
The first time you execute the command might take a while as Docker has to download all the required content.
But it will cache this information so future spinups will be much faster:
```shell script
docker-compose up
```

List the urls that exist
```shell script
http://0.0.0.0:8000/api/
```

API Root
```shell script
http://0.0.0.0:8000/api/harvest
http://0.0.0.0:8000/api/stock
```
Note: But to view, you must first have:
```shell script
 - username
 - email
 - password
```

which generates a token.

url to login:
```shell script
http://0.0.0.0:8000/rest-auth/login/
```

When you’re done, don’t forget to close down your Docker container.
```shell script
docker-compose down
```

Run the tests:
```shell script
pytest coffee --cov=coffee
```