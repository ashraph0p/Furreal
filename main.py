import os
import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ['SECRET']
headers = {
    'x-api-key': os.environ['API_KEY']
}


@app.route("/")
def home():
    img_cat = requests.get("https://api.thecatapi.com/v1/images/search", headers).json()[0]['url']
    fact_cat = requests.get("https://catfact.ninja/fact").json()['fact']
    return render_template('index.html', cat_img=img_cat, cat_fact=fact_cat)


if __name__ == "__main__":
    app.run(debug=True)
