#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29217567
API_HASH = "0cb03c3bdddb1eb6c0a84576629e2f61"
BOT_TOKEN = "6322016957:AAFuXnb1HxRa9TYwC-KQFUNVC1zEcKdrris"
SESSION = "BQDNvmIArjbkUl4CFrrsIJ1gOadMrTZ_e2b-Axd3upVW1_LiAjy7TsY441S-a8NXfo-9poI0PtQ4uMBMGEwRnE3v3CrZjDnD5EoRZ7HxrQCXzQRl3j-j-WeFPAEyDebB4dV1MPQcsP4CoUtXcyLhrKuAhnR3k6PL3vc3vJ4xy7r5aPidLrPCm2ghugyZoLiDdL5m_COgLXOL7z2KTBqUehKH97_SWjWr3JWgdVgKNWvjsFbTZT0bOi-8X_PJgvgsvXSYyoaN8iK69D--k--nypk5JHbC2jv2jSy-FoOjHli3YzKXWhZ8XeQlf2X0gS_mky3ZDl4XYznHo7lwcYcSjnBANHOy-gAAAAGQUGCtAA"
FORCESUB = "forcesubclu"
AUTH = 6716154029
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
