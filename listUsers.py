"""
Gets the list of users in an account as a list of 'dictionaries'
Usage:
token_string = '3AAABLblqZhC2YTAO******* Your integration key or access token ************ohF9DaLV-4GKbLuiM-0lmTtSq'
userList = list_users(token_string)
pprint(userList)
access elements of each 'dictionary' using list index + dictionary index
print(userlist[0]['email'])
priint(userlist[0]['company'])
"""

import requests
from pprint import pprint # if needed for pprint

def list_users(api_token):
    shard = 'na1'
    baseUrl = 'https://api.' + shard + '.echosign.com/api/rest/v5'
    usersUrl = baseUrl + '/users'
    headers = {
        'Access-Token': api_token  # Your access token or integration key here.
    }
    url = usersUrl
    return requests.get(url, headers=headers).json().get('userInfoList')
