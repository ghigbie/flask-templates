from flask import Flask, render_template
app = Flask(__name__)

app_name_foundation = "Chubby Puppy"

@app.route('/')
def index():
    return render_template('home.html', app_name_foundation=app_name_foundation)

@app.route('/about')
def about():
    return render_template('about.html', app_name_foundation=app_name_foundation)

@app.route('/contact')
def contac():
    return render_template('contact.html', app_name_foundation=app_name_foundation)
    
if __name__ == '__main__':
    app.run(debug=True)