from flask import Flask, render_template
import requests

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=7a2210d4e71141cd9f3207e3b13b3873"
    r = requests.get(url).json()
    
    news = {
        'articles' : r['articles']
    }
    return render_template('index.html', allNews = news)


if __name__ == '__main__':
    app.run(debug=True)
