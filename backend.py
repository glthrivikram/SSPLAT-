from flask import *
import pandas as pd 
from flask import jsonify, request
import json
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    data = pd.read_csv('D:/clg/mini proj/ssplat/articles.csv')
    return jsonify({"sum":sum(data['source.id'] == 'the-hindu')})

@app.route('/count', methods=['GET'])
def count():
    data = pd.read_csv('D:/clg/mini proj/ssplat/articles.csv')
    c = data.shape[0]
    return jsonify({"count":c })

@app.route('/source', methods=['GET'])
def unique():
    data = pd.read_csv('D:/clg/mini proj/ssplat/articles.csv')
    source  = list(data['source.id'].unique())
    return jsonify({"sources":source })

@app.route('/authors', methods=['GET'])
def authors():
    data = pd.read_csv('D:/clg/mini proj/ssplat/articles.csv')
    author  = list(data['author'].unique())
    return jsonify({"sources":author })

@app.route('/searchbydate/<string:date>', methods=['GET'])
def searchbydate(date):
    data = pd.read_csv('D:/clg/mini proj/ssplat/articles.csv')
    mask  =  (data['publishedAt'] == date)
    results  = data[mask].to_json(orient="split")
    parsed = json.loads(results)
    
    return json.dumps(parsed, indent=4)

app.run()