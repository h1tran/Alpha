from flask import Flask, escape, request

# Double underscore name is a special variable in Python that is the name of the module.
app = Flask(__name__)

# Route decorators | Seems similar to linking in React (?)
@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)