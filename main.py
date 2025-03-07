import asyncio
import sqlite3
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
#from aiogram.dispatcher import FSMContext
#from aiogram.fsm.storage.memory import MemoryStorage  # Новый импорт хранилища FSM
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import time
import os
import re
import random

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

TOKEN = "8175894906:AAGnmTKH20bFDYDBjRauzYj1zQndS1c2L_c"

dp = Dispatcher()


chat_id = '532705230'
ADMIN_ID = 532705230
stat_id = '7688360686'
tyom_stat_id = '1797123496'
tyom_ADMIN_ID = 1797123496

users_requests = {}  # Хранение активных запросов пользователей

price = cg.get_price(ids='tether, bitcoin, ethereum, litecoin, dogecoin, official-trump, ripple, solana, notcoin, binarydao, cardano, tron, the-open-network, avalanche-2, sui, chainlink, aptos, stellar, mantra-dao, hedera-hashgraph, polkadot, hyperliquid, uniswap, monero', vs_currencies='rub') #, based-pepe, , shiba-inu
balance = 0
count = 0

class UserState(StatesGroup):
    next_message5 = State()
    next_message6 = State()
    next_message7 = State()
    next_message8 = State()
    next_message9 = State()
    next_message10 = State()
    next_message11 = State()
    next_message12 = State()
    next_message13 = State()
    next_message27 = State()
    next_message28 = State()
    next_message29 = State()
    next_message30 = State()
    next_message31 = State()
    next_message32 = State()
    next_message33 = State()
    next_message34 = State()
    next_message35 = State()
    next_message36 = State()
    next_message37 = State()
    next_message38 = State()
    next_message39 = State()
    next_message40 = State()
    next_message41 = State()
    vivod = State()

# Класс состояний (оставляем на будущее, но используем только один раз)
class OrderState(StatesGroup):
    processing_order = State()

class MyClass:
    def __init__(self):
        # Инициализация переменной класса
        self.my_variable = None
        self.nx5 = False
        self.nx6 = False
        self.nx7 = False
        self.nx8 = False
        self.nx9 = False
        self.nx10 = False
        self.nx11 = False
        self.nx12 = False
        self.nx13 = False
        self.nx27 = False
        self.nx28 = False
        self.nx29 = False
        self.nx30 = False
        self.nx31 = False
        self.nx32 = False
        self.nx33 = False
        self.nx34 = False
        self.nx35 = False
        self.nx36 = False
        self.nx37 = False
        self.nx38 = False
        self.nx39 = False
        self.nx40 = False
        self.nx41 = False

    def set_variable(self, value):
        # Функция для установки значения переменной
        self.my_variable = value
        print(f"Значение переменной установлено: {self.my_variable}")

    def use_variable(self):
        # Функция для использования значения переменной
        print(f"Используем значение переменной: {self.my_variable}")
        return self.my_variable
    def delete_variable(self):
        self.my_variable = None

my_object = MyClass()

menu1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Актуальные курсы криптовалют 💹', callback_data='1')],
    [InlineKeyboardButton(text='Купить криптовалюту 💸', callback_data='2')],
    [InlineKeyboardButton(text='Баланс кошелька 💰', callback_data='3')]
])

menu2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться в главное меню ⬅', callback_data='4')]
])

menu3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='tether (USDT)', callback_data='5')],
    [InlineKeyboardButton(text='bitcoin (BTC)', callback_data='6')],
    [InlineKeyboardButton(text='ethereum (ETH)', callback_data='7')],
    [InlineKeyboardButton(text='litecoin (LTC)', callback_data='8')],
    [InlineKeyboardButton(text='dogecoin (DOGE)', callback_data='9')],
    [InlineKeyboardButton(text='official trump (TRUMP)', callback_data='10')],
    [InlineKeyboardButton(text='ripple (XRP)', callback_data='11')],
    [InlineKeyboardButton(text='solana (SOL)', callback_data='12')],
    [InlineKeyboardButton(text='notcoin (NOT)', callback_data='13')],
    [InlineKeyboardButton(text='binarydao (BYTE)', callback_data='27')],
    [InlineKeyboardButton(text='cardano (ADA)', callback_data='28')],
    [InlineKeyboardButton(text='tron (TRX)', callback_data='29')],
    [InlineKeyboardButton(text='вперед ⏩', callback_data='25')],
    [InlineKeyboardButton(text='Вернуться в главное меню ⬅', callback_data='4')]
])

menu4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оформить заказ', callback_data='14')]
])

menu5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вывести средства', callback_data='15')],
    [InlineKeyboardButton(text='Вернуться в главное меню ⬅', callback_data='4')]
])

menu6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='tether (USDT)', callback_data='16')],
    [InlineKeyboardButton(text='bitcoin (BTC)', callback_data='17')],
    [InlineKeyboardButton(text='ethereum (ETH)', callback_data='18')],
    [InlineKeyboardButton(text='litecoin (LTC)', callback_data='19')],
    [InlineKeyboardButton(text='doge (DOGE)', callback_data='20')],
    [InlineKeyboardButton(text='official trump (TRUMP)', callback_data='21')],
    [InlineKeyboardButton(text='ripple (XRP)', callback_data='22')],
    [InlineKeyboardButton(text='solana (SOL)', callback_data='23')],
    [InlineKeyboardButton(text='notcoin (NOT)', callback_data='24')],
    [InlineKeyboardButton(text='binarydao (BYTE)', callback_data='42')],
    [InlineKeyboardButton(text='cardano (ADA)', callback_data='43')],
    [InlineKeyboardButton(text='tron (TRX)', callback_data='44')],
    [InlineKeyboardButton(text='toncoin (TON)', callback_data='45')],
    [InlineKeyboardButton(text='avalanche (AVAX)', callback_data='46')],
    [InlineKeyboardButton(text='sui (SUI)', callback_data='47')],
    [InlineKeyboardButton(text='chainlink (LINK)', callback_data='48')],
    [InlineKeyboardButton(text='aptos (APT)', callback_data='49')],
    [InlineKeyboardButton(text='stellar (XLM)', callback_data='50')],
    [InlineKeyboardButton(text='mantra (OM)', callback_data='51')],
    [InlineKeyboardButton(text='hedera (HBAR)', callback_data='52')],
    [InlineKeyboardButton(text='polkadot (DOT)', callback_data='53')],
    [InlineKeyboardButton(text='hyperliquid (HYPE)', callback_data='54')],
    [InlineKeyboardButton(text='uniswap (UNI)', callback_data='55')],
    [InlineKeyboardButton(text='monero (XMR)', callback_data='56')],
    [InlineKeyboardButton(text = 'Вернуться в главное меню ⬅', callback_data='4')]
])

menu7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='toncoin (TON)', callback_data='30')],
    [InlineKeyboardButton(text='avalanche (AVAX)', callback_data='31')],
    [InlineKeyboardButton(text='sui (SUI)', callback_data='32')],
    [InlineKeyboardButton(text='chainlink (LINK)', callback_data='33')],
    [InlineKeyboardButton(text='aptos (APT)', callback_data='34')],
    [InlineKeyboardButton(text='stellar (XLM)', callback_data='35')],
    [InlineKeyboardButton(text='mantra (OM)', callback_data='36')],
    [InlineKeyboardButton(text='hedera (HBAR)', callback_data='37')],
    [InlineKeyboardButton(text='polkadot (DOT)', callback_data='38')],
    [InlineKeyboardButton(text='hyperliquid (HYPE)', callback_data='39')],
    [InlineKeyboardButton(text='uniswap (UNI)', callback_data='40')],
    [InlineKeyboardButton(text='monero (XMR)', callback_data='41')],
    [InlineKeyboardButton(text='⏪ назад', callback_data='26')],
    [InlineKeyboardButton(text='Вернуться в главное меню ⬅', callback_data='4')]
])

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
#dp = Dispatcher()
# Определяем состояния


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    file_bal = open(f'/root/bot/bal/{[message.chat.id]}.txt', "w", encoding="utf-8")
    file_bal.write(
        f'Tether (USDT) == {0.0} руб \n'
        f'Bitcoin (BTC) == {0.0} руб \n'
        f'Ethereum (ETH) == {0.0} руб \n'
        f'Litecoin (LTC) == {0.0} руб \n'
        f'Dogecoin (DOGE) == {0.0} руб \n'
        f'Official Trump (TRUMP) == {0.0} руб \n'
        f'Ripple (XRP) == {0.0} руб \n'
        f'Solana (SOL) == {0.0} руб \n'
        f'Notcoin (NOT) == {0.0} руб \n'
        f'Binarydao (BYTE) == {0.0} руб \n'
        f'Cardano (ADA) == {0.0} руб \n'
        f'Tron (TRX) == {0.0} руб \n'
        f'Toncoin (TON) == {0.0} руб \n'
        f'Avalanche (AVAX) == {0.0} руб \n'
        f'Sui (SUI) == {0.0} руб \n'
        f'Chainlink (LINK) == {0.0} руб \n'
        f'Aptos (APT) == {0.0} руб \n'
        f'Stellar (XLM) == {0.0} руб \n'
        f'Mantra (OM) == {0.0} руб \n'
        f'Hedera (HBAR) == {0.0} руб \n'
        f'Polkadot (DOT) == {0.0} руб \n'
        f'Hyperliquid (HYPE) == {0.0} руб \n'
        f'Uniswap (UNI) == {0.0} руб \n'
        f'Monero (XMR) == {0.0} руб \n'
    )
    file_bal.close()
    await bot.send_message(stat_id,
                           f"🚀 Новый START от {message.from_user.full_name} (ID: {message.chat.id}) \n"
                           )
    await bot.send_message(tyom_stat_id,
                           f"🚀 Новый START от {message.from_user.full_name} (ID: {message.chat.id}) \n"
                           )
    ##conn = sqlite3.connect('dbcrypto.sql')
    ##cur = conn.cursor()
    ##cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, summa varchar(50))')
    ##conn.commit()
    ##cur.close()
    ##conn.close()
    #await message.delete()
    await message.answer('Привет, {0.first_name}!\n'
                                      '\n'
                                      '🌐💱 Добро пожаловать в криптобот! \n'
                                      '\n'
                                      '\n'
                                      'Здесь вы можете ознакомиться с актуальными курсами 📈🔥 \n'
                                      '\n'
                                      'а также приобрести криптотокены по низкому курсу 💰💎 \n'
                                      '\n'
                                      '\n'.format(message.from_user), reply_markup=menu1)


@dp.callback_query()
async def callback(call: types.CallbackQuery, state: FSMContext):
    if call.message:
        if call.data == '1':
            await call.message.delete()
            await call.message.answer(
                f'Tether (USDT) == {round(0.92 * price["tether"]["rub"], 2)} руб \n'
                                                        f'Bitcoin (BTC) == {round(0.98 * price["bitcoin"]["rub"], 2)} руб \n'
                                                        f'Ethereum (ETH) == {round(0.98 * price["ethereum"]["rub"], 2)} руб \n'
                                                        f'Litecoin (LTC) == {round(0.98 * price["litecoin"]["rub"], 2)} руб \n'
                                                        f'Dogecoin (DOGE) == {round(0.98 * price["dogecoin"]["rub"], 2)} руб \n'
                                                        f'Official Trump (TRUMP) == {round(0.98 * price["official-trump"]["rub"], 2)} руб \n'
                                                        f'Ripple (XRP) == {round(0.98 * price["ripple"]["rub"], 2)} руб \n'
                                                        f'Solana (SOL) == {round(0.98 * price["solana"]["rub"], 2)} руб \n'
                                                        f'Notcoin (NOT) == {round(0.98 * price["notcoin"]["rub"], 2)} руб \n'
                                                        f'Binarydao (BYTE) == {round(0.98 * price["binarydao"]["rub"], 2)} руб \n'
                                                        f'Cardano (ADA) == {round(0.98 * price["cardano"]["rub"], 2)} руб \n'
                                                        f'Tron (TRX) == {round(0.98 * price["tron"]["rub"], 2)} руб \n'
                                                        f'Toncoin (TON) == {round(0.98 * price["the-open-network"]["rub"], 2)} руб \n'
                                                        f'Avalanche (AVAX) == {round(0.98 * price["avalanche-2"]["rub"], 2)} руб \n'
                                                        f'Sui (SUI) == {round(0.98 * price["sui"]["rub"], 2)} руб \n'
                                                        f'Chainlink (LINK) == {round(0.98 * price["chainlink"]["rub"], 2)} руб \n'
                                                        f'Aptos (APT) == {round(0.98 * price["aptos"]["rub"], 2)} руб \n'
                                                        f'Stellar (XLM) == {round(0.98 * price["stellar"]["rub"], 2)} руб \n'
                                                        #f'Shiba Inu (SHIB) == {round(0.98 * price["shiba-inu"]["rub"], 2)} руб \n'
                                                        f'Mantra (OM) == {round(0.98 * price["mantra-dao"]["rub"], 2)} руб \n'
                                                        f'Hedera (HBAR) == {round(0.98 * price["hedera-hashgraph"]["rub"], 2)} руб \n'
                                                        f'Polkadot (DOT) == {round(0.98 * price["polkadot"]["rub"], 2)} руб \n'
                                                        f'Hyperliquid (HYPE) == {round(0.98 * price["hyperliquid"]["rub"], 2)} руб \n'
                                                        #f'Pepe (PEPE) == {round(0.98 * price["based-pepe"]["rub"], 2)} руб \n'
                                                        f'Uniswap (UNI) == {round(0.98 * price["uniswap"]["rub"], 2)} руб \n'
                                                        f'Monero (XMR) == {round(0.98 * price["monero"]["rub"], 2)} руб \n', reply_markup=menu2)
        elif call.data == '2':
            await call.message.delete()
            await call.message.answer('Выберите криптовалюту, которую хотите купить: \n', reply_markup=menu3)
        elif call.data == '3':
            await call.message.delete()
            await call.message.answer('Баланс вашего кошелька: \n', reply_markup=menu5)
            file_bal = open(f'/root/bot/bal/{[call.message.chat.id]}.txt', "r", encoding="utf-8")
            content_bal = file_bal.read()
            file_bal.close()
            await call.message.answer(content_bal, parse_mode='Markdown')
        elif call.data == '4':
            await call.message.delete()
            await call.message.answer('Привет, {0.first_name}!\n'
                                                  '\n'
                                                  '🌐💱 Добро пожаловать в криптобот! \n'
                                                  '\n'
                                                  '\n'
                                                  'Здесь вы можете ознакомиться с актуальными курсами 📈🔥 \n'
                                                  '\n'
                                                  'а также приобрести криптотокены по низкому курсу 💰💎 \n'
                                                  '\n'
                                                  '\n'.format(call.message.from_user), reply_markup=menu1)
        elif call.data == '5':
            await call.message.delete()
            await call.message.answer('Напишите количество usdt, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message5)  # Устанавливаем состояние
        elif call.data == '6':
            await call.message.delete()
            await call.message.answer('Напишите количество btc, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message6)  # Устанавливаем состояние
        elif call.data == '7':
            await call.message.delete()
            await call.message.answer('Напишите количество eth, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message7)
        elif call.data == '8':
            await call.message.delete()
            await call.message.answer('Напишите количество ltc, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message8)
        elif call.data == '9':
            await call.message.delete()
            await call.message.answer('Напишите количество doge, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message9)
        elif call.data == '10':
            await call.message.delete()
            await call.message.answer('Напишите количество trump, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message10)
        elif call.data == '11':
            await call.message.delete()
            await call.message.answer('Напишите количество xrp, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message11)
        elif call.data == '12':
            await call.message.delete()
            await call.message.answer('Напишите количество sol, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message12)
        elif call.data == '13':
            await call.message.delete()
            await call.message.answer('Напишите количество not, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message13)
        elif call.data == '27':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество byte, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message27)
        elif call.data == '28':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество ada, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message28)
        elif call.data == '29':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество trx, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message29)
        elif call.data == '30':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество ton, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message30)
        elif call.data == '31':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество avax, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message31)
        elif call.data == '32':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество sui, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message32)
        elif call.data == '33':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество link, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message33)
        elif call.data == '34':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество apt, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message34)
        elif call.data == '35':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество xlm, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message35)
        elif call.data == '36':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество om, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message36)
        elif call.data == '37':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество hbar, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message37)
        elif call.data == '38':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество dot, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message38)
        elif call.data == '39':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество hype, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message39)
        elif call.data == '40':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество uni, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message40)
        elif call.data == '41':
            await call.message.delete()
            await call.message.answer(
                'Напишите количество xmr, которое хотите купить: \n'.format(call.message.from_user), reply_markup=menu2)
            await state.set_state(UserState.next_message41)
        elif call.data == '25':
            await call.message.delete()
            await call.message.answer('Выберите криптовалюту, которую хотите купить: \n', reply_markup=menu7)
        elif call.data == '26':
            await call.message.delete()
            await call.message.answer('Выберите криптовалюту, которую хотите купить: \n', reply_markup=menu3)
        elif call.data == '14':
            await call.message.delete()
            ##conn = sqlite3.connect('dbcrypto.sql')
            ##cur = conn.cursor()
            user_id = [call.message.chat.id]
            chat = await bot.get_chat(chat_id=call.message.chat.id)
            username = chat.username
            user_id2 = call.from_user.id
            users_requests[user_id2] = call.from_user.full_name
            # Используем state.update_data(), чтобы записывать данные для конкретного пользователя
            await state.update_data(order=f"Заказ пользователя {user_id2}")
            # Чтение данных
            data = await state.get_data()
            print(f"[DEBUG] User {user_id2} - {data}")
            ##await call.message.answer("Данные сохранены!")
            summa = None
            if my_object.nx5:
                summa = str(round(0.92 * my_object.use_variable() * price["tether"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: USDT \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: USDT \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx5 = False
            if my_object.nx6:
                summa = str(round(0.98 * my_object.use_variable() * price["bitcoin"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: BTC \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: BTC \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx6 = False
            if my_object.nx7:
                summa = str(round(0.98 * my_object.use_variable() * price["ethereum"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: ETC \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: ETC \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx7 = False
            if my_object.nx8:
                summa = str(round(0.98 * my_object.use_variable() * price["litecoin"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: LTC \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: LTC \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx8 = False
            if my_object.nx9:
                summa = str(round(0.98 * my_object.use_variable() * price["dogecoin"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: DOGE \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: DOGE \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx9 = False
            if my_object.nx10:
                summa = str(round(0.98 * my_object.use_variable() * price["official-trump"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: TRUMP \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: TRUMP \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx10 = False
            if my_object.nx11:
                summa = str(round(0.98 * my_object.use_variable() * price["ripple"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: XRP \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: XRP \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx11 = False
            if my_object.nx12:
                summa = str(round(0.98 * my_object.use_variable() * price["solana"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: SOL \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: SOL \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx12 = False
            if my_object.nx13:
                summa = str(round(0.98 * my_object.use_variable() * price["notcoin"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: NOT \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: NOT \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx13 = False
            if my_object.nx27:
                summa = str(round(0.92 * my_object.use_variable() * price["binarydao"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: BYTE \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: BYTE \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx27 = False
            if my_object.nx28:
                summa = str(round(0.92 * my_object.use_variable() * price["cardano"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: ADA \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: ADA \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx28 = False
            if my_object.nx29:
                summa = str(round(0.92 * my_object.use_variable() * price["tron"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: TRX \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: TRX \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx29 = False
            if my_object.nx30:
                summa = str(round(0.92 * my_object.use_variable() * price["the-open-network"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: TON \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: TON \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx30 = False
            if my_object.nx31:
                summa = str(round(0.92 * my_object.use_variable() * price["avalanche-2"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: AVAX \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: AVAX \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx31 = False
            if my_object.nx32:
                summa = str(round(0.92 * my_object.use_variable() * price["sui"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: SUI \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: SUI \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx32 = False
            if my_object.nx33:
                summa = str(round(0.92 * my_object.use_variable() * price["chainlink"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: LINK \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: LINK \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx33 = False
            if my_object.nx34:
                summa = str(round(0.92 * my_object.use_variable() * price["aptos"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: APT \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: APT \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx34 = False
            if my_object.nx35:
                summa = str(round(0.92 * my_object.use_variable() * price["stellar"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: XLM \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: XLM \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx35 = False
            if my_object.nx36:
                summa = str(round(0.92 * my_object.use_variable() * price["mantra-dao"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: OM \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: OM \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx36 = False
            if my_object.nx37:
                summa = str(round(0.92 * my_object.use_variable() * price["hedera-hashgraph"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: HBAR \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: HBAR \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx37 = False
            if my_object.nx38:
                summa = str(round(0.92 * my_object.use_variable() * price["polkadot"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: DOT \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: DOT \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx38 = False
            if my_object.nx39:
                summa = str(round(0.92 * my_object.use_variable() * price["hyperliquid"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: HYPE \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: HYPE \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx39 = False
            if my_object.nx40:
                summa = str(round(0.92 * my_object.use_variable() * price["uniswap"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: UNI \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: UNI \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx40 = False
            if my_object.nx41:
                summa = str(round(0.92 * my_object.use_variable() * price["monero"]["rub"], 2))
                await bot.send_message(ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: XMR \n"
                                       f"На сумму: {summa} \n"
                                       )
                await bot.send_message(tyom_ADMIN_ID,
                                       f"📩 Новый запрос от {call.from_user.full_name} (ID: {user_id2}) \n"
                                       f"Пользователь: {user_id} @{username} \n"
                                       f"Хочет купить: XMR \n"
                                       f"На сумму: {summa} \n"
                                       )
                my_object.nx41 = False
            # user_id = [call.message.chat.id]
            data2 = (f'{user_id}', f'{summa}')
            ##cur.execute(f'REPLACE INTO users (id, summa) VALUES {data2};')
            ##conn.commit()
            ##cur.close()
            ##conn.close()
            # Извлекаем данные из FSM и проверяем, что они сохраняются корректно
            user_data = await state.get_data()
            order_details = user_data.get("order", "Ошибка записи заказа!")
            random_number = random.randint(100000, 999999)  # Генерируем шестизначное число
            # Сообщаем пользователю, что заказ оформлен
            ##await call.message.answer(f"✅ Ваш заказ успешно оформлен!\n{order_details}")
            await call.message.answer(f"✅ Ваша заявка №{random_number} на покупку криптовалюты успешно оформлена! \n"
                                      f"\n"
                                      f"В течение нескольких минут отправим вам реквизиты \n"
                                      f"Необходимо произвести оплату и прислать чек в формате ПДФ \n"
                                      f"\n"
                                      f"\n"
                                      f"❗ ВНИМАНИЕ ❗ \n"
                                      f"\n"
                                      f"Без чека криптовалюта не поступит на ваш баланс".format(call.message.from_user))
            # Сбрасываем состояние
            ##await state.set_state(OrderState.waiting_for_something)
            await state.clear()
            ##await call.answer()
            #file = open(f'/root/bot/rek/{user_id}.txt', "w", encoding="utf-8")
            #file.write(f'РЕКВИЗИТЫ ДЛЯ ПЕРЕВОДА \n\nна сумму {summa} руб \n\n\n')
            #file = open(f'/root/bot/rek/{user_id}.txt', "r", encoding="utf-8")
            #time.sleep(330)
            #content = file.read()
            #print(content)
            #file.close()
            #await call.message.answer(content)
            #await call.message.answer("✅ Ваш запрос отправлен админу.")
        elif call.data == '15':
            await call.message.delete()
            await call.message.answer('Выберите криптовалюту, которую хотите вывести \n'.format(call.message.from_user), reply_markup=menu6)
        elif call.data == '16':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька в сети TRC20 \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '17':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '18':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '19':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '20':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '21':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '22':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '23':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '24':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '42':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '43':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '44':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '45':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '46':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '47':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '48':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '49':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '50':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '51':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '52':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '53':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '54':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '55':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
        elif call.data == '56':
            await call.message.delete()
            if balance < 100:
                await call.message.answer('Минимальная сумма вывода составляет сумму, равнозначную 100$ по текущему курсу \n'.format(call.message.from_user), reply_markup=menu2)
            else:
                await call.message.answer('Введите адрес своего криптокошелька \n'.format(call.message.from_user), reply_markup=menu2)
                await state.set_state(UserState.vivod)
@dp.message(UserState.next_message5)
async def next_message5(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx5 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Tether (USDT) == {0.0}', f'Tether (USDT) == {round(0.92 * count * price["tether"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                                      f'\n'
                                      f'{round(0.92 * count * price["tether"]["rub"], 2)} руб'.format(message.from_user), reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message6)
async def next_message6(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx6 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Bitcoin (BTC) == {0.0}',
                                f'Bitcoin (BTC) == {round(0.98 * count * price["bitcoin"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["bitcoin"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message7)
async def next_message7(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx7 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Ethereum (ETH) == {0.0}',
                                f'Ethereum (ETH) == {round(0.98 * count * price["ethereum"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["ethereum"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message8)
async def next_message8(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx8 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Litecoin (LTC) == {0.0}',
                                f'Litecoin (LTC) == {round(0.98 * count * price["litecoin"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["litecoin"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message9)
async def next_message9(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx9 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Dogecoin (DOGE) == {0.0}',
                                f'Dogecoin (DOGE) == {round(0.98 * count * price["dogecoin"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["dogecoin"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message10)
async def next_message10(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx10 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Official Trump (TRUMP) == {0.0}',
                                f'Official Trump (TRUMP) == {round(0.98 * count * price["official-trump"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["official-trump"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message11)
async def next_message11(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx11 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Ripple (XRP) == {0.0}',
                                f'Ripple (XRP) == {round(0.98 * count * price["ripple"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["ripple"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message12)
async def next_message12(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx12 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Solana (SOL) == {0.0}',
                                f'Solana (SOL) == {round(0.98 * count * price["solana"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["solana"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message13)
async def next_message13(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx13 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Notcoin (NOT) == {0.0}',
                                f'Notcoin (NOT) == {round(0.98 * count * price["notcoin"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.98 * count * price["notcoin"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message27)
async def next_message27(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx27 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Binarydao (BYTE) == {0.0}',
                                f'Binarydao (BYTE) == {round(0.98 * count * price["binarydao"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["binarydao"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message28)
async def next_message28(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx28 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Cardano (ADA) == {0.0}',
                                f'Cardano (ADA) == {round(0.92 * count * price["cardano"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["cardano"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message29)
async def next_message29(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx29 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Tron (TRX) == {0.0}',
                                f'Tron (TRX) == {round(0.92 * count * price["tron"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["tron"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message30)
async def next_message30(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx30 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Toncoin (TON) == {0.0}',
                                f'Toncoin (TON) == {round(0.92 * count * price["the-open-network"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["the-open-network"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message31)
async def next_message31(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx31 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Avalanche (AVAX) == {0.0}',
                                f'Avalanche (AVAX) == {round(0.92 * count * price["avalanche-2"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["avalanche-2"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message32)
async def next_message32(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx32 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Sui (SUI) == {0.0}',
                                f'Sui (SUI) == {round(0.92 * count * price["sui"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["sui"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message33)
async def next_message33(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx33 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Chainlink (LINK) == {0.0}',
                                f'Chainlink (LINK) == {round(0.92 * count * price["chainlink"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["chainlink"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message34)
async def next_message34(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx34 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Aptos (APT) == {0.0}',
                                f'Aptos (APT) == {round(0.92 * count * price["aptos"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["aptos"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message35)
async def next_message35(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx35 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Stellar (XLM) == {0.0}',
                                f'Stellar (XLM) == {round(0.92 * count * price["stellar"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["stellar"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message36)
async def next_message36(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx36 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Mantra (OM) == {0.0}',
                                f'Mantra (OM) == {round(0.92 * count * price["mantra-dao"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["mantra-dao"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message37)
async def next_message37(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx37 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Hedera (HBAR) == {0.0}',
                                f'Hedera (HBAR) == {round(0.92 * count * price["hedera-hashgraph"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["hedera-hashgraph"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message38)
async def next_message38(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx38 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Polkadot (DOT) == {0.0}',
                                f'Polkadot (DOT) == {round(0.92 * count * price["polkadot"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["polkadot"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message39)
async def next_message39(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx39 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Hyperliquid (HYPE) == {0.0}',
                                f'Hyperliquid (HYPE) == {round(0.92 * count * price["hyperliquid"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["hyperliquid"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message40)
async def next_message40(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx40 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Uniswap (UNI) == {0.0}',
                                f'Uniswap (UNI) == {round(0.92 * count * price["uniswap"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["uniswap"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.next_message41)
async def next_message41(message: types.Message, state: FSMContext):
    count = float(message.text.replace(",", "."))
    my_object.set_variable(count)
    my_object.nx41 = True
    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'r', encoding="utf-8") as f:
        old_data = f.read()

    new_data = old_data.replace(f'Monero (XMR) == {0.0}',
                                f'Monero (XMR) == {round(0.92 * count * price["monero"]["rub"], 2)}')

    with open(f'/root/bot/bal/{[message.chat.id]}.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
    await message.answer(f'Сумма к оплате составит: \n'
                         f'\n'
                         f'{round(0.92 * count * price["monero"]["rub"], 2)} руб'.format(message.from_user),
                         reply_markup=menu4)
    await state.clear()  # Очищаем состояние, завершив диалог
@dp.message(UserState.vivod)
async def vivod(message: types.Message, state: FSMContext):
    await message.answer('Ваша заявка на вывод оформлена! В течение нескольких минут криптовалюта будет выведена \n'.format(message.from_user), reply_markup=menu2)
    await state.clear()


@dp.message(lambda message: message.chat.id == ADMIN_ID and message.reply_to_message)
async def admin_reply(message: types.Message):
    reply_text = message.reply_to_message.text
    match = re.search(r'ID:\s*(\d+)', reply_text)  # Ищем число после "ID: "

    if match:
        user_id2 = int(match.group(1))  # Извлекаем ID пользователя
        await bot.send_message(user_id2, f"✉️ Реквизиты: \n"
                                              f" \n"
                                              f" {message.text}")
        await message.answer("✅ Сообщение отправлено пользователю.")
    else:
        await message.answer("⚠ Не удалось распознать ID пользователя.")

@dp.message(F.document)
async def handle_pdf(message: Message):
    if message.document.mime_type == "application/pdf":
        await message.answer("Пожалуйста, дождитесь проверки чека и зачисления криптовалюты на баланс \n")

        # Сохранение файла
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        # Отправка файла админу
        await bot.send_document(chat_id=ADMIN_ID, document=file_id,
                                caption=f"Новый PDF от {message.from_user.full_name} (@{message.from_user.username})")

        await bot.download_file(file_path, f"/root/bot/pdf/{message.document.file_name}")
        #old_name = f"C:/Users/vnsag/OneDrive/Desktop/Aiogram/pdf/{message.document.file_name}"
        #new_name = f"C:/Users/vnsag/OneDrive/Desktop/Aiogram/pdf/{[message.chat.id]}"

        #os.rename(old_name, new_name)
        time.sleep(15)
        await message.answer('Ваш баланс успешно пополнен! \n', reply_markup=menu2)
    else:
        await message.answer("Отправленный файл не является PDF. \n"
                             "Пожалуйста отправьте верный файл. \n"
                             "\n"
                             "Его можно скачать в вашем онлайн-банке в разделе истории переводов \n")

@dp.message(F.photo)
async def handle_photo(message: Message):
    photo = message.photo[-1]  # Получаем фото в наилучшем качестве
    #file = await bot.get_file(photo.file_id)
    #file_path = file.file_path
    #await bot.download_file(file_path, f"downloads/{photo.file_id}.jpg")
    await message.answer("Пожалуйста, отправляйте чеки в виде файла в формате PDF. \n"
                         "\n"
                         "Иначе бот не сможет обработать вашу заявку \n")

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
