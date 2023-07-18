from aiogram import types, Dispatcher
from create_bot import dp, bot
from Keyboards import kb_client
from data_base import sqlite_db



# @dp.message_handler(commands=["start", "help"])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client) #Отправляет в личку
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/Mytelegramproject1731_bot')

# @dp.message_handler(commands=["Режим_работы"])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-ЧТ с 9 до 20, Пт-Сб с 10 до 23')

# @dp.message_handler(commands=["Расположение"])
async def pizza_place_command(message: types.message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


async def pizza_buy(callback_query: types.CallbackQuery):
    await callback_query.answer()


# @dp.message_handler(commands=["Меню"])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
    dp.register_callback_query_handler(pizza_buy, lambda x: x.data and x.data.startswith('купить '))







