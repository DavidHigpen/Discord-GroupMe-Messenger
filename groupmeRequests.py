import requests
import string
import random

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def randomString(stringLength):
    letters = string.ascii_lowercase + "1234567890"
    return ''.join(random.choice(letters) for i in range(stringLength))

def sendGroupMeMessages(message, token):
    groupids = [100244761, 100244772]

    for groupid in groupids:
        accesstoken = token
        headers = {
            'Host': 'api.groupme.com',
            'X-Access-Token': accesstoken,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko 20100101 Firefox/124.0',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        data = '{"message":{"source_guid":"'+randomString(25)+'","attachments":[],"text":"'+message+'"}}'

        response = requests.post('https://api.groupme.com/v3/groups/'+str(groupid)+'/messages', headers=headers, data=data, verify=False)