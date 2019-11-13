## simple greeting + goodbye
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart


<!-- ## sick with intro and ending
* greet
    - utter_greet
* sickness
    - utter_get_well_soon
* goodbye
    - utter_goodbye -->

## happy, holiday
* greet
    - utter_greet
* holiday
## happy, sickness
* greet
    - utter_greet
* sickness
    - utter_authorize
* fetch_sickness_data
    - sickness_form
    - form{"name": "sickness_form"}
    - form{"name": null}
    - utter_get_well_soon_with_name 
* goodbye
    - utter_goodbye
    - action_restart

## happy, sickness fetch users name, no intro
* sickness
    - utter_authorize
* fetch_sickness_data
    - sickness_form
    - form{"name": "sickness_form"}
    - form{"name": null}
    - utter_get_well_soon_with_name 
* goodbye
    - utter_goodbye
    - action_restart