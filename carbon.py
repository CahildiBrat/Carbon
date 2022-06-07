#Bu kod Repohane ve MultiAzBot a aittir.
#Kodu öz adına çıxaran Bizə ata desin :)
# T.me/MultiAzOfficial ve T.me/Repohane


from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, idle, filters
from io import BytesIO
from aiohttp import ClientSession
#--------------------------------------------------------------
API_ID = xxxxxxx
API_HASH = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
BOT_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#--------------------------------------------------------------

rphn = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

aiohttpsession = ClientSession()


async def get_http_status_code(url: str) -> int:
    async with aiohttpsession.head(url) as resp:
        return resp.status
    

async def make_carbon(code):
    url = "https://carbonara.vercel.rphn/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@rphn.on_message(filters.command("carbon"))
async def carbon_func(bot: rphn, msg: Message):
    m = await msg.reply_text("`Hazırlanır`")
    carbon = await make_carbon(msg.reply_to_message.text)
    await m.edit("`Göndərilir`")
    await bot.send_photo(msg.chat.id, photo=carbon)
    await m.delete()
    carbon.close()

rphn.start()
print("Bot başladı!")
idle()
