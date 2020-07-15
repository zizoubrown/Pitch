from flask import Flask, render_template
app = Flask(__name__)

pitches = [
    {
        'author': 'Abdul Aziz',
        'title':'Pitch 1',
        'content':'First Pitch content',
        'date_posted':'July 14, 2020'
    },
    {
        'author':'Anorld Swaz',
        'title':'Pitch 2',
        'content':'Second Pitch content',
        'date_posted':'July 15, 2020'
    }
]

@app.route('/')
def home():
    return render_template('home.html', pitches=pitches)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)