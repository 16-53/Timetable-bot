import calendar
import datetime
from datetime import date
from pathlib import Path

from telebot import TeleBot, types
from timetable import timetable

token = Path("token.txt").read_text().strip()
bot = TeleBot(token)


@bot.message_handler(commands=["start", "help"])
def start(message):
    text = "Hey there! \n" "Write /next_lesson to find out what the next lesson is"
    bot.send_message(message.chat.id, text, reply_markup=actions())


@bot.message_handler(commands=["next_lesson"])
def lesson(message):
    date_now = date.today()
    hour = datetime.datetime.today().hour
    minute = datetime.datetime.today().minute
    weekday = calendar.day_name[date_now.weekday()]
    
    if weekday == "Sunday" or weekday == "Saturday":
        bot.send_message(message.chat.id, 'Have a nice weekend!')
        
    else:       
        time_table = timetable(weekday)
        text = ""

        for i in range(len(time_table) - 1):
            start_lesson = list(map(int, time_table[i][0].split(":")))
            start_lesson_2 = list(map(int, time_table[i + 1][0].split(":")))


            if hour < 7 or hour == 7 and minute <= 45:
                text = time_table[i][0] + " - " + time_table[i][1]
                for i in range(len(time_table[0][2])):
                    text += time_table[0][2][i] + "\n"
                bot.send_message(message.chat.id, text)
                break
            
            elif (
                hour < start_lesson_2[0]
                or (hour == start_lesson_2[0] and minute <= start_lesson_2[1])
            ):
                text = time_table[i+1][0] + " - " + time_table[i+1][1]
                for j in range(len(time_table[i+1][2])):
                    text += time_table[i+1][2][j] + "\n"
                bot.send_message(message.chat.id, text)
                break
            
        if text == "":
            text = "Congratulations! No more lessons for today!"
            bot.send_message(message.chat.id, text)


def actions():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button_next_lesson = types.KeyboardButton("/next_lesson")
    keyboard.add(button_next_lesson)
    
    return keyboard

bot.polling(none_stop=True, interval=0)
