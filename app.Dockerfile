FROM rasa/rasa:latest

LABEL maintainer="Spenlingwimer Gerald" version="1.4"

COPY ./ /app

CMD [ "run", "--enable-api", "--cors", "*" ]