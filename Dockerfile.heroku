FROM python:3.10-slim-buster


COPY ./devops/docker/requirements.txt ./

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean \
    && pip install --no-cache-dir -r requirements.txt


COPY . /code
WORKDIR /code/

ENV PYTHONPATH $PYTHONPATH:/code/

CMD ["uvicorn", "api.app:app", "--reload", "--host", "0.0.0.0", "--port", "6400"]