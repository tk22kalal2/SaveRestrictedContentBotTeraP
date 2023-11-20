#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28698132
API_HASH = "1a2837cd39f87e9b224710af8acd13de"
BOT_TOKEN = "6838710773:AAFeCymPSrz3TqUGQG2y1uEgglpsFGbN0BA"
SESSION = "BQAn2fQ-Rs6rKynfnTHzBi3d4CuvtLvoRVAMACcm0MYIzPrsgHjAw8bsG6qgeEsQXMbXmDZEiH0UDpsD5ZyexzVWMVBK3uVANPB4Ps0z8nCxhQ9gDj39CPAnRzn33Ryx2n0opd8FhLCbHxYt2jbKp73YxkWAmdHBBQ9_0DjckbwZCxKYPn0pUNTAGOn03RxBwj2Wis3tfHEKCM0oZDOgvbrBn1fk7REDJCmfyUfNibGt2bL-zONDPhK_pi4gsdtoCLqeO0N7NdcmMLTtPpxdHILM1TPrknz3btv8gKTDH_30nlFpMPAZAdpKPN3rsmB8YbFB0qoC1ROjtES0IabZJyOkAAAAAZ-F-NAA"
FORCESUB = "forcesubpavo"
AUTH = 6971324624

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
