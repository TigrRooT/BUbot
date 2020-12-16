tabl = {"Яблоко": 9.8, 'Банан': 21.8,'Груша': 15.2,'Абрикос': 11.1,'Ананас': 10.5,'Арбуз': 7.5,'Апельсин': 8.1,'Виноград': 18.1,'Гранат': 11,'Грейпфрут': 10.6,'Дыня': 7.4,'Киви': 10.2,'Клубника': 7.7,'Малина': 11.9,'Манго': 15,'Мандарин': 13.3,'Персик': 9.5,'Слива': 11,'Хурма': 33.5,'Черника': 14.4,'Морковь': 9.5,'Свекла': 9.5,'Кукуруза': 18.7}
import telebot
name = 0
z = 0
e = 0
vvv = 0
text = 0
bog = 0
m = 0
bot = telebot.TeleBot('#####');
@bot.message_handler(content_types=['text'])
def reg_name(message):
    bot.send_message(message.from_user.id, "Привет, я умею счетать ХЕ (все продукты пишутся в единственном числе)")
    bot.send_message(message.from_user.id, "Введи количество углеводов (г)")
    bot.register_next_step_handler(message, ainput)
def ainput(message):
    global vvv
    vvv = message.text
    if vvv is None:
        bot.send_message(message.from_user.id, "Необходимо вводить числа!")
        bot.send_message(message.from_user.id, "Введи количество углеводов (г)")
        bot.register_next_step_handler(message, ainput)
    else:    
        bot.send_message(message.from_user.id, "Введите массу нетто (г)") 
        bot.register_next_step_handler(message, binput)

def binput(message):
    global e
    e = message.text
    try:
        if e is None: 
            bot.send_message(message.from_user.id, "Необходимо вводить числа!")
            bot.send_message(message.from_user.id, "Введи количество углеводов (г)")
            bot.register_next_step_handler(message, ainput)
        else:
            bot.send_message(message.from_user.id, ""+str(round((float(vvv)/100*float(e)/12), 1))+" ХЕ")
            bot.send_message(message.from_user.id, '''/Products (продукты)  \n/BreadUnits (подсчетать ХЕ)''')
            if message.text == "/Products":
                bot.send_message(message.from_user.id, "Чтобы вернуться напиши <Выход>")
                bot.register_next_step_handler(message, prod)
            else: 
                bot.register_next_step_handler(message, ссс)
    except ValueError:
        bot.send_message(message.from_user.id, "Необходимо вводить числа!")
        bot.send_message(message.from_user.id, "Введи количество углеводов (г)")
        bot.register_next_step_handler(message, ainput)
def ссс(message):
    if message.text == "/Products":
        bot.send_message(message.from_user.id, "Чтобы вернуться напиши <Выход>")
        bot.register_next_step_handler(message, prod)
        bot.send_message(message.from_user.id, "Введи продукт который хочешь найти")
    else:
        bot.send_message(message.from_user.id, "Введи количество углеводов (г)")
        bot.register_next_step_handler(message, ainput)
def prod(message):
    global name
    name = message.text 
    tabl = {"Яблоко": 9.8, 'Банан': 21.8,'Груша': 15.2,'Абрикос': 11.1,'Ананас': 10.5,'Арбуз': 7.5,'Апельсин': 8.1,'Виноград': 18.1,'Гранат': 11,'Грейпфрут': 10.6,'Дыня': 7.4,'Киви': 10.2,'Клубника': 7.7,'Малина': 11.9,'Манго': 15,'Мандарин': 13.3,'Персик': 9.5,'Слива': 11,'Хурма': 33.5,'Черника': 14.4,'Морковь': 9.5,'Свекла': 9.5,'Кукуруза': 18.7}
    if message.text in tabl:
        bot.send_message(message.from_user.id, ""+str(tabl[message.text])+"г углеводов.")
        bot.send_message(message.from_user.id, "Введите массу продукта (г)")
        bot.register_next_step_handler(message, zzzz)
    elif message.text == "Выход" or "/Exit":
        bot.send_message(message.from_user.id, "Введи количество углеводов (г)")
        bot.register_next_step_handler(message, ainput)
    else:
        bot.register_next_step_handler(message, prod)
        bot.send_message(message.from_user.id, "Введи продукт который хочешь найти")
def zzzz(message):
    try: 
        if message.text is None:
            bot.send_message(message.from_user.id, "Необходимо вводить числа!")
            bot.send_message(message.from_user.id, "Введи продукт который хочешь найти")
            bot.register_next_step_handler(message, prod)
        else:    
            z = float(tabl[name])/100*float(message.text)/12
            bot.send_message(message.from_user.id, ""+str(round(z, 1))+" ХЕ")
            bot.send_message(message.from_user.id, "Введи продукт который хочешь найти или можешь выйти(/Exit)")
            bot.register_next_step_handler(message, prod)
    except ValueError:
        bot.send_message(message.from_user.id, "Необходимо вводить числа!")
        bot.send_message(message.from_user.id, "Введи продукт который хочешь найти")
        bot.register_next_step_handler(message, prod)

bot.polling(none_stop=True, interval=0)