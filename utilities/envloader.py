import os
from dotenv import load_dotenv


class envloader:

    load_dotenv()

    def getToken():
        TOKEN = os.getenv('DISCORD_TOKEN')
        return TOKEN

    def getGuild():
        GUILD = os.getenv('DISCORD_GUILD')
        return GUILD
