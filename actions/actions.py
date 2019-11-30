# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, SlotSet
from rasa_sdk.events import Restarted, AllSlotsReset # to restart the bot after successfull conversation

import requests
import json
import re

class SicknessForm(FormAction):

    name_pattern = re.compile("^(([A-Za-zöäüÜÖÄüöäÜÖÄß]{1,}) )(([A-Za-zöäüÜÖÄüöäÜÖÄß]{1,}) ?)*$")
    dob_pattern = re.compile("^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)?\d{2})\s*$")

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
        value = value.strip()
        
        print("Found", value)

        if SicknessForm.name_pattern.match(value):
            print("OK")
            return {"name": value}

        print("wrong")
        return {"name": None}

    def validate_dob(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        value = value.strip()
        
        print("Found", value)

        if SicknessForm.dob_pattern.match(value):
            print("OK")
            return {"dob": value}

        print("wrong")
        return {"dob": None}

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": self.from_entity(entity="name"),
            "dob": self.from_entity(entity="dob")
        }

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

        return [self.asEventMessage("Es wurde keine Person zu den eingegebenen Informationen gefunden. Um erneut die Krankmeldung zu probieren bitte Krankmeldung wiederholen eingeben."), AllSlotsReset()]

class RestartAction(Action):
    def name(self):
        return "action_restart" # include action in domain file

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class SlotResetAction(Action):
    def name(self):
        return "action_slot_reset" # include action in domain file

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]