## general greeting
* greet
    - utter_greet
    - action_restart

## general how are you
* how_are_you
    - utter_how_are_you
    - action_restart

## general chitchat
* chitchat
    - utter_greet
    - action_restart

## general bye
* goodbye
    - utter_goodbye
    - action_restart

## general can do
* cando
    - utter_i_can_do
    - action_restart

## general bot question
* are_you_a_bot
    - utter_i_am_a_bot
    - action_restart

## general thanks
* thanks
    - utter_thanks
    - action_restart

## unahppy stop 1
* sickness
    - utter_authorize
* stop
    - utter_stop
    - action_restart

## unhappy stop in the middle
* sickness
    - utter_authorize
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
    - action_restart

## happy path 1
* sickness
    - utter_authorize
* fetch_sickness_data{"name":"Harry Potter","dob":"24.05.1965"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Harry Potter"}
    - slot{"dob":"24.05.1965"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_get_well_soon_with_name
    - action_restart

## happy path 2
* sickness
    - utter_authorize
* fetch_sickness_data{"name":"Alfons Houthen"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Alfons Houthen"}
    - slot{"requested_slot":"dob"}
* fetch_sickness_data{"dob":"12.12.2012"}
    - sickness_form
    - slot{"dob":"12.12.2012"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_get_well_soon_with_name
    - action_restart

## happy path 3
* sickness
    - utter_authorize
* fetch_sickness_data{"dob":"30.09.2000"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"dob":"30.09.2000"}
    - slot{"requested_slot":"name"}
* fetch_sickness_data{"name":"Elias Markdown"}
    - sickness_form
    - slot{"name":"Elias Markdown"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_get_well_soon_with_name
    - action_restart
    
## unhappy break after dob
* sickness
    - utter_authorize
* fetch_sickness_data{"dob":"23.06.1967"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"dob":"23.06.1967"}
    - slot{"requested_slot":"name"}
* stop
    - utter_stop
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart