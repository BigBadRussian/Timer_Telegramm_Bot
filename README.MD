# DEVMAN
## Курс основы Python.  
## Урок 7 "Считаем секунды в Telegram"
### Описание
Таймер с прогресс-баром в формате бота телеграмм
### Регистрация бота в telegram
В интерфейсе telegram с помощью поиска чатов найдите бота BotFather.
```bash
/start
```
```bash
/newbot
```
```
type_bot_name
```
### Установка и запуск
1. Python 3 должен бытть установлен. 
2. Скачайте архив из репозитория. Распакуйте архив в нужную вам директорию. Обратите внимание файл ptbot.py должен лежать рядом с файлом script_1.py
3. В данной директории нужно создать файл .env  
В файл .env необходимо указать токен вашего бота:
```bash
TG_TOKEN=...
``` 
4. Используя pip, установите необходимые библиотеки из файла requirements.txt:
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
```bash
pip install -r requirements.txt
```
5. Запустите скрипт:
```bash
python3 script_1.py
```
Пока скрипт крутится - бот работает. Чтобы запустить таймер отправьте сообщения формата: ns, где n - количество секунд, например 5 s.
### Пример работы
![](https://github.com/BigBadRussian/Timer_Telegramm_Bot/blob/master/timer_tg_bot.gif)
