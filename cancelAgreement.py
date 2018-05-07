"""
Cancels agreement given your API token and the agreement ID
Usage:
agreement_id = '3AAABLblqZhDrhM26Uz_14FQJUk804WV9F4VHug-zu2FWeOStzJWXsmP4yf75PBSBg8xONYPbO3bSl0JY8LsqpP9bzK4RJZ9m'
token_string ='3AAABLblqZhC2Y******* Your api access token or integration key here *******LV-4GKbLuiM-0lmTtSq'
sender_email = 'skaboy71@gmail.com'
comment = 'This needs to be cancelled'
notify_tf = 'false'
cancelled_agreement = cancel_agreement(token_string, agreement_id, sender_email, comment, notify_tf)
pprint(cancelled_agreement)
: param token_string    -- Your API access token or integration key
: param agreement_id    -- The API related agreement ID for the agreement being cancelled
: param sender_email    -- The user context of the sender designated by the email address
: param comment         -- A comment string as to the reason for this cancellation
: param notify_tf         -- true or false to have Adobe Sign send notification to participants about the cancel

"""
import requests
import json
from pprint import pprint

def cancel_agreement(token_string, agreement_id, sender_email, comment = 'This needs to be cancelled', notify_tf = 'false'):
    #  Set up URLs to use for cancel and delete
    shard = 'na1'
    base_url = 'https://api.' + shard + '.echosign.com/api/rest/v5'
    agmts_url = base_url + '/agreements'
    cancelUrl = agmts_url + '/' + agreement_id + '/status'
    print(cancelUrl)

    headers = {
        'Access-Token': token_string,
        'x-user-email': sender_email,
        'Content-Type': 'application/json'
    }

    data_c = {
        "value": "CANCEL",
        "comment": comment,
        "notifySigner": notify_tf
    }

    url = cancelUrl

    cancel_response = requests.put(url, headers=headers, data=json.dumps(data_c)).json()
    print(cancel_response)  #.json()
    return cancel_response

