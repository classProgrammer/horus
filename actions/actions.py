# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, SlotSet
from rasa_sdk.events import Restarted # to restart the bot after successfull conversation

import requests
import json


class SicknessForm(FormAction):

    def name(self) -> Text:
        return "sickness_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "dob"]

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    #     return { "name": self.from_entity(entity="name"), 
    #              "dob": self.from_entity(entity="dob")}

    def asEventMessage(self, message, data = {}):
        return {"event": "bot", "text": message, "data": data}

    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("Found", value)

        if (len(value.split(" ")) != 2):
            print("wrong")
            return {"num_people": None}
        
        print("OK")
        return {"name": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        name = tracker.current_slot_values()["name"].lower()
        dob = tracker.current_slot_values()["dob"]
        data = json.dumps({
            "name": name,
            "dob": dob
        })

        headers = {'Content-type': 'application/json'}
        url = 'https://resteasy.azurewebsites.net/sick'
        response = requests.post(url, data=data, headers=headers)
        print(response)

        if (response.ok):
            return [self.asEventMessage("Informationen erfolgreich gespeichert")]

        return [self.asEventMessage("Die eingegebenen Inromationen sind nicht korrekt, Konversation wird zurückgesetzt"), Restarted()]

class WelcomeAction(Action):
    def name(self):
        return "action_welcome" # include action in domain file

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return []


class RestartAction(Action):
    def name(self):
        return "action_restart" # include action in domain file

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]