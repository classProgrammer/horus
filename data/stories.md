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

## unahppy 1
* sickness
    - utter_authorize
* stop
    - utter_stop
    - action_restart

## unhappy 2
* greet
    - utter_greet
* sickness
    - utter_authorize
* stop
    - utter_stop

## happy full
* sickness
    - utter_authorize
* fetch_sickness_data{"name":"Hans Wurst","dob":"27.04.1997"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Hans Wurst"}
    - slot{"dob":"27.04.1997"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye

## happy 2
* sickness
    - utter_authorize
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Johan Aichberger"}
    - utter_ask_dob
    - slot{"dob":"15.07.1996"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye

## happy 3
* sickness
    - utter_authorize
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"dob":"26.09.19954"}
    - utter_ask_name
    - slot{"name":"Anna Fakename"}
    - form{"name":null}
    - slot{"requested_slot":null}
* goodbye
    - utter_goodbye