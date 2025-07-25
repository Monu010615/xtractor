import os

class Config(object):
    # Telegram Bot Token
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # Telegram API ID and Hash
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH")

    # Admin User IDs (space-separated string → list of ints)
    ADMIN_ID = list(map(int, os.environ.get("ADMIN_ID", "").split()))

    # MongoDB Database URL and Name
    DB_URL = os.environ.get("DB_URL")
    DB_NAME = os.environ.get("DB_NAME", "MY_BOT_DB")

    # Log and Channel IDs
    TXT_LOG = int(os.environ.get("TXT_LOG", "0"))
    AUTH_LOG = int(os.environ.get("AUTH_LOG", "0"))
    HIT_LOG = int(os.environ.get("HIT_LOG", "0"))
    DRM_DUMP = int(os.environ.get("DRM_DUMP", "0"))
    PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "0"))
    CHANNEL = int(os.environ.get("CHANNEL", "0"))

    # External URLs
    CH_URL = os.environ.get("CH_URL")
    OWNER = os.environ.get("OWNER")
    THUMB_URL = os.environ.get("THUMB_URL")
