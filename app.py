# app.py
from flask import Flask, render_template, request, jsonify
from search import perform_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_api():
    query = request.form['query']
    results = perform_search(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
