import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20053544")

API_HASH = os.environ.get("API_HASH", "f26c4d28081c11e0c48707143f7bb5b1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6614517373:AAHcoPA3v3dULv72p88vND8hva0ptuWK53g") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001688675040") 

DB_NAME = os.environ.get("DB_NAME","Cluste0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://MovieTimeHD1:MovieTimeHD1@cluster0.trfqzij.mongodb.net/ ")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/52807f093e8b1f225a37a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
