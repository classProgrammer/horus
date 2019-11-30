# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, SlotSet
from rasa_sdk.events import Restarted, AllSlotsReset

import requests
import json

class SicknessForm(FormAction):

    def name(self) -> Text:
        return "sickness_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "dob"]

    def asEventMessage(self, message, data = {}):
        return {"event": "bot", "text": message, "data": data}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

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

        return [self.asEventMessage("Es wurde keine Person zu den eingegebenen Informationen gefunden. Um erneut die Krankmeldung zu probieren bitte Krankmeldung wiederholen eingeben."), Restarted()]

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