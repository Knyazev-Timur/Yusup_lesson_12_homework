from flask import Flask, send_from_directory

from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.run()


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

app.run()
