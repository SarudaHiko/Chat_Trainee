# Подключение datetime 
from datetime import datetime

# Подключение сервера через Flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Привет! Добро пожаловать в чат "Saruda"'


# Основной код
all_messages = []


# Добавление нового сообщения с временем
def add_messages(sender, text):
    new_messages = {
        'name': sender,
        'text': text,
        'time': datetime.now().strftime('%H:%M:%S | %m.%d.%Y'),
    }
    all_messages.append(new_messages)


# Вывод без скобок
def print_all_messages():
    for message in all_messages:
        name = message['name']
        text = message['text']
        time = message['time']
        print(f'{name}: {text}')
        print({time})


# Работа с Flask
# Добавление получения сообщений
@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages}


# Добавление уведомления об отправке
@app.route('/send_message')
def send_message():
    name = request.args.get('name')
    text = request.args.get('text')
    add_messages(name, text)
    return 'Сообщение отправлено'


# Добавление Html кода
@app.route('/chat')
def chat_page():
    return render_template('Chat.html')

# Настройка и запуск чата в сети
app.run(host='0.0.0.0', port=8080, debug=True)
