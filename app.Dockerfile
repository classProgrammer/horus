FROM rasa/rasa:latest

LABEL maintainer="Spenlingwimer Gerald" version="1.5"

COPY ./ /app

CMD [ "run", "--enable-api", "--cors", "\"*\""" ]