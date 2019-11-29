## general greeting
* greet
    - utter_greet


## general bye
* goodbye
    - utter_goodbye


## general can do
* cando
    - utter_i_can_do


## general bot question
* are_you_a_bot
    - utter_i_am_a_bot

## general thanks
* thanks
    - utter_thanks

<!-- ## happy, holiday
* greet
    - utter_greet
* holiday -->

## happy, sickness fetch users name, no intro
* sickness
    - utter_authorize
* fetch_sickness_data
    - sickness_form
    - form{"name": "sickness_form"}
    - form{"name": null}
    - utter_get_well_soon_with_name 
    - action_restart

## unahppy #1
* sickness
    - utter_authorize
* fetch_sickness_data
* stop
    - utter_stop
    - action_restart

## uhappy #2
* sickness
    - utter_authorize
* fetch_sickness_data
    - sickness_form
* stop
    - utter_stop
    - action_restart

## uhappy #3
* sickness
    - utter_authorize
* fetch_sickness_data
    - sickness_form
    - form{"name": "sickness_form"}
* stop
    - utter_stop
    - action_restart

## uhappy #4
* sickness
    - utter_authorize
* fetch_sickness_data
    - sickness_form
    - form{"name": "sickness_form"}
    - form{"name": null}
* stop
    - utter_stop
    - action_restart