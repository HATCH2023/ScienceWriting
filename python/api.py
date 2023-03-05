from flask import Flask, request, jsonify
from keywordSearch1 import searchScholarForKeywords
from scrapeNIH import getArticle

app = Flask(__name__)

@app.route('/python-api/articles')
def get_articles():
  keywords = request.args.get('keywords')
  index = request.args.get('index')
  articles = searchScholarForKeywords(keywords, int(index) if index != None else 0)
  return jsonify(articles)

@app.route('/python-api/article')
def get_article():
  url = request.args.get('url')
  article = getArticle(url)
  return jsonify(article)

if __name__ == '__main__':
  app.run()
