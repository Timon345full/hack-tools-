import telebot
from config import api 
import os 

bot = telebot.TeleBot(api)

# def checkerWeb(message_chat, username, flags="", flagsValue=""): # user name обезательно нужно водить дальше не обезательно флаги аргументы flags и т.д
#     os.system("cd tools")
#     os.system("cd usersInformation")

#     if flags != "" and flagsValue != "":
#         os.system("cd blackbird")
#         value =os.system(f"python blackbird.py -u {username} {flags} {flagsValue} ")
#         bot.send_message(message_chat, value)
#         os.system("cd ../../")
#     else:
#         os.system("cd blackbird")
#         value = os.system(f"python blackbitd.py -u {username}")
#         bot.send_message(message_chat, value)
#         os.system("cd ../../")
        
@bot.message_handler(content_types=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Здравствуйте этот бот предстовляет собой инструмент по нахождению совподений по нику в интернете {message.from_user.first_name}")

@bot.message_handler(content_types=['text'])
def send_text(message):
    # checkerWeb(message.chat.id, message.text)
    bot.send_message(message.chat.id, message.text)
    # os.system('cd tools')
    # os.system("dir")
    # os.system("cd usersInformation")
    # os.system("cd blackbird")
    # text = os.system(f"python blackird.py -u {message.text}")
    # os.system("cd ../../../")
    # print(text)


bot.polling(none_stop=True)