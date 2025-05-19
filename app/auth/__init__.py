from flask import Blueprint

bp = Blueprint('auth', __name__)


@bp.after_request
def add_cache_control(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

from app.auth import routes