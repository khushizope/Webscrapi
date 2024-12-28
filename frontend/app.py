from flask import Flask, render_template, request, jsonify
from scraper import WebScraper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    scraper = WebScraper(url)
    data = scraper.scrape()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
