FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /app

WORKDIR /app
EXPOSE 8000
RUN python -m pip install --upgrade pip && \
    pip install -r /requirements/development.txt

RUN chmod -R +x /scripts


ENV PATH="/scripts:py/bin:$PATH"

CMD ["run.sh"]



