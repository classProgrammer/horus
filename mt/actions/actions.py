# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, SlotSet
from rasa_sdk.events import Restarted

import requests
import json
import re
import datetime

def getSlot(tracker: Tracker, slotName):
    slot =  tracker.current_slot_values()[slotName]
    if not slot:
        return None
    return slot

def asEventMessage(message, data = {}):
    return {'event': 'bot', 'text': message, 'data': data}

headers = {'Content-type': 'application/json'}
url = 'https://resteasy.azurewebsites.net/sick'

class SicknessForm(FormAction):
    def name(self) -> Text:
        return 'sickness_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['PERSON', 'time']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
             'PERSON': [self.from_entity(entity='PERSON')],
             'time': [self.from_entity(entity='time')],
             'DATE': [self.from_entity(entity='DATE')]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        print(tracker.current_slot_values())

        person = getSlot(tracker, 'PERSON')       
        return_date = getSlot(tracker, 'time')
        if isinstance(return_date, Dict):
            return_date = return_date['to']
        else:
            return_date = return_date.title()

        SlotSet('return_date', return_date, datetime.datetime.now().timestamp())

        date = getSlot(tracker, 'DATE')

        if date == 'today':
            return [asEventMessage(f'Please confirm that {person.title()} is sick')]

        return [asEventMessage(f'Please confirm that {person.title()} is sick until {return_date}.')]

class VacationForm(FormAction):
    def name(self) -> Text:
        return 'vacation_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['PERSON', 'time']

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
             'PERSON': [self.from_entity(entity='PERSON')],
             'time': [self.from_entity(entity='time')],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        print(tracker.current_slot_values())

        person = getSlot(tracker, 'PERSON')       
        dates = getSlot(tracker, 'time')

        if not isinstance(dates, Dict):
             return [asEventMessage(f'Something went wrong. enter vacation to retry.')]

        start_date = dates['from']
        return_date = dates['to']

        return [asEventMessage(f'Please confirm that {person.title()} is on vacation from {start_date} to {return_date}.')]


class RestartAction(Action):
    def name(self):
        return 'action_restart' 

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class SubmitSicknessDataAction(Action):
    def name(self):
        return 'action_submit_sickness_data' 

    def run(self, dispatcher, tracker, domain):
        person = getSlot(tracker, 'PERSON')      
        return_date = getSlot(tracker, 'time')
        date = getSlot(tracker, 'DATE')

        if isinstance(return_date, Dict):
            return_date = return_date['to']
        else:
            return_date = return_date.title()

        if not person:
            return [asEventMessage('No person found. To retry enter sick')]

        if date == 'today':
            return [asEventMessage(f'Submitted that {person.title()} is sick')]

        return [asEventMessage(f'Submitted that {person.title()} is sick until {return_date}')]

class SubmitVacationDataAction(Action):
    def name(self):
        return 'action_submit_vacation_data' 

    def run(self, dispatcher, tracker, domain):
        person = getSlot(tracker, 'PERSON')      
        dates = getSlot(tracker, 'time')

        start_date = dates['from']
        return_date = dates['to']

        if not person:
            return [asEventMessage('No person found. To retry enter vacation')]

        return [asEventMessage(f'Submitted that {person.title()} requested a vacation form {start_date} to {return_date}')]

