from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        try:
            title = request.form['search']
            page = wikipedia.page(title, auto_suggest=False)
            return render_template('search.html',
                                title=page.title,
                                summary=page.summary,
                                url=page.url)
        except wikipedia.DisambiguationError as e:
            return render_template('search.html',
                                disambiguation=e.options[:5])
        except wikipedia.PageError:
            return render_template('search.html',
                                error=f"Page '{title}' not found")
    return render_template('search.html')


if __name__ == '__main__':
    app.run()