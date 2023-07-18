import sqlite3 as sql
from create_bot import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def sql_start():
    global db, cur
    db = sql.connect('pizza.db')
    cur = db.cursor()
    if db:
        print('DB connected OK')
    db.execute('CREATE TABLE IF NOT EXISTS menu('
               'img TEXT,'
               'name TEXT PRIMARY KEY,'
               'description TEXT,'
               'price TEXT)'
               )
    db.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        db.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]} ₽', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Купить {ret[1]}', callback_data=f'купить {ret[1]}')))



async def sql_read2():
    return cur.execute("SELECT * FROM menu").fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    db.commit()
