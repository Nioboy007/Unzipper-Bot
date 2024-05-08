#Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("APP_ID", "10471716"))
    API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1002048766471"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6883997969"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN", "EThzPCbiFHqZJ2iaHxykeGa4YIKhFquf")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
