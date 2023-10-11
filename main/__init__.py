#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24316517
API_HASH = "ab33479d43c662f11cf9ae4b26350709"
BOT_TOKEN = "6355377964:AAHs_j4Oyrbf1qhziDOg3Nbiftpw7UxAhq8"
SESSION = "BQFzCmUAnmS3gslM32AR3NDjcUQknlsvGPwfo4pJ_tR6LqJaTiCVVVme6QXnyov5c34h65QxK3VcX1s9290WI367WIZJv6KGw_Fk4MAbIP7604Kkv428oRvQ1X7X_QByqsq3IrtOwFr79dzd_PgGN6jtnQzkk0LaqQ4DZ4oqiQKKyieKJc6fOhMv6skvsk_g0pAk82-nBSOMa-RD_K8r2o--Dez5zygsP5_YZMB4Mxa6ZyQRrSOBrYOaPw_wFIVv7SYVASfmT4JrG7j8Uf41XR3eVP9Jtqwy5WSGggyV_xHLPVW-T5KuqJHguYE2SnME_uKKKZ1y7ba6T8xphnmV5WXE8scVWAAAAAFcoFYAAA"
FORCESUB = "forsesubpavo"
AUTH = 5848978944

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
