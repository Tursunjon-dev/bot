from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8505355606:AAEWnrgZDr-eSky1bsTboBltoOuTab4eg8U"     # BotFather bergan tokenni shu yerga qo'ying
ADMIN_ID = 8394905295        # Sizning Telegram ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# User -> Admin forward
@dp.message_handler()
async def forward_to_admin(msg: types.Message):
    fwd = await msg.forward(ADMIN_ID)
    dp['map'] = dp.get('map', {})
    dp['map'][fwd.message_id] = msg.from_user.id

# Admin reply -> Userga qaytadi
@dp.message_handler(chat_id=ADMIN_ID)
async def reply_from_admin(msg: types.Message):
    if msg.reply_to_message:
        orig = dp['map'].get(msg.reply_to_message.message_id)
        if orig:
            await bot.send_message(orig, msg.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

