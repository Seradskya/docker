FROM python:3.11-bullseye

WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY ./backend/requirements.txt .
RUN pip install -r requirements.txt

# for migrations
COPY ./backend/pyproject.toml .

# for statrat app
COPY ./docker/backend/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/backend/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT ["/entrypoint"]