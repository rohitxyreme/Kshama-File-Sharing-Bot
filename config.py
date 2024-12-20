import os
import logging
from logging.handlers import RotatingFileHandler

# Sensitive tokens fetched from environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # Bot token from BotFather
API_ID = int(os.environ.get("API_ID", ""))  # Telegram API ID
API_HASH = os.environ.get("API_HASH", "")  # Telegram API hash
OWNER_ID = int(os.environ.get("OWNER_ID", ""))  # Telegram user ID of the bot owner
DB_URL = os.environ.get("DB_URL", "")  # Database connection URL
DB_NAME = os.environ.get("DB_NAME", "maaljaal")  # Optional: Default DB name

# Non-sensitive variables (can be hardcoded)
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002444409596"))  # Channel ID for bot operations
FORCE_SUB_CHANNELS = [
    -1001234567890,  # Replace with your first channel ID
    -1009876543210,  # Replace with your second channel ID
    -1001112131415,  # Add more as needed
]
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600"))  # Auto-delete files in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Admin setup
try:
    ADMINS = [1720931455]  # Add default admin(s)
    for x in os.environ.get("ADMINS", "").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)  # Add owner to admins

# Optional features
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False").lower() == "true"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True").lower() == "true"

# Default messages
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.",
)
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>",
)
USER_REPLY_TEXT = "❌ Don't Send Me Messages Directly; I'm Only a File Share Bot!"

# Logging setup
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"
