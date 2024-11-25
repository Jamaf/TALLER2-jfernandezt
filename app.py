from flask import Flask
from flask import render_template

from controllers.animal_controller import animal_blueprint

app = Flask(__name__, template_folder="views")

app.register_blueprint(animal_blueprint)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)