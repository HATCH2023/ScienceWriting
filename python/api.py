from flask import Flask, request
#import my_module # TODO: update this to be your python file
from keywordSearch1 import searchScholarForKeywords

app = Flask(__name__)

@app.route('/articles')
def get_articles():
  keywords = request.args.get('keywords')
  articles = searchScholarForKeywords(keywords, 0) # TODO: update this to be your function
  return articles

if __name__ == '__main__':
  app.run()
