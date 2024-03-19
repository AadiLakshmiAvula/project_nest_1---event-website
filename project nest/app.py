from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')  # Define a route for the "Login" page
def login():
    return render_template('login.html')  # Directly render the "Registration" page

@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
