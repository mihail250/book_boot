from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
import random


from aiogram import Router, F
from keyboards import keyboard_utils

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                        reply_markup=keyboard_utils.keys_builder.as_markup())

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

@router.message(F.text == 'yes')
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['yes'],
                        reply_markup=keyboard_utils.keys_choises.as_markup())
    




@router.message(F.text == 'stone')
@router.message(F.text == 'scissors')
@router.message(F.text == 'paper')
async def process_help_command(message: Message):
    res = {tuple(sorted(('stone', 'paper'))): 'paper',
       tuple(sorted(('stone', 'scissors'))): 'stone',
       tuple(sorted(('scissors', 'paper'))): 'scissors'
       }
    all = ['scissors', 'paper', 'stone']
    bot_choice = random.choice(all)
    winner = {bot_choice: 'BOT',
              message.text: 'player',
              'nobody wins': 'nobody wins'
              }
    if bot_choice == message.text:
        result = 'nobody wins'
    else:
        key = tuple(sorted([message.text, bot_choice]))
        result = res[key]


    await message.answer(text=f'your choice: {message.text}, bot choice: {bot_choice}, winner: {winner[result]}',
                        )
