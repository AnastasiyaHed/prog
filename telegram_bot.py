import telebot
from telebot import types
import datetime
import re
import random
from datetime import datetime

token = "token"####
bot = telebot.TeleBot(token)

class User:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.full_name = None
        self.address = None
        self.phone_number = None
        self.date = None
        self.time = None

users = {}

def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Услуги'))
    keyboard.add(types.KeyboardButton('Хочу оформить заказ'))
    keyboard.add(types.KeyboardButton('Отменить заказ'))
    return keyboard

def create_services_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Генеральная уборка квартир', callback_data='service_1'))
    keyboard.add(types.InlineKeyboardButton('Уборка после ремонта', callback_data='service_2'))
    keyboard.add(types.InlineKeyboardButton('Поддерживающая уборка', callback_data='service_3'))
    keyboard.add(types.InlineKeyboardButton('Мойка окон любой сложности', callback_data='service_4'))

    return keyboard

@bot.message_handler(commands=['start'])
def start_message(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Добрый день, {user_name}! Вас приветствует ассистент клининговой компании "CleanCo". Как я могу вам помочь?', reply_markup=create_keyboard())
    users[message.chat.id] = User(message.chat.id)

@bot.message_handler(func=lambda message: message.text == 'Услуги')
def show_services(message):
    services = [
        {'name': 'Генеральная уборка квартир', 'price': 'от 3 руб/м²', 'description': '*Удаление максимально возможных загрязнений, \n*Работы осуществляются на всю высоту \n*Влажная уборка помещений с применением промышленных пылесосов, роторных машин и специальных средств'},
        {'name': 'Уборка после ремонта', 'price': 'от 3,3 руб/м²', 'description': '*Удаление максимально возможных загрязнений, \n*Работы осуществляются на всю высоту \n*Влажная уборка помещений с применением промышленных пылесосов, роторных машин и специальных средств \n*Удаление после строительной пыли и следов ремонта, очистка от краски, цемента, клея и т. д.'},
        {'name': 'Поддерживающая уборка', 'price': 'от 1 руб/м²', 'description': '*Удаление легких/средних загрязнений, \n*Работы осуществляются не выше 2.2 м от пола \n*Применяется сухая и влажная уборка пола и всех поверхностей (столы, плинтуса, двери, подоконники)'},
        {'name': 'Мойка окон любой сложности', 'price': 'Нестандартное окно от 3 руб/м²', 'description': '*Двухстворчатое окно с обеих сторон (рамы и подоконники): 18 руб, \n*Мойка послестроительных окон: 25 руб'},
    ]

    response = 'Список услуг:\n\n'
    for service in services:
        response += f"Название: {service['name']}\n"
        response += f"Цена: {service['price']}\n"
        response += f"Описание:\n {service['description']}\n\n"

    bot.send_message(message.chat.id, response)

@bot.message_handler(func=lambda message: message.text == 'Хочу оформить заказ')
def show_services(message):
    bot.send_message(message.chat.id, 'Пожалуйста, выберите услугу:', reply_markup=create_services_keyboard())

@bot.callback_query_handler(func=lambda call: call.data.startswith('service_'))
def select_service(call):
    service_id = int(call.data.split('_')[1])
    services = [
        {'name': 'Генеральная уборка квартир', 'price': 'от 3 руб/м²', 'description': '*Удаление максимально возможных загрязнений, \n*Работы осуществляются на всю высоту \n*Влажная уборка помещений с применением промышленных пылесосов, роторных машин и специальных средств'},
        {'name': 'Уборка после ремонта', 'price': 'от 3,3 руб/м²', 'description': '*Удаление максимально возможных загрязнений, \n*Работы осуществляются на всю высоту \n*Влажная уборка помещений с применением промышленных пылесосов, роторных машин и специальных средств \n*Удаление после строительной пыли и следов ремонта, очистка от краски, цемента, клея и т. д.'},
        {'name': 'Поддерживающая уборка', 'price': 'от 1 руб/м²', 'description': '*Удаление легких/средних загрязнений, \n*Работы осуществляются не выше 2.2 м от пола \n*Применяется сухая и влажная уборка пола и всех поверхностей (столы, плинтуса, двери, подоконники)'},
        {'name': 'Мойка окон любой сложности', 'price': 'Нестандартное окно от 3 руб/м²', 'description': '*Двухстворчатое окно с обеих сторон (рамы и подоконники): 18 руб, \n*Мойка послестроительных окон: 25 руб'},
    ]
    selected_service = services[service_id - 1]

    users[call.message.chat.id].service = selected_service['name']

    bot.send_message(call.message.chat.id, f'Вы выбрали услугу "{selected_service["name"]}"\n'
                                           f'Цена: {selected_service["price"]}\n'
                                           f'Описание: {selected_service["description"]}\n\n'
                                           'Пожалуйста, введите свое ФИО:')

@bot.message_handler(func=lambda message: True if message.chat.id in users and users[message.chat.id].service else False)
def process_order(message):
    current_user = users[message.chat.id]

    if current_user.full_name is None:
        current_user.full_name = message.text
        bot.send_message(message.chat.id, 'Введите адрес:')
    elif current_user.address is None:
        current_user.address = message.text
        bot.send_message(message.chat.id, 'Введите номер телефона в формате +375XXXXXXXXX:')
    elif current_user.phone_number is None:
        phone_pattern = r'\+375\d{9}'
        if re.match(phone_pattern, message.text):
            current_user.phone_number = message.text
            bot.send_message(message.chat.id, 'Введите желаемую дату в формате дд/мм/гггг:')
        else:
            bot.send_message(message.chat.id,'Некорректный формат номера телефона. Пожалуйста, введите номер в формате +375XXXXXXXXX.')
    elif current_user.date is None:
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        if re.match(date_pattern, message.text):
            current_user.date = message.text
            bot.send_message(message.chat.id, 'Введите желаемое время:')
        else:
            bot.send_message(message.chat.id,'Некорректный формат даты. Пожалуйста, введите дату в формате дд/мм/гггг.')
    elif current_user.time is None:
        current_user.time = message.text
        time_pattern = r'\d{2}:\d{2}'
        if re.match(time_pattern, message.text):
            current_user.time = message.text
            current_date = datetime.now().strftime("%d%m%Y")  # Текущая дата в формате "ГГГГММДД"
            current_user.order_number = current_date + str(random.randint(1000, 9999))  # Генерация номера заказа с датой
            bot.send_message(message.chat.id, 'Спасибо за заказ. Номер вашего заказа: {}'.format(current_user.order_number))

            # Отправка сообщения администратору с данными пользователя

            admin_chat_id = '676134939'
            admin_message = f'Новый заказ\nИмя: {current_user.name}\nНомер телефона: {current_user.phone}\nВремя: {current_user.time}\nНомер заказа: {current_user.order_number}'
            bot.send_message(admin_chat_id, admin_message)
        else:
            bot.send_message(message.chat.id, 'Некорректный формат времени. Пожалуйста, введите время в формате ЧЧ:ММ.')

@bot.message_handler(func=lambda message: message.text == 'Отменить заказ')
def request_order_to_cancel(message):
    msg = bot.send_message(message.chat.id, 'Введите номер заказа для отмены:')
    bot.register_next_step_handler(msg, cancel_order)

def cancel_order(message):
    order_number = message.text
    bot.send_message(message.chat.id, f'Заказ номер {order_number} отменен.')


bot.infinity_polling()

# не отправляет сообщение администратору






