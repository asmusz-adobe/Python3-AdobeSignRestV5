"""
Gets all available agreement info including status, events, recipients, name ect
See REST example call https://www.evernote.com/l/AgVX4E3HakZJ76-TOCm2ABHaZoa4Kb6Lxws
Usage:
token_string = '3AAABLblqZhC2YTAO******* Your integration key or access token ************ohF9DaLV-4GKbLuiM-0lmTtSq'
sender_email = 'skaboy71@gmail.com'
agreement_id = '3AAABLblqZhBJmhc*************** Agreement ID here ******************AFDPtDiM4fQnVjJ0owy-pO'
agreement_info = get_agreement_info(token_string, sender_email, agreement_id)
pprint(agreement_info)
pprint(agreement_info['events'][0]['actingUserIpAddress'])
"""

import requests
import json
from pprint import pprint # if needed for pprint

def get_agreement_info(token_string, sender_email, agreement_id):
    shard = 'na1'
    baseUrl = 'https://api.' + shard + '.echosign.com/api/rest/v5'
    agUrl = baseUrl + '/agreements/' + agreement_id
    headers = {
        'Access-Token': token_string,  # Your access token or integration key here.
        'x-user-email': sender_email
    }
    url = agUrl
    return requests.get(url, headers=headers).json()
