from flask import Flask, request
from keywordSearch1 import searchScholarForKeywords

app = Flask(__name__)

@app.route('/articles')
def get_articles():
  keywords = request.args.get('keywords')
  index = request.args.get('index')
  articles = searchScholarForKeywords(keywords, int(index) if index != None else 0)
  return articles

if __name__ == '__main__':
  app.run()
