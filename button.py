from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Температура")],
        [KeyboardButton(text="Вологість")],
        [KeyboardButton(text="Авто Повідомлення")],
        [KeyboardButton(text="Стоп Авто Повідомлення")],
    ],
    resize_keyboard=True
)