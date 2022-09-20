import calendar
from datetime import date, datetime, timedelta
from pathlib import Path

from telebot import TeleBot, types
from timetable import timetable

token = Path("token.txt").read_text().strip()
bot = TeleBot(token)


@bot.message_handler(commands=["start", "help"])
def start(message):
    text = (
        "Hey there! \n"
        "Commands: \n"
        "/next_lesson - to find out what the next lesson is \n"
        "/tt_today - to get today's timetable \n"
        "/tt_tomorrow - to get tomorrow's timetable"
    )
    bot.send_message(message.chat.id, text, reply_markup=actions())


@bot.message_handler(commands=["tt_today"])
def tt_today(message):
    date_now = date.today()
    weekday = calendar.day_name[date_now.weekday()]

    if weekday == "Sunday" or weekday == "Saturday":
        bot.send_message(message.chat.id, "No lessons for today!")

    else:
        time_table = timetable(weekday)
        text = ""

        for i in range(len(time_table)):
            text += "\n" + (time_table[i][0] + " - " + time_table[i][1])
            for j in range(len(time_table[i][2])):
                text += "\n" + time_table[i][2][j]
            text += "\n"

        bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["tt_tomorrow"])
def tt_tomorrow(message):
    date_tomorrow = date.today() + timedelta(days=1)
    weekday = calendar.day_name[date_tomorrow.weekday()]

    if weekday == "Sunday" or weekday == "Saturday":
        bot.send_message(message.chat.id, "No lessons for tomorrow!")

    else:
        time_table = timetable(weekday)
        text = ""

        for i in range(len(time_table)):
            text += "\n" + (time_table[i][0] + " - " + time_table[i][1])
            for j in range(len(time_table[i][2])):
                text += "\n" + time_table[i][2][j]
            text += "\n"

        bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["next_lesson"])
def lesson(message):
    date_now = date.today()
    hour = (datetime.utcnow() + timedelta(hours=3)).hour
    minute = (datetime.utcnow() + timedelta(hours=3)).minute
    weekday = calendar.day_name[date_now.weekday()]

    if weekday == "Sunday" or weekday == "Saturday":
        bot.send_message(message.chat.id, "Have a nice weekend!")

    else:
        time_table = timetable(weekday)
        text = ""

        for i in range(len(time_table) - 1):
            start_lesson_2 = list(map(int, time_table[i + 1][0].split(":")))

            if hour < 7 or hour == 7 and minute <= 45:
                text = time_table[i][0] + " - " + time_table[i][1]
                for j in range(len(time_table[0][2])):
                    text += "\n" + time_table[0][2][j]
                bot.send_message(message.chat.id, text)
                break

            elif hour < start_lesson_2[0] or (
                hour == start_lesson_2[0] and minute <= start_lesson_2[1]
            ):
                text = time_table[i + 1][0] + " - " + time_table[i + 1][1]
                for j in range(len(time_table[i + 1][2])):
                    text += "\n" + time_table[i + 1][2][j]
                bot.send_message(message.chat.id, text)
                break

        if text == "":
            text = "Congratulations! No more lessons for today!"
            bot.send_message(message.chat.id, text)


def actions():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.row_width = 3

    button_next_lesson = types.KeyboardButton("/next_lesson")
    button_tt_today = types.KeyboardButton("/tt_today")
    button_tt_tomorrow = types.KeyboardButton("/tt_tomorrow")

    keyboard.row(button_next_lesson, button_tt_today, button_tt_tomorrow)

    return keyboard


bot.polling(none_stop=True, interval=0)
