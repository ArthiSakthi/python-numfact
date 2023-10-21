from flask import Flask, render_template, request, jsonify
import requests
from flask_caching import Cache

app = Flask(__name__)
cache=Cache(app)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/number_fact', methods=['POST'])
@cache.cached(timeout=300)
def number_fact():
    try:
        api_url = (f'http://numbersapi.com/random/math')
        response = requests.get(api_url)
        if response.status_code == 200:
            fact = response.text
            return render_template('result.html', fact=fact)
        else:
            return render_template('error.html', error='Failed to fetch number fact.')
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

