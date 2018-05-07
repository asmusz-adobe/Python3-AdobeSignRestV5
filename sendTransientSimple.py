'''
Sends "transient doc" as agreement with one signer and "SENDER_SIGNATURE_NOT_REQUIRED"
No "merge" data
Usage:  agreement_id = send_trans_doc_no_merge_one_signer("*** Your api token or integration key here ***",
                                                         "*** trans ID here ***", "sender@yourdomain.com", "signer@theirdomain.com", "Your agreement Name here", 
                                                         "Please sign this agreement from us.")
'''
import requests
import json


def send_trans_doc_no_merge_one_signer(api_token, transID, sender_email, recipEmail, agName, _message):
    shard = 'na1'
    base_url = 'https://api.' + shard + '.echosign.com/api/rest/v5'
    agmts_url = base_url + '/agreements'

    headers = {
        'Access-Token': api_token,
        'x-user-email': sender_email,
        'Content-Type': 'application/json'
    }
    data = {
        "documentCreationInfo": {
            "signatureType": "ESIGN",
            "recipientSetInfos": [
                {
                    "recipientSetMemberInfos": [
                        {
                            "email": recipEmail
                        }
                    ],
                    "recipientSetRole": "SIGNER"
                }
            ],
            "signatureFlow": "SENDER_SIGNATURE_NOT_REQUIRED",
            "message": _message,
            "fileInfos": [
                {
                    "transientDocumentId": transID
                }
            ],
            "name": agName
        }

    }
    url = agmts_url
    return requests.post(url, headers=headers, data=json.dumps(data)).json().get('agreementId')
