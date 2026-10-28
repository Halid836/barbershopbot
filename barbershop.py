import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

# Токен бота
Token = ""

admin_id =  #тут свой TGID
bot= Bot(Token)
dp = Dispatcher()


# Функции бота
@dp.message(Command("start"))
async def start(message: Message):
    # Кнопки для бота
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Записаться", callback_data="signup")]
        ]
    )
    # Сообщение для пользователя
    await message.answer(
        f"Здравствуйте {message.from_user.first_name}, это Официальный бот для записи в парикмахерскую",
        reply_markup=inl_kb
    )


# Callback-нажатие для кнопки записаться
@dp.callback_query(F.data == "signup")
async def signup(callback: CallbackQuery):
    # Кнопки с временем
    time_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="11:00", callback_data="time11")],
            [InlineKeyboardButton(text="12:00", callback_data="time12")],
        ]
    )

    # сообщение при нажатии кнопки записаться
    await callback.message.answer("Выберите время:", reply_markup=time_btn)


# Ответ при нажатии кнопки 11:00
@dp.callback_query(F.data == "time11")
async def time11(callback: CallbackQuery):
    await callback.message.answer("Вы записаны")
    await bot.send_message(
        admin_id,
        text=f"{callback.from_user.first_name}, записан в 11:00"
    )


# Ответ при нажатии кнопки 12:00
@dp.callback_query(F.data == "time12")
async def time12(callback: CallbackQuery):
    await callback.message.answer("Вы записаны")
    await bot.send_message(
        admin_id,
        text=f"{callback.from_user.first_name}, записан в 12:00"
    )


# поллинг
async def main():
    print("Bot starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
