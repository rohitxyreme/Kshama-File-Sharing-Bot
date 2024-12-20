import os
import logging
from logging.handlers import RotatingFileHandler

# Bot tokens and API configuration
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Owner and database configuration
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "maaljaal")

# Channel and subscription configuration
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
FORCE_SUB_CHANNELS = [int(x) for x in os.environ.get("FORCE_SUB_CHANNELS", "").split()]  # Environment variable setup

# Other configurations
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600"))  # auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Admin setup
try:
    ADMINS = [1720931455]  # Default admin(s)
    for x in os.environ.get("ADMINS", "").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)  # Add owner to admins

# Customizable bot messages and settings
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False
BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"
START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")

# Logging setup
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
