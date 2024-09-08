from flask import Flask, render_template, request
from model import summarize_text
from newspaper import Article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        print(f'URL received: {url}')  # Debug print
        article = Article(url)
        article.download()
        article.parse()
        summary = summarize_text(article.text)
        return render_template('index.html', article=article.text[:1000], summary=summary)
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting Flask application...")  # Debug print
    app.run(debug=True)
