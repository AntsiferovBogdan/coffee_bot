from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

import config
import handlers


def main():
    bot = Updater(config.API_TOKEN)

    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', handlers.greet_user))

    conv = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Консультация)$'), handlers.start_conversation),
        ],
        states={
            'send_question': [MessageHandler(Filters.text, handlers.send_question)],
        },
        fallbacks=[],
    )

    dp.add_handler(conv)
    dp.add_handler(MessageHandler(Filters.text, handlers.answer_to_user))
    dp.add_handler(MessageHandler(Filters.regex('^(О нас)$'), handlers.about_us))
    dp.add_handler(MessageHandler(Filters.regex('^(Отследить заказ)$'), handlers.fetch_orders))
    dp.add_handler(MessageHandler(Filters.regex('^(История заказов)$'), handlers.fetch_orders))

    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
