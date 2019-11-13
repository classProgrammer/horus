# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import Restarted # to restart the bot after successfull conversation

class RestartAction(Action):
    def name(self):
        return "action_restart" # include action in domain file

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]


class SicknessForm(FormAction):

    def name(self) -> Text:
        return "sickness_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "dob"]

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    #     return {
    #         "name": self.from_entity(entity="name"),
    #     }


    # @staticmethod
    # def is_int(string: Text) -> bool:
    #     """Check if a string is an integer"""

    #     try:
    #         int(string)
    #         return True
    #     except ValueError:
    #         return False

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
            dispatcher.utter_template("utter_ask_name", tracker)
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

        print("IN SUBMIT")

        # utter submit template
        #dispatcher.utter_template("confirm", tracker)
        return []
