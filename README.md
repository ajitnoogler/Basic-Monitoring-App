Here is a professional **README.md** for your Flask Server Monitor application. It covers the setup, the logic behind the health checks, and how to deploy it on your EC2 instance.

---

# 🚀 flaskctrl: Server Health Dashboard

A lightweight, independent Flask application designed to monitor the reachability of multiple backend servers. It features a clean, cream-themed UI with real-time "ping" status and individual recheck capabilities.

## 📋 Features

* **Dual-Server Monitoring**: Specifically configured to track `http://10.0.143.32:5000` and `http://10.0.137.9:5000`.
* **Real-Time Status**: Uses the Python `requests` library to verify connectivity directly from the server-side.
* **Individual Rechecks**: Each server card has its own "RECHECK" button to trigger an isolated health check via API.
* **Auto-Refresh**: Automatically pings all configured servers every 10 seconds.
* **System Logs**: A console-style display showing recent connectivity events.

## 📂 Project Structure

```text
monitoring-app/
├── monitoring.py        # Main Flask application logic
├── requirements.txt     # Python dependencies
└── templates/
    └── index.html       # Dashboard UI (themed)

```

## ⚙️ Installation & Setup

### 1. Prepare your Environment

Ensure you have Python 3.9+ installed on your EC2 instance.

### 2. Install Dependencies

Install the required libraries using the provided `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 3. Configure Security Groups

Since your apps are running on port **5000**, ensure your AWS Security Group allows:

* **Inbound TCP 5000**: From the Monitoring Server to the target EC2 instances.
* **Inbound TCP 8080**: To access this monitoring dashboard from your browser.

## 🚀 Running the App

Start the monitoring service from your project root:

```bash
python3 monitoring.py

```

Access the dashboard in your browser at: `http://<YOUR-EC2-PUBLIC-IP>:8080`.

## 🛠️ Troubleshooting

If a server shows **UNREACHABLE** even when it is running:

* **Check Binding**: Ensure the target Flask app is bound to `0.0.0.0`, not `127.0.0.1`.
* **Check Nginx**: If Nginx can reach the app but the monitor cannot, verify that the monitor is using the correct internal IP or hostname.
* **Headers**: The monitor is configured to send `Connection: close` to prevent socket hanging on Werkzeug servers.

---

## 📄 License

MIT License - Feel free to use and modify for your infrastructure.
