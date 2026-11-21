import random
import telebot

bot = telebot.TeleBot("9066765548:AAGD9drklQAEQJGgJDlho7-URBGuMULTufU")

TIPS = [
    "В IT главное — разбивать задачу на мелкие шаги и проверять каждый по очереди.",
    "Если бот не реагирует на новые команды — чаще всего забыл перезапустить скрипт после сохранения.",
    "Перед отправкой проекта на GitHub всегда убирай токены и пароли из кода.",
]


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет! Я работаю в Telegram!")


@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.reply_to(
        message,
        "Команды:\n"
        "/start - начать работу\n"
        "/help - список команд\n"
        "/about - о боте\n"
        "/ping - проверить связь\n"
        "/tip - совет про IT и ботов",
    )


@bot.message_handler(commands=["about"])
def about_cmd(message):
    bot.reply_to(message, "Я учебный Telegram-бот на Python. Скоро подключу нейросеть.")


@bot.message_handler(commands=["ping"])
def ping_cmd(message):
    bot.reply_to(message, "Понг! Бот в сети и готов к работе.")


@bot.message_handler(commands=["tip"])
def tip_cmd(message):
    bot.reply_to(message, "У данного бота версия 1.1.2")


@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Пока я не подключён к нейросети.")


bot.infinity_polling()