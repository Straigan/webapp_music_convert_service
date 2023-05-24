from flask import Blueprint, render_template


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/api/v1.0')
def index():
    return {'program': 'Hello World'}