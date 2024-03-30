from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keys_builder = ReplyKeyboardBuilder()

button_yes = KeyboardButton(text='yes')
button_no = KeyboardButton(text='no')
keys_builder.row(button_yes, button_no)

#
keys_choises = ReplyKeyboardBuilder()

button_stone = KeyboardButton(text='stone')
button_scissors = KeyboardButton(text='scissors')
button_paper = KeyboardButton(text='paper')


keys_choises.row(button_stone, button_scissors, button_paper)
