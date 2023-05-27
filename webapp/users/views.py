from flask import Blueprint, request
from uuid import uuid4

from webapp.db import db
from webapp.users.models import User


blueprint = Blueprint('users',  __name__)

@blueprint.route('/api/v1.0/registration', methods=['POST'])
def registration() -> dict:
    """Сервис принимает на вход запросы с именем пользователя"""

    user_name = request.json['name']
    check_user_name = User.query.filter(User.name==user_name).first()
    if check_user_name != None:
        return {
        'error': 'This name is in use, try something else',
        }
    else:
        create_use_in_db = User(
            name = request.json['name'],
            access_token = uuid4()
            )
        
        db.session.add(create_use_in_db)
        db.session.commit()

        current_user = User.query.filter(User.name==user_name).first()

        return {
            'id': current_user.id,
            'name': current_user.name,
            'access_token': current_user.access_token,
            }