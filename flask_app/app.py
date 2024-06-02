from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

articles = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/article', methods=['GET', 'POST'])
def article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        articles.append({'title': title, 'content': content})
        return redirect(url_for('home'))
    return render_template('article.html')

@app.route('/articles')
def article_list():
    return render_template('articles.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
