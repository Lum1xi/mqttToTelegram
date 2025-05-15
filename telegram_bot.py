import json

from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyexpat.errors import messages

from button import keyboard
from subscriber import get_message
bot_router = Router()

def get_data(type):
    try:
        messages = json.loads(get_message())
        if type == "temperature":
            return messages["content"]["temp"]
        elif type == "humidity":
            return messages["content"]["hum"]

    except Exception as e:
        return e

@bot_router.message()
async def handle_msg(message: types.Message):

    if message.text == "Температура":
        await message.answer(f"Температура: {get_data("temperature")}", reply_markup=keyboard)
    elif message.text == "Вологість":
        await message.answer(f"Вологість: {get_data("humidity")}", reply_markup=keyboard)
    else:
        await message.answer("Натисни кнопку 👇", reply_markup=keyboard)
