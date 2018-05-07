"""
Gets agreements available to a user in account (same data as 'manage page' in webUI)
Usage:
token_string = '3AAABLblqZhC2YTAO******* Your integration key or access token ************ohF9DaLV-4GKbLuiM-0lmTtSq'
sender_email = 'skaboy71@gmail.com'
user_agreement_list = list_agreements(token_string, sender_email)
pprint(user_agreement_list)
pprint(user_agreement_list[0]['displayUserSetInfos'][0]['displayUserSetMemberInfos'][0]['email'])
"""
import requests
import json
from pprint import pprint # if needed for pprint

def list_agreements(token_string, sender_email):
    shard = 'na1'
    baseUrl = 'https://api.' + shard + '.echosign.com/api/rest/v5'
    agUrl = baseUrl + '/agreements'
    headers = {
        'Access-Token': token_string,  # Your access token or integration key here.
        'x-user-email': sender_email
    }
    url = agUrl
    return requests.get(url, headers=headers).json().get('userAgreementList')
