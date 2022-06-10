FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --update-cache add gcc libc-dev

RUN pip install -U pip
RUN pip install Django gunicorn

COPY ./entrypoint.sh /
CMD ["/entrypoint.sh"]
