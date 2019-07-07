import os, sys
import requests
import logging
from flask import Flask, render_template, request
app = Flask(__name__)
logging.basicConfig(
            format='%(asctime)s %(levelname)s %(message)s',
            level=logging.INFO,
            datefmt='%m/%d/%Y %I:%M:%S %p'
            )
logger = logging.getLogger(__name__)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/', methods=['GET', 'POST'])
def index():

    results = {}
    errors = []
    logger.info("test")
    if request.method == 'POST' :
        try :
            logger.info("method post")
        except :
            logger.error('Erreur method post')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

