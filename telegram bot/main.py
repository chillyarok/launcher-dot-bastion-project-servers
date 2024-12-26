import telebot as tbot
import bd_module as bd
token =  "token"
bot = tbot.TeleBot(token)
nick = ""
passw = ""

@bot.message_handler(commands = ["start","info"])
def stert(message):
    start_text = """ru\n
Добро пожаловать в бота сообщества BasMine. Здесь вы можете зарегистрироваться для получения доступа к проекту. Для получения инструкций по регистрации аккаунта впишите /reg_ru\n
    en \n
Welcome to the Basmine community bot. Here you can register to access the project. To receive instructions on account registration, enter /reg_en
    """
    bot.send_message(message.chat.id,start_text)
@bot.message_handler(["reg_ru"])
def register_ru(message):
    msg = bot.send_message(message.from_user.id,"Для регистрации аккаунта введите ниже никнейм который вы будете использовать на сервере:")
    bot.register_next_step_handler(msg,nick_handler_ru)
@bot.message_handler(["reg_en"])
def register_ru(message):
    msg = bot.send_message(message.from_user.id,"To register an account, enter the nickname below that you will use on the server:")
    bot.register_next_step_handler(msg,nick_handler_ru)
bot.polling(non_stop=True)



'''ru block'''
def nick_handler_ru(message):
    nick = message.text
    print(nick)
    msg2 = bot.send_message(message.from_user.id,"Далее введите пароль (постарайтесь не забыть его восстановление пока невозможно):")
    bot.register_next_step_handler(msg2,pass_hendler)


'''en block'''
def nick_handler_en(message):
    nick = message.text
    print(nick)
    msg2 = bot.send_message(message.from_user.id,"Next, enter the password (try not to forget it is not possible to restore it yet):")
    bot.register_next_step_handler(msg2,pass_hendler)


'''own block'''
def pass_hendler(message):
    passw = message.text
    bd.to_bd(str(message.from_user.id),nick,passw)
