from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

SERVERS = [
    {"id": 1, "name": "Flask App 1", "url": "http://10.0.143.32:5000", "ip": "10.0.143.32"},
    {"id": 2, "name": "Flask App 2", "url": "http://10.0.137.9:5000", "ip": "10.0.137.9"}
]

def check_status(url):
    try:
        # 2-second timeout to check reachability
        response = requests.get(url, timeout=2)
        return "REACHABLE" if response.status_code == 200 else "UNREACHABLE"
    except requests.exceptions.RequestException:
        return "UNREACHABLE"

@app.route('/')
def index():
    return render_template('index.html', servers=SERVERS)

@app.route('/api/recheck/<int:server_id>')
def recheck_individual(server_id):
    server = next((s for s in SERVERS if s['id'] == server_id), None)
    if not server:
        return jsonify({"error": "Server not found"}), 404
    
    status = check_status(server['url'])
    return jsonify({
        "id": server['id'],
        "status": status,
        "class": "online" if status == "REACHABLE" else "offline"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)