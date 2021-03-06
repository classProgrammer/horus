# Masterthesis Chatbot Project

## Rasa Structure
 - nlu: Intent Definition
 - domain: Definition of all adressable components
 - stories: Definition of conversation structures/scripts
 - actions: Validation and processing of data

## Rasa Install Guide
- [Rasa Get Started](https://rasa.com/docs/getting-started/)

## Project Lifecycle Methods
### Train the Network:
```shell
shell@something/.../horus> rasa train
```
### Start the Action Server
```shell
shell@something/.../horus> rasa run actions
```

### Start the local Rasa Shell
```shell
shell@something/.../horus> rasa shell
```

### Start Rasa-X (Browser)
```shell
shell@something/.../horus> rasa x
```

### Run Rasa as local HTTP Server
```shell
shell@something/.../horus> rasa run --enable-api --cors "*"
```
Local Address: http://localhost:5005/webhooks/rest/webhook

Request Body:
```json
{
  "sender": "other",
  "message": "hallo"
}
```

### Rasa in a local Docker Container
#### Startup Command
```shell
docker-compose up
```
#### Docker Compose File
```yml
version: '3.0'
services:
  rasa:
    image: rasa/rasa:1.4.6
    ports:
      - 80:5005
    networks: 
      - app_net
    volumes:
      - ./:/app
    command:
      run 
      --enable-api
      --cors *
    
  action_server:
    image: rasa/rasa-sdk:1.4.0    
    volumes:
      - ./actions:/app/actions
    expose: 
      - 5055
    networks: 
      - app_net

networks: 
  app_net:
```
#### run the shell
```shell
    docker run -it -v %cd%:/app rasa/rasa:1.4.6 shell
```
#### train custom model
```shell
    docker run -v %cd%:/app rasa/rasa:1.4.6 train --domain domain.yml --data data --out models
```

### Rasa Azure Docker Container

Addresses: 
  - [Base](https://3bitrasa.azurewebsites.net/)
  - [Rest](https://3bitrasa.azurewebsites.net/webhooks/rest)
  - [Requests](https://3bitrasa.azurewebsites.net/webhooks/rest/webhook)
  
```shell
docker build -t horusrasaregistry.azurecr.io/rasa/rasa-sdk:custom .

docker push horusrasaregistry.azurecr.io/rasa/rasa-sdk:custom

docker build -f app.Dockerfile -t horusrasaregistry.azurecr.io/rasa/rasa:custom2 .

docker push horusrasaregistry.azurecr.io/rasa/rasa:custom2
```
#### Action Server Image
```dockerfile
FROM rasa/rasa-sdk:latest
LABEL maintainer="Spenlingwimer Gerald" version="1.0"
COPY ./actions /app/actions
```
#### Rasa Image
```dockerfile
FROM rasa/rasa:latest
LABEL maintainer="Spenlingwimer Gerald" version="1.4"
COPY ./ /app
CMD [ "run", "--enable-api", "--cors", "*" ]
```
#### Azure Compose File
```yml
version: '3.0'
services:
  rasa:
    image: horusrasaregistry.azurecr.io/rasa/rasa:custom2
    ports:
      - 80:5005
    networks: 
      - app_net
    
  action_server:
    image: horusrasaregistry.azurecr.io/rasa/rasa-sdk:custom2
    expose: 
      - 5055
    networks: 
      - app_net
networks: 
  app_net:
```

## Source of Information
- [Rasa Documentation](https://rasa.com/docs/)
