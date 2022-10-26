import json

path_data_json = 'posts.json'
def get_data_from_json(path_data_json='posts.json'):
    """
    Функция загружает данные из json в список словарей
    :param path_data_json: принимает название файла json
    :return: список словарей с постами
    """
    with open (path_data_json, 'r', encoding='utf-8') as file:
        return json.load(file)


def search_by_query(query) -> list[dict]:
    """
    Функция возвращет список с постами словарями,
    где есть введеный пользователем запрос
    :param query: get запрос str пользователя
    :return: список словарей где в контенте присутствует
    переданная подстрока

    """
    posts = get_data_from_json()
    search_posts = []
    for post in posts:
        if query in post['content']:
            search_posts.append(post)

    return search_posts


def add_post(post, path_data_json='posts.json'):
    posts = get_data_from_json()
    posts.append(post)
    with open(path_data_json, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
