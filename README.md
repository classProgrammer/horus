# Masterarbeit Projekt Chatbot

## Rasa Struktur
 - nlu: Definition aller Intents
 - domain: Definition von allem das Namentlich angesprochen werden soll
 - stories: Definition des Konversationsflusses
 - actions: Validierung und Verarbeitung von Daten die der Nutzer eingiebt

## Rasa Installation
- [Rasa Get Started](https://rasa.com/docs/getting-started/)

## Ausführen des Projekts
### Trainierne des Netzwerks:
```shell
shell@something/.../horus> rasa train
```
### Starten des Action Servers von Rasa
```shell
shell@something/.../horus> rasa run actions
```

### Starten der lokalen Rasa Shell
```shell
shell@something/.../horus> rasa shell
```

### Starten von Rasa-X (Browser Umgebung)
```shell
shell@something/.../horus> rasa x
```

### Rasa als lokalen HTTP Server verwenden
```shell
shell@something/.../horus> rasa run --enable-api --cors "*"
```
Erreichbar unter http://localhost:5005/webhooks/rest/webhook

Request Body:
```json
{
  "sender": "other",
  "message": "hallo"
}
```

## Referenzen
- [Rasa Dokumentation](https://rasa.com/docs/)
