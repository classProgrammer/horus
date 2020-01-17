## general greeting
* greet
    - utter_greet

## general how are you
* how_are_you
    - utter_how_are_you

## general chitchat
* chitchat
    - utter_help

## general bye
* goodbye
    - utter_goodbye
    - action_restart

## general can do
* cando
    - utter_i_can_do

## general bot question
* are_you_a_bot
    - utter_i_am_a_bot

## general thanks
* thanks
    - utter_thanks
    - action_restart

## Happy 1
* sickness
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"requested_slot":"name"}
* fetch_sickness_data{"name":"Franz Bauer"}
    - sickness_form
    - slot{"name":"Franz Bauer"}
    - form{"name":null}
    - slot{"requested_slot":null}

## Happy 3
* sickness
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"requested_slot":"name"}
* fetch_sickness_data{"name":"Werner Kurschel","dob":"05.02.1967"}
    - sickness_form
    - slot{"dob":"05.02.1967"}
    - slot{"name":"Werner Kurschel"}
    - form{"name":null}
    - slot{"requested_slot":null}

## unhappy 1
* sickness
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"requested_slot":"name"}
* stop
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_stop
    - utter_help
    - action_restart

# unhappy 2
* sickness
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"requested_slot":"name"}
* fetch_sickness_data{"dob":"04.02.1977"}
    - sickness_form
    - slot{"dob":"04.02.1977"}
    - slot{"requested_slot":"name"}
* stop
    - action_deactivate_form
    - form{"name":null}
    - utter_stop
    - utter_help
    - action_restart
