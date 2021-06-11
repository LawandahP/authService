FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /authApp
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
# install system dependencies

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /authApp/requirements.txt
RUN pip install -r requirements.txt
COPY . /authApp
