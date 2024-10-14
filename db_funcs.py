from db import db_session
from models import User


def create_user(telegram_id, username):
    check_user = User.query.filter_by(telegram_id=telegram_id).first()
    if not check_user:
        new_user = User(
            telegram_id=telegram_id,
            username=username,
        )
        db_session.add(new_user)
        db_session.commit()
        return True
    return False
