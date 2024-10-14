from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update

import config
import db_funcs
from models import Order, User
import utils


def about_us(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Инфо о нас
Инфо о нас
Инфо о нас''',
    )


def answer_to_user(update: Update, context: CallbackContext):
    if update.message.chat.id == config.ADMIN_ID:
        print('ты админ')
        print(update.message.reply_to_message.forward_from.id)
    else:
        print('нет')


def greet_user(update: Update, context: CallbackContext):
    telegram_id = update.message.chat.id
    username = update.message.chat.username
    response = db_funcs.create_user(telegram_id, username)
    update.message.reply_text(
        f'Привет, {username.capitalize()}!',
        reply_markup=utils.get_kb(response),
    )


def fetch_orders(update: Update, context: CallbackContext):
    telegram_id = update.message.chat.id
    user_id = User.query.filter_by(telegram_id=telegram_id).first().id
    all_orders = Order.query.filter_by(user_id=user_id).all()
    if all_orders:
        for order in all_orders:
            if update.message.text == 'История заказов':
                update.message.reply_text(str(order))
            elif order.status != 'close':
                update.message.reply_text(str(order))
    else:
        update.message.reply_text('У вас нет активных заказов')


def start_conversation(update: Update, context: CallbackContext):
    update.message.reply_text('Напишите Ваш вопрос...')
    return 'send_question'


def send_question(update: Update, context: CallbackContext):
    context.bot.forward_message(
        chat_id=config.ADMIN_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id,
    )
    return ConversationHandler.END
