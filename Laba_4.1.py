import telebot
import requests
from googletrans import Translator

# Задаем токен вашего бота
token = '6593023929:AAEpKcrOCweJvKHQYuxzvdbvdYLZ3zUNW0E'

# Создаем объект бота
bot = telebot.TeleBot(token)

def get_quote():
    # URL для получения цитаты
    api_url = "https://api.quotable.io/random"

    try:
        # Отправляем GET-запрос на получение цитаты
        response = requests.get(api_url)
        response.raise_for_status()  # Проверяем, есть ли ошибки

        # Получаем цитату из ответа
        quote_data = response.json()

        # Извлекаем необходимую информацию
        quote_text = quote_data['content']
        quote_author = quote_data['author']

        return quote_text, quote_author

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def translate_to_russian(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='ru')
    return translation.text

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    # Отправляем сообщение с объяснением возможностей бота
    help_message = ("Привет! Я - бот Джейсона Стейтема. Мои команды:\n"
                    "/start - начать общение с ботом\n"
                    "/quote - получить случайную цитату\n"
                    "/help - получить справку о доступных командах")
    bot.send_message(message.chat.id, help_message)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Приветственное сообщение
    welcome_message = ("Привет! Я Джейсон Стейтем и я научу тебя жить жизнь!\n"
                       "Напиши /quote, не пожалеешь!")
    bot.send_message(message.chat.id, welcome_message)

# Обработчик команды /цитата
@bot.message_handler(commands=['quote'])
def handle_quote(message):
    # Получаем цитату
    quote_text, quote_author = get_quote()

    # Переводим цитату на русский
    translated_quote = translate_to_russian(quote_text)

    # Отправляем переведенную цитату с указанием автора
    bot.send_message(message.chat.id, f"Цитата:\n{translated_quote}\n\n(c) Джейсон Стейтем")

# Обработчик текстовых сообщений без команд
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    # Отправляем сообщение о том, что бот не понимает текст
    unknown_message = ("Извини, я не понимаю этот текст. "
                       "Воспользуйтесь командами /start, /quote или /help.")
    bot.send_message(message.chat.id, unknown_message)


# Запускаем бота
bot.polling(none_stop=True)
