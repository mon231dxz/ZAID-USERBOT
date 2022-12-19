from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5610994282").split()))
OWNER_ID = int(getenv("OWNER_ID", "5610994282")) #ur id
MONGO_URL = getenv("MONGO_URL","mongodb+srv://bssamfor4:Zaid@cluster0.wqzjo7d.mongodb.net/?retryWrites=true&w=majority") # an database 
BOT_TOKEN = getenv("BOT_TOKEN", "5971864806:AAGdFg8s_gEULjFOFk0M626kyto9QItJAto")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # l'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want to enable tagalert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BABiMZkAk82dAm2xcffNjBF9lf7SrebT6XW97UzHWRqmx8x3uu_c5msyLHqcBD7aTZrJ7GLTr_MSvsyEON8gCeabUbLNZyNp8Q0uBW69tcubwiOryLNRdCXnwR2AVew9yymZf6PdlOTpZm-zCTF6YsfVTzWuSuhTRLCUbBeywZfK2vmDhgVYQsByMxJ_AsDH6fQd5oM7X1P150hdIRyZ2j0MCuwHqDoFnxBgZqYb0Jej0lBprqMth3TIsFquYhHcVh2IyTaxWMA5f7OIX5l8y6Qo_Er1tyVFNIhtCes1WLOnF9sAKpTDKneyBVKro4kBUimq2EoBalJnro_q6JcJZWlPkrsZSAAAAAFOcPpqAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
