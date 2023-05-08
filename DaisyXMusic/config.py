from os import getenv

que = {}
SESSION_NAME = getenv("BQAOyJeHvMbg5tjuXkbUkDsYZCOnj8q9uyBkjA88f0XUp6s8VncoTW8wC0AsNpG1tzRK7YFB8q5tLaD4GljF0f_xz-woncfUpjv15p6g99q8bRA6rLB4BqK_ISyMOW37MhtBPLSIciZ1TGkze5NgpqPH8EoEFr566b0dZLCusz8Mx_vaMzXw8KHS4NFeKYzXSH6ywCiyFAKhbi4EfY6LiusTsfTwcvP_Ob7g0kxrpkuCLLE7B8M92sbqZmaGBQ6E1RCem0H5viozEKyUsf3u_o3HQX_dt9ElvYN7No6ia9H57cm1RwDztyHODUvDlEN6Dpc3hNYNpbc7wmgOuijCu3DlAAAAATslPdEA", "session")
BOT_TOKEN = getenv("6192180909:AAFD3RuFOOBv3lOTswHQwWGHkViLilusmKE")
BOT_NAME = getenv("Uta")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RealmBotUpdates")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/2941b97ce13e2347bac8f.jpg")
admins = {}
API_ID = int(getenv("API_ID", "26019444"))
API_HASH = getenv("a308fac723905cdbd836414b18f3b3d6")
BOT_USERNAME = getenv("UtaXDivaMusicBot")
ASSISTANT_NAME = getenv("ASSIS", "UtaMusicAssistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "RealmBotSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "Uta")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("5860097723 5925926828 6046532356").split()))
