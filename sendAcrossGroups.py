from discordRequests import sendDiscordMessages
from groupmeRequests import sendGroupMeMessages
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    message = 'SEND TO ALL PLATFORMS'
    sendDiscordMessages(message, os.environ.get('DISCORD_TOKEN'))
    sendGroupMeMessages(message, os.environ.get('GROUPME_TOKEN'))
    

if __name__ == '__main__':
    main()