from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about_1')
def about_1():
    return render_template('about_1.html')

@app.route('/about_2')
def about_2():
    return render_template('about_2.html')

@app.route('/about_3')
def about_3():
    return render_template('about_3.html')

if __name__ == '__main__':
    app.run(debug=True)

