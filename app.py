from flask import Flask, render_template, url_for

# Double underscore name is a special variable in Python that is the name of the module.
app = Flask(__name__)

posts = [
    {
        'author': 'Henry Tran',
        'title': 'Hello World!',
        'content': 'First post!',
        'date_posted': 'November 11, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Welcome Henry!',
        'content': 'Welcome to Alpha!',
        'date_posted': 'November 12, 2020'
    }
]

# Route decorators | Seems similar to linking in React (?)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)