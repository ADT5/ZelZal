import sys
import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("Zelzal")

print(userbot.__copyright__)
print(f"المرخصة بموجب شروط  {userbot.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("⌭ بـدء تنزيـل زدثــون ⌭")
    zedub.loop.run_until_complete(setup_bot())
    LOGS.info("⌭ بـدء تشغيـل البـوت ⌭")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()



async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("تـم التنصـيب .. بنجـاح ✓")
    print(
        f"<b> •⎆┊زدثــون™يـوزربـوت.. 🧸♥️ </b> \n<b>•⎆┊تحيـاتي .. زلـزال الهيبـه</b>\n<b>•⎆┊قنـاة السـورس ↶. </b>\n🌐┊@ZedThon "
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return



zedub.loop.run_until_complete(startup_process())
if len(sys.argv) in {1, 3, 4}:
    try:
        zedub.run_until_disconnected()
    except ConnectionError:
        pass
else:
    zedub.disconnect()
