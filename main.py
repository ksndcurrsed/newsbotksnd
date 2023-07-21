import aiogram, time, sys
global chatt_id
from scripts import *
from config import *


print(str(dt.hour) + ':' + str(dt.minute))


bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: aiogram.types.Message):
    await message.reply('Привет, я новостной бот Ksndcursed в сфере IT')

@dp.message_handler(commands=['news'])
async def minut(message: aiogram.types.Message):
    await message.reply(newss(0))
    print(message.chat.id)

@dp.message_handler(commands=['best'])
async def minut(message: aiogram.types.Message):
    await message.reply(bestnews(0))

@dp.message_handler()
async def nov(msg:aiogram.types.Message):
    await bot.send_message(adm_id, "Итак, новости на " + str(dt.hour) + ":" + str(dt.minute) + '\n' + '\n' + newss(0))

for i in range(300):
    time.sleep(1)
    cnt += 1
    print(cnt)
    if cnt == 300:
        sys.exit(0)

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, on_startup=nov)




