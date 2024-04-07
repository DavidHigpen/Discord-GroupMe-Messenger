import requests

def sendDiscordMessages(message, token):
    urls = ['https://discord.com/api/v9/channels/1226342529646071859/messages',
            'https://discord.com/api/v9/channels/1226351339853058099/messages',
            'https://discord.com/api/v9/channels/1226351352846749696/messages',
            'https://discord.com/api/v9/channels/1226351367740854406/messages']

    payload = {
        'content' : message
    }

    headers = {
        'Authorization' : token
    }

    for url in urls:
        data = requests.post(url, payload, headers=headers)