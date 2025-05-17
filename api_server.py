from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['POST'])
def fetch():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL belirtilmedi'}), 400

    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050',
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=15)
        return jsonify({'content': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
