from telegram import ReplyKeyboardMarkup


def get_kb(old_user=False):
    btns = [
        ['О нас', 'Оплата/Доставка'],
        ['Купить кофе', 'Консультация'],
    ]
    if not old_user:
        btns.extend([['Отследить заказ', 'История заказов']])
    return ReplyKeyboardMarkup(btns, resize_keyboard=True)
