from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5869188823").split()))
OWNER_ID = int(getenv("OWNER_ID", "5869188823")) #ur id
MONGO_URL = getenv("MONGO_URL","mongodb+srv://bssamfor4:Zaid@cluster0.wqzjo7d.mongodb.net/?retryWrites=true&w=majority") # an database 
BOT_TOKEN = getenv("BOT_TOKEN", "5835802710:AAHOTQm0afi9pGYsxbkpHTWskrJpcl5PKL8")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT") #optional
PM_LOGGER = getenv("PM_LOGGER") # l'd if uh want 
LOG_GROUP = getenv("LOG_GROUP") #id if uh want to enable tagalert
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BABiMZkAcGNIG5wQ-Y0rnWvpPbEHrgtOclcNoop2EeA710OhPBOzKslpA5s78fVbR4Swm6sDUT9U60G4DXbU3NOQO2VvO-eX-XlFCgKa0s9JiwiRhTFlfKjCH1RcVR9tcT79S5OQTE9TME86XDz9fN8sBukdoj1M5a7OPMiKxlca7E4fRnMCmv2R0m4wqnjgt6SykgdU-9AOQn6kUtcYWvLLpjY0BULJjdVWe6EdSDoMYandDPX7Oa_9K0dMX_hk7_VNwFyzV6ukMpfos_qI4vgLglNXxqpxjvRqdgtjDnyZreqJcaZLq_L0UPNfYwvCvZ7lNuAFq_zLjNGXHb9V40N-QT2RoQAAAAFd1LbXAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
