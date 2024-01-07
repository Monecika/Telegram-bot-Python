from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = '/start'
quit_button = '/quit'
add_task_button = '/add_task'
remove_button = '/remove'
show_button = '/show'

user_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=start_button)
        ],
        [
            KeyboardButton(text=add_task_button),
            KeyboardButton(text=remove_button)
        ],
        [
            KeyboardButton(text=quit_button),
            KeyboardButton(text=show_button)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
