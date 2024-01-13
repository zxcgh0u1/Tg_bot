# tg_bot

## Описание

Мой телеграм-бот представляет из себя сборник цитат, которые он берет с сайта Quotable, после чего переводит их на русский язык и заменяет настоящего автора на "(с) Джейсон Стейтем"

## Структура бота

Задается токен для Telegram бота и создается объект бота.
Определены функции get_quote и translate_to_russian для получения случайной цитаты по ссылке "https://api.quotable.io/random" и перевода текста на русский соответственно.
В обработчике команды /start отправляется приветственное сообщение новым пользователям.
В обработчике команды /цитата вызывается функция get_quote для получения случайной цитаты и ее автора.
Цитата переводится на русский с помощью функции translate_to_russian.
Отправляется сообщение с переведенной цитатой и указанием автора.

## Пример работы бота

![image](https://github.com/zxcgh0u1/Tg_bot/assets/102488451/738e0842-7a98-49ab-963c-62be0fb7c646)
![image](https://github.com/zxcgh0u1/Tg_bot/assets/102488451/57c53eb0-0be5-4529-99b7-86ff6d7154e7)
![image](https://github.com/zxcgh0u1/Tg_bot/assets/102488451/989d2e4b-3476-4ff1-a063-816c8ca13f70)
