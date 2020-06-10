## Greeting Story
* greeting
	- utter_greet

## Goodbye Story
* goodbye
	- utter_goodbye

## Thanks Story
* thank_you
    - utter_thank_you

## Sickness Affirm
* sickness
    - sickness_form
    - form{"name":"sickness_form"}
* submit{"PERSON":"Anna Maria Müller"}
    - sickness_form
    - slot{"PERSON":"Anna Maria Müller"}
* submit{"time":"2020-05-30T00:00:00.000-07:00","DATE":"today"}
    - sickness_form
    - form{"name":null}
    - slot{"time":"2020-05-30T00:00:00.000-07:00"}
* affirm
    - action_submit_sickness_data
    - action_restart

## Sickness Deny
* sickness
    - sickness_form
    - form{"name":"sickness_form"}
* submit{"PERSON":"Anna Maria Müller"}
    - sickness_form
    - slot{"PERSON":"Anna Maria Müller"}
* submit{"time":"2020-05-30T00:00:00.000-07:00","DATE":"today"}
    - sickness_form
    - form{"name":null}
    - slot{"time":"2020-05-30T00:00:00.000-07:00"}
* deny
    - utter_aborted
    - utter_retry_sick
    - action_restart

## Submit All Affirm
* sickness{"time":{"to":"2020-06-02T00:00:00.000-07:00","from":null},"PERSON":"Max Franz","DATE":"Tuesday"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"PERSON":"Max Franz"}
* affirm
    - action_submit_sickness_data
    - action_restart

## Submit All Deny
* sickness{"time":{"to":"2020-06-02T00:00:00.000-07:00","from":null},"PERSON":"Max Franz","DATE":"Tuesday"}
    - sickness_form
    - form{"name":"sickness_form"}
    - slot{"PERSON":"Max Franz"}
* deny
    - utter_aborted
    - utter_retry_sick
    - action_restart

## Vacation Affirm
* vacation
    - vacation_form
    - form{"name":"vacation_form"}
    - slot{"requested_slot":"PERSON"}
* submit{"PERSON":"Alice Chains"}
    - vacation_form
    - slot{"PERSON":"Alice Chains"}
* submit{"time":{"to":"2020-06-13T00:00:00.000-07:00","from":"2020-06-02T00:00:00.000-07:00"},"DATE":"06/02/2020"}
    - sickness_form
    - form{"name":null}
    - slot{"time":"2020-05-30T00:00:00.000-07:00"}
* affirm
    - action_submit_vacation_data
    - action_restart

## Vacation Deny
* vacation
    - vacation_form
    - form{"name":"vacation_form"}
    - slot{"requested_slot":"PERSON"}
* submit{"PERSON":"Alice Chains"}
    - vacation_form
    - slot{"PERSON":"Alice Chains"}
* submit{"time":{"to":"2020-06-13T00:00:00.000-07:00","from":"2020-06-02T00:00:00.000-07:00"},"DATE":"06/02/2020"}
    - sickness_form
    - form{"name":null}
    - slot{"time":"2020-05-30T00:00:00.000-07:00"}
* deny
    - utter_aborted
    - utter_retry_vaction
    - action_restart
