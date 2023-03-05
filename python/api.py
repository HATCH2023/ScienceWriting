from flask import Flask, request, jsonify
from keywordSearch1 import searchScholarForKeywords
from summarize import generate_summary, generate_Chad_Social, generate_Chad_Dalle
from scrapeNIH import getArticle
from generateDalleImage4 import generateDalleImage
from facebookPhoto3 import uploadImageToFacebook
from instagramPost3 import uploadImageToInstagram
from twitterUploadImage3 import uploadTweetWithImage
from linkedInFullImagePost3 import uploadImageToLinkedIn

app = Flask(__name__)

@app.route('/python-api/articles')
def get_articles():
  keywords = request.args.get('keywords')
  index = request.args.get('index')
  articles = searchScholarForKeywords(keywords, int(index) if index != None else 0)
  return jsonify(articles)

@app.route('/python-api/summarize')
def get_article():
  url = request.args.get('url')
  article = getArticle(url)['article']
  summary = generate_summary(article)
  return jsonify(summary)

@app.route('/python-api/platformContent', methods=['POST'])
def get_platform_content():
  summary = request.json['summary']
  platform_content = generate_Chad_Social(summary)
  return jsonify(platform_content)

@app.route('/python-api/getImages', methods=['POST'])
def get_images():
  summary = request.json['summary']
  dallePrompt = generate_Chad_Dalle(summary) # string
  images = generateDalleImage(dallePrompt)
  return jsonify(images)

@app.route('/python-api/postFacebook', methods=['POST'])
def post_facebook():
  path = request.json['path']
  caption = request.json['caption']
  uploadImageToFacebook(path, caption)
  return "good boy"

@app.route("/python-api/postInstagram", methods=['POST'])
def post_instagram():
  path = request.json['path']
  caption = request.json['caption']
  uploadImageToInstagram(path, caption)
  return "good boy"

@app.route("/python-api/postLinkedIn", methods=['POST'])
def post_linkedin():
  path = request.json['path']
  caption = request.json['caption']
  uploadImageToLinkedIn(path, caption)
  return "good boy"

@app.route("/python-api/postTwitter", methods=['POST'])
def post_twitter():
  path = request.json['path']
  caption = request.json['caption']
  uploadTweetWithImage(path, caption)
  return "good boy"

if __name__ == '__main__':
  app.run()
