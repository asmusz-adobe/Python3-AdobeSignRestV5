"""Uploads pdf document to EchoSign and returns its transientDocumentId
:param access_token: EchoSign Access Token
:param file_path: Absolute or relative path to File
:return string: transientDocumentId
:usage example:   transID = upl_trans('*** api token or integration key ***','./_MSA_noline.pdf','Test1.pdf')
"""
import requests


def upl_trans(api_token, file_path, docName):
    shard = 'na1'
    baseUrl = 'https://api.' + shard + '.echosign.com/api/rest/v5'
    tranUrl = baseUrl + '/transientDocuments'
    headers = {
        'Access-Token': api_token,  # Your access token or integration key here.
    }
    data = {
        'Mime-Type': 'application/pdf',
        'File-Name': docName
    }
    url = tranUrl
    files = {'File': open(file_path, 'rb')}
    return requests.post(url, headers=headers, data=data,files=files).json().get('transientDocumentId')
