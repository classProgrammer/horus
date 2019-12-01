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

## happy 1
* sickness
    - utter_authorize
* fetch_sickness_data{"name":"Gerwald Witcher","dob":"12.09.19956"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Gerwald Witcher"}
    - slot{"dob":"12.09.19956"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## happy 2
* sickness 
    - utter_authorize
* fetch_sickness_data{"name":"Julian Border"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Julian Border"}
    - slot{"requested_slot":"dob"}
* fetch_sickness_data{"dob":"12.12.2012"}
    - sickness_form
    - slot{"dob":"12.12.2012"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## happy 3
* sickness
    - utter_authorize
* fetch_sickness_data{"dob":"30.11.2014"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"dob":"30.11.2014"}
    - slot{"requested_slot":"name"}
* fetch_sickness_data{"name":"Johan Heinzelreiter"}
    - sickness_form
    - slot{"name":"Johan Heinzelreiter"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## happy 4
* sickness
    - utter_authorize
* fetch_sickness_data{"name":"Stefani Quenn"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Stefani Quenn"}
    - slot{"requested_slot":"dob"}
* fetch_sickness_data{"dob":"26.07.1987"}
    - sickness_form
    - slot{"dob":"26.07.1987"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## happy 5
* sickness
    - utter_authorize
* fetch_sickness_data{"name":"Madonna Marinello"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"name":"Madonna Marinello"}
    - slot{"requested_slot":"dob"}
* fetch_sickness_data{"dob":"05.05.19988"}
    - sickness_form
    - slot{"dob":"05.05.19988"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## happy 6
* sickness
    - utter_authorize
* fetch_sickness_data{"dob":"15.04.1999"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"dob":"15.04.1999"}
    - slot{"requested_slot":"name"}
* fetch_sickness_data{"name":"Cirilla Vanilla"}
    - sickness_form
    - slot{"name":"Cirilla Vanilla"}
    - action_restart
