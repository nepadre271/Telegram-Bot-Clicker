import asyncio  
import logging  
import sys  
import os 
from dotenv import load_dotenv 
 
from aiogram import Bot, Dispatcher, html, types 
from aiogram.client.default import DefaultBotProperties  
from aiogram.enums import ParseMode  
from aiogram.filters import CommandStart  
from aiogram.types import Message, CallbackQuery 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
 
load_dotenv() 
TOKEN = os.getenv("TELEGRAM_TOKEN") 
 
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  
dp = Dispatcher() 
dp.bot = bot     
 
@dp.message()  
async def echo_handler(message: Message) -> None: 
    text = "<b>Привет! Добро пожаловать в Кликер Хомяка 🐹</b>\n"\
           "\nОтныне ты — директор криптобиржи.\n"\
           "\nКакой? <i>Выбирай сам</i>. Тапай по экрану, собирай монеты, качай пассивный доход, разрабатывай собственную стратегию дохода.\n"\
           "\nМы в свою очередь оценим это во время выдачи бесплатных подписок на приватную группу, даты которой ты узнаешь совсем скоро.\n"\
           "\n<b>Про друзей не забывай</b> — зови их в игру и получайте вместе ещё больше монет!" 
 
    keyboard = InlineKeyboardMarkup(inline_keyboard=[ 
        [InlineKeyboardButton(text="Играть сейчас", url="https://t.me/")], 
        [InlineKeyboardButton(text="Как играть", callback_data='how_to_play')], 
        [InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/")] 
    ]) 
    await message.answer( 
        text = text, 
        parse_mode="html", 
        disable_web_page_preview=True, 
        reply_markup=keyboard 
    ) 
     
@dp.callback_query(lambda c: c.data == 'how_to_play') 
async def process_callback_button1(callback_query: CallbackQuery): 
    await bot.answer_callback_query(callback_query.id) 

    help_text = ""

    await bot.send_message(callback_query.from_user.id, help_text) 
     
async def main() -> None:   
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  
  
    await dp.start_polling(bot)  
  
if __name__ == "__main__":  
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)  
    asyncio.run(main())