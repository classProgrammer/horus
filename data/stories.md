## simple greeting + goodbye
* greet
    - utter_greet
* goodbye
    - utter_goodbye


<!-- ## sick with intro and ending
* greet
    - utter_greet
* sickness
    - utter_get_well_soon
* goodbye
    - utter_goodbye -->

## happy, sickness
* greet
    - utter_greet
* fetch_sickness_data
    - sickness_form
    - form{"name": "sickness_form"}
    - sickness_form
    - form{"name": null}
    - sickness_form
    - utter_get_well_soon_with_name 
* goodbye
    - utter_goodbye

## happy, fetch users name, no intro
* fetch_sickness_data
    - sickness_form
    - form{"name": "sickness_form"}
    - sickness_form
    - form{"name": null}
    - sickness_form
    - utter_get_well_soon_with_name 
* goodbye
    - utter_goodbye