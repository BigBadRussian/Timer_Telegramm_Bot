import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
bot = ptbot.Bot(TG_TOKEN)


def reply_to_user(chat_id, user_text):
    message_id = bot.send_message(chat_id, "Таймер запущен")
    timer = parse(user_text)
    bot.create_countdown(timer, notify_secs, user_id=chat_id, message_id=message_id, user_text=user_text)
    bot.create_timer(timer, send_message_time_is_over, user_id=chat_id)


def notify_secs(secs_left, user_id, message_id, user_text):
    new_message = f"Осталось {secs_left} секунд \n {render_progressbar(parse(user_text), secs_left)}"
    bot.update_message(user_id, message_id, new_message)


def send_message_time_is_over(user_id):
    answer = "Время вышло!"
    bot.send_message(user_id, answer)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    bot.reply_on_message(reply_to_user)
    bot.run_bot()


if __name__ == "__main__":
    main()
