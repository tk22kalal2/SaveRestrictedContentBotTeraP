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
SESSION = "BQFzCmUALtmhtjC1VDgfgRbQ8qkeKaUGopw4FtCxnz9QX7i1go2t1N54kTGXF2tT-jHFp81E4iFJz9H5U-Ght3HNqC5-Ut25w88ufY1yxrab8tJdpc0rpB2NUH0IMTU59Pfe5tERCj2NtHfe4u2I4GMYhNNxouFfE1pbAuj9Fr_oD7Y61sffoASO1nZgI7Cnpjmdpw-76LS4lVcvF7iZG4KUi4V90EI8e63dSBcYQvuWJhnrM1RI5LHyIWShpi88O14obKnwgjWpU9i4CWW8HgXE9OgqQAnWTj7e87JbPzO5WQE62VipWz5fkwNaLWa2Zsv7sahYyjI9PTh5WxvJuWtQ0tMfJQAAAAFcoFYAAA"
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
