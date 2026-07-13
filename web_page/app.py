from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("../page_data/news.json", "r", encoding="utf-8") as f:
        news = json.load(f)

    return render_template("index.html", news=news)

if __name__ == "__main__":
    app.run(debug=True)