import asyncio
from aiogram import Router, types
from button import keyboard
from subscriber import get_message
import json

bot_router = Router()

auto_tasks = {}  # словник chat_id: task

def get_data(type):
    try:
        messages = json.loads(get_message())
        if type == "temperature":
            return messages["content"]["temp"]
        elif type == "humidity":
            return messages["content"]["hum"]
    except Exception as e:
        return str(e)

@bot_router.message()
async def handle_msg(message: types.Message):
    chat_id = message.chat.id

    if message.text == "Температура":
        await message.answer(f"Температура: {get_data('temperature')}", reply_markup=keyboard)

    elif message.text == "Вологість":
        await message.answer(f"Вологість: {get_data('humidity')}", reply_markup=keyboard)

    elif message.text == "Авто Повідомлення":
        if chat_id in auto_tasks:
            await message.answer("Авто повідомлення вже запущено", reply_markup=keyboard)
        else:
            task = asyncio.create_task(auto_send_message(chat_id, message.bot))
            auto_tasks[chat_id] = task
            await message.answer("Авто повідомлення запущено", reply_markup=keyboard)

    elif message.text == "Стоп Авто Повідомлення":
        task = auto_tasks.pop(chat_id, None)
        if task:
            task.cancel()
            await message.answer("Авто повідомлення зупинено", reply_markup=keyboard)
        else:
            await message.answer("Авто повідомлення не було запущено", reply_markup=keyboard)

    else:
        await message.answer("Натисни кнопку 👇", reply_markup=keyboard)

async def auto_send_message(chat_id: int, bot):
    try:
        while True:
            temp = get_data("temperature")
            hum = get_data("humidity")
            await bot.send_message(chat_id, f"Авто повідомлення:\nТемпература: {temp}\nВологість: {hum}", reply_markup=keyboard)
            await asyncio.sleep(10)
    except asyncio.CancelledError:
        pass
