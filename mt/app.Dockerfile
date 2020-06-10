FROM rasa/rasa:1.4.6

LABEL maintainer="Spenlingwimer Gerald" version="1.5"

COPY ./ /app

CMD [ "run", "--enable-api", "--cors", "*" ]