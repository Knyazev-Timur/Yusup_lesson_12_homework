from flask import render_template, Blueprint, request

from functions import *
from loader.utils import *

loader_blueprint = Blueprint('loader_blueprint', __name__,
                             template_folder='templates', url_prefix='/')


@loader_blueprint.route('/post')
def load_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def upload_post():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Картина или текст не были отправлены'

    path_to_picture = save_picture(picture)

    post = {'pic': path_to_picture, 'content': content}

    add_post(post)

    return render_template('post_uploaded.html', path=path_to_picture, content=content)

