from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')

def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


if __name__ == '__main__':
    token = ''
    request_kwargs = {
    	'proxy_url': ''
    }
    updater = Updater(token=token, request_kwargs=request_kwargs)
    dispatcher = updater.dispatcher

    # Хендлеры
    start_command_handler = CommandHandler('start', startCommand)

    text_message_handler = MessageHandler(Filters.text, textMessage)
    # Добавляем хендлеры в диспетчер
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(text_message_handler)
    # Начинаем поиск обновлений
    updater.start_polling(clean=True)
    # Останавливаем бота, если были нажаты Ctrl + C
    updater.idle()
