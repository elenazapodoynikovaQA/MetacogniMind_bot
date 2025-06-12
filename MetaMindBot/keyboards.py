from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Помощь⁉️", callback_data="s:help"))
    kb.insert(InlineKeyboardButton(text="Pomodoro-таймер🍅", callback_data="s:pomodoro"))
    kb.add(InlineKeyboardButton(text="Метакогнитивный тренинг", callback_data="s:metakog"))
    kb.add(InlineKeyboardButton(text="Тренинг с информацией", callback_data="s:info"))
    kb.insert(InlineKeyboardButton(text="Рефлексия", callback_data="s:reflect"))
    kb.add(InlineKeyboardButton(text="Чат с психологом", callback_data="s:psycho"))
    kb.insert(InlineKeyboardButton(text="Пройти тест заново", callback_data="s:retest"))
    kb.add(InlineKeyboardButton(text="Профиль", callback_data="s:profile"))
    kb.add(InlineKeyboardButton(text="Курсы", callback_data="s:courses"))
    kb.insert(InlineKeyboardButton(text="Ресурсы", callback_data="s:resources"))
    kb.add(InlineKeyboardButton(text="MetamegaQuiz", callback_data="s:metamega"))



    return kb


def main_menu_keyboard():
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(text="В главное меню", callback_data="main_menu"))

    return kb

def metamega_quiz_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="В главное меню", callback_data="main_menu"))
    return kb
