from logging import debug
from flask import Flask, render_template, request

from textblob import TextBlob

from textblob import Word

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/define',methods = ['POST'])
def predict():
    ip_word = request.form.get('ip-word')
    
    res = ' '.join(map(str, Word(ip_word).definitions))
    return render_template('base.html',prediction_text=f'\n the meaning of the word {(ip_word)}  is : {res}')

if __name__=='__main__':
    app.run(debug=True)