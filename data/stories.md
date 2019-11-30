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

## unahppy 1
* sickness
    - action_slot_reset
    - utter_ask_name
* stop
    - utter_stop

## unhappy 2
* greet
    - utter_greet
* sickness
    - action_slot_reset
    - utter_ask_name
* stop
    - utter_stop

## happy path 1
* greet
    - utter_greet
* cando
    - utter_i_can_do
* sickness
    - action_slot_reset
    - utter_ask_name
* fetch_sickness_data{"name":"Harry Potter","dob":"24.05.1965"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Harry Potter"}
    - slot{"dob":"24.05.1965"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_get_well_soon_with_name

## unhappy Break in the Middle
* cando
    - utter_i_can_do
* sickness
    - action_slot_reset
    - utter_ask_name
* fetch_sickness_data{"name":"Franz Bauer"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Franz Bauer"}
    - slot{"requested_slot":"dob"}
* stop
    - utter_stop
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}

## happy path 2
* sickness
    - action_slot_reset
    - utter_ask_name
* fetch_sickness_data{"dob":"31.08.1993","name":"Gerald Spenlingwimmer"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Gerald Spenlingwimmer"}
    - slot{"dob":"31.08.1993"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_get_well_soon_with_name
* thanks
    - utter_thanks

## happy path 3
* sickness
    - action_slot_reset
    - utter_ask_name
* fetch_sickness_data{"dob":"31.08.1993","name":"Gerald Spenlingwimmer"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Gerald Spenlingwimmer"}
    - slot{"dob":"31.08.1993"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_get_well_soon_with_name
* goodbye
    - utter_goodbye