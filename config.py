import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6774687158:AAEDn31cTpjFmvHzooHGeQKP16HLfrh3Qyc")
      API_ID = int(os.environ.get("APP_ID", "27413186"))
      API_HASH = os.environ.get("API_HASH", "f048e304046953301390f710cd091350")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Ivansh22")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", "6874386860" )) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://shubhsharma2253:FTWATOI3mt8haSUp@cluster0.zncuwxt.mongodb.net/?retryWrites=true&w=majority")
