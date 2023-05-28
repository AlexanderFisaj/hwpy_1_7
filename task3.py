import telebot
from random import randint


file_settings = open('E:\GB\Python\hwpy_1_7\settings.ini', mode='r', encoding='utf-8')
my_token = file_settings.read()
file_settings.close()
bot = telebot.TeleBot(my_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, 'Для начала игры напиши "играть"')

@bot.message_handler(content_types='text')
def read_text_commands(message):
    global secret_number
    global counter
    
    if message.text == 'играть':  
        secret_number = randint(1, 1001)
        counter = 0
        bot.reply_to(message, 'Я задумал число от 1 до 1000! Попробуй его отгадать!')
        bot.register_next_step_handler(message, game)


def game(message):
    global counter
    global secret_number
    
    if message.text.isdigit():
        entered_number = int(message.text)
        if entered_number > secret_number:
            counter += 1
            bot.reply_to(message, '__Меньше!__')
            bot.register_next_step_handler(message, game)
        elif entered_number < secret_number:
            counter += 1
            bot.reply_to(message, '__Больше!__')
            bot.register_next_step_handler(message, game)
        elif entered_number == secret_number:
            bot.reply_to(message, f'{game_answer(counter)}\n__Я загадывал число {secret_number}!__')
            bot.reply_to(message, f'Сделано ходов: {counter}!')
        else:
            bot.reply_to(message, 'Некорректный ввод... Попробуй ещё раз.')
            bot.register_next_step_handler(message, game)
    else:
        bot.reply_to(message, 'Ты ввел не число. Будь внимательнее.\nНужно ввести число...')
        bot.register_next_step_handler(message, game)

def game_answer(switch):
    if switch in range(1, 8):
        return '**Молодец! Ты угадал!**'
    elif switch in range(8, 20):
        return '**Ты угадал! Не плохой результат!**'
    elif switch > 20:
        return '**Ну наконец-то ты угадал!\nПоиздевался, конечно, на до мной... но угадал)**'

bot.polling()