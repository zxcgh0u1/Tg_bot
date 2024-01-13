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

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Приветственное сообщение
    welcome_message = ("Привет! Я Джейсон Стейтем и я научу тебя жить жизнь!\n"
                       "Напиши /цитата, не пожалеешь!")
    bot.send_message(message.chat.id, welcome_message)

# Обработчик команды /цитата
@bot.message_handler(commands=['цитата'])
def handle_quote(message):
    # Получаем цитату
    quote_text, quote_author = get_quote()

    # Переводим цитату на русский
    translated_quote = translate_to_russian(quote_text)

    # Отправляем переведенную цитату с указанием автора
    bot.send_message(message.chat.id, f"Цитата:\n{translated_quote}\n\n(c) Джейсон Стейтем")

# Запускаем бота
bot.polling(none_stop=True)
