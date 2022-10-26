from flask import render_template, Blueprint, request
from functions import search_by_query

main_blueprint = Blueprint('main_blueprint', __name__,
                           template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    query = request.args.get('s')
    posts = search_by_query(query)
    return render_template('post_list.html', query=query, posts=posts)