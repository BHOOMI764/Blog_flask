from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Bhoomi jaiswal',
        'title': 'Blog on Flask',
        'content': 'First post content',
        'date_posted': 'jan 20, 2025'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)