# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from violen import draw_violen, list_of_colleges
import time

app = Flask(__name__, static_url_path='/static')  # create instance of Flask class
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/comparison', methods=['GET', 'POST'])
def comparison():
    first = request.form.get('first')
    if first is None:
        first = list_of_colleges[0]
    second = request.form.get('second')
    if second is None:
        second = list_of_colleges[1]

    print("first: {}".format(first))
    print("second: {}".format(second))
    draw_violen(first, second)

    millis = int(round(time.time() * 1000))
    return render_template('comparison.html', list_of_colleges=list_of_colleges,
                           first = first, second = second, millis=millis)


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')


@app.route('/clustering')
def clustering():
    return render_template('clustering.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/draw_violen')
def call_violen(first, second):
    return draw_violen(col1  = first, second= second)


if __name__ == '__main__':
    app.run()
