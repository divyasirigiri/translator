from logging import debug
from flask import Flask, render_template, request

from textblob import TextBlob
from textblob import Word

app1 = Flask(__name__)


@app1.route('/')
def hello():
    return render_template('base.html')

@app1.route('/define',methods = ['POST'])
def define():
    ip_word = request.form.get('ip-word')
    
    res = ' '.join(map(str, Word(ip_word).definitions))
    return render_template('base.html',prediction_text=f'\n the meaning of the word {(ip_word)}  is : {res}')

if __name__=='__main__':
    app1.run(debug=True)
