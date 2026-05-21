# 🌐 Network Speed Monitor Dashboard

Advanced open-source network speed monitoring system developed with Python and Flask.

This project monitors internet performance continuously and provides:

- Real-time speed analytics
- Live dashboard
- Download / Upload monitoring
- Ping monitoring
- CSV data logging
- Automatic graph generation
- Outage detection

---

# 🚀 Features

## 📊 Live Dashboard

Modern Flask-based dashboard with:

- Real-time charts
- Average statistics
- Ping monitoring
- Outage detection
- Responsive UI

---

## 📈 Real-Time Graphs

The system automatically generates:

- Download speed graph
- Upload speed graph
- Ping graph

using Chart.js and Matplotlib.

---

## 💾 CSV Logging

All speed test results are automatically saved into:

```bash
speed_results.csv
```

Example:

| Time | Download | Upload | Ping |
|------|------|------|------|
| 10:00 | 35 Mbps | 12 Mbps | 45 ms |

---

## 🚨 Internet Outage Detection

If internet speed falls below threshold values,
the system detects potential outages automatically.

---

# 🛠 Technologies Used

- Python
- Flask
- Pandas
- Matplotlib
- Chart.js
- HTML/CSS
- CSV Logging

---

# 📂 Project Structure

```bash
Network-Speed-Monitor/
│
├── main_v2.py
├── web_dashboard.py
├── pdf_report.py
├── speed_results.csv
│
├── static/
│   ├── style.css
│   ├── speed_graph.png
│   └── ping_graph.png
│
├── templates/
│   └── dashboard.html
│
└── README.md
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/183195Se/Network-Speed-Monitor.git
```

Install dependencies:

```bash
pip install flask pandas matplotlib speedtest-cli
```

---

# ▶ Run Speed Monitor

```bash
python main_v2.py
```

---

# 🌐 Run Dashboard

```bash
python web_dashboard.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# 📸 Dashboard Preview

Add dashboard screenshots here.

Example:

```bash
screenshots/dashboard.png
```

---

# 🔥 Future Improvements

- Telegram notifications
- PDF reporting
- Multi-device monitoring
- Docker support
- Linux service integration

---

# 👨‍💻 Open Source Contribution

This project was improved as part of an open-source software contribution study.

Added features include:

- Advanced dashboard system
- Analytics monitoring
- Real-time chart updates
- CSV export support
- UI improvements

---

# 📄 License

MIT License