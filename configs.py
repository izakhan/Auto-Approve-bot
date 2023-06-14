from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "7839182"))
    API_HASH = getenv("API_HASH", "c4787b79c1bc855dbcb6d7f84be81883")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1001885243855"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://channel:channel1234@cluster0.qffsd2a.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
