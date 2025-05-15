from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Температура")],
        [KeyboardButton(text="Вологість")]
    ],
    resize_keyboard=True
)