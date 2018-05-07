'''
This gets the "signingUrl" for a "serial" send (1 URL only)

Usage:  SigningURL = get_signing_url("*** Your api token or integration key here ***", "*** an agreement/document key from earlier send here ***"):

'''
import requests
import json
import time


def get_signing_url(api_token, agreementId):
    shard = 'na1'
    base_url = 'https://api.' + shard + '.echosign.com/api/rest/v5'
    agmts_url = base_url + '/agreements'
    headers = {
        'Access-Token': api_token,  #
    }
    url = agmts_url + "/" + agreementId + "/signingUrls"
    sUrl1 = ''
    while "https://" not in sUrl1:
        request1 = requests.get(agmts_url, headers=headers)
        this_json = request1.json()
        rec1 = this_json.get('signingUrlSetInfos', {})[0]
        sUrl1 = rec1.get('signingUrls', {})[0]['esignUrl']
        time.sleep(.3)  # If no URL in response wait 3 tenths of a second and try again
    return sUrl1
