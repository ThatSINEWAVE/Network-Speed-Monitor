from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

CSV_FILE = "speed_results.csv"


def calculate_stats():

    if not os.path.exists(CSV_FILE):
        return {}

    df = pd.read_csv(CSV_FILE, encoding="latin1")

    stats = {}

    stats["avg_download"] = round(df["download_mbps"].mean(), 2)
    stats["avg_upload"] = round(df["upload_mbps"].mean(), 2)
    stats["avg_ping"] = round(df["latency_ms"].mean(), 2)

    outages = df[df["download_mbps"] < 1]
    stats["outage_count"] = len(outages)

    return stats


@app.route("/data")
def data():

    if not os.path.exists(CSV_FILE):
        return jsonify({})

    df = pd.read_csv(CSV_FILE, encoding="latin1")

    df = df.tail(20)

    return jsonify({
        "time": df["time"].tolist(),
        "download": df["download_mbps"].tolist(),
        "upload": df["upload_mbps"].tolist(),
        "ping": df["latency_ms"].tolist()
    })


@app.route("/")
def index():

    stats = calculate_stats()

    html = f"""
    <html>

    <head>

    <title>Network Speed Dashboard</title>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>

    * {{
        margin:0;
        padding:0;
        box-sizing:border-box;
    }}

    body {{
        background: #0f172a;
        color: white;
        font-family: Arial;
        padding: 30px;
    }}

    h1 {{
        text-align:center;
        margin-bottom:30px;
        font-size:40px;
    }}

    .stats {{
        display:grid;
        grid-template-columns: repeat(auto-fit, minmax(220px,1fr));
        gap:20px;
        margin-bottom:40px;
    }}

    .card {{
        background:#1e293b;
        padding:25px;
        border-radius:18px;
        text-align:center;
        box-shadow:0px 0px 20px rgba(0,0,0,0.4);
        transition:0.3s;
    }}

    .card:hover {{
        transform:translateY(-5px);
        box-shadow:0px 0px 25px rgba(59,130,246,0.5);
    }}

    .card h3 {{
        margin-bottom:15px;
        color:#93c5fd;
    }}

    .card p {{
        font-size:28px;
        font-weight:bold;
    }}

    .graph-container {{
        background:#1e293b;
        padding:25px;
        border-radius:18px;
        margin-bottom:30px;
        box-shadow:0px 0px 20px rgba(0,0,0,0.4);
    }}

    canvas {{
        width:100% !important;
        height:350px !important;
    }}

    .footer {{
        text-align:center;
        margin-top:30px;
        color:gray;
    }}

    </style>

    </head>

    <body>

    <h1>🌐 Network Speed Dashboard</h1>

    <div class="stats">

        <div class="card">
            <h3>⬇ Avg Download</h3>
            <p>{stats.get("avg_download","-")} Mbps</p>
        </div>

        <div class="card">
            <h3>⬆ Avg Upload</h3>
            <p>{stats.get("avg_upload","-")} Mbps</p>
        </div>

        <div class="card">
            <h3>📡 Avg Ping</h3>
            <p>{stats.get("avg_ping","-")} ms</p>
        </div>

        <div class="card">
            <h3>🚨 Outages</h3>
            <p>{stats.get("outage_count","0")}</p>
        </div>

    </div>


    <div class="graph-container">
        <h2>📈 Speed Monitor</h2>
        <canvas id="speedChart"></canvas>
    </div>

    <div class="graph-container">
        <h2>📶 Ping Monitor</h2>
        <canvas id="pingChart"></canvas>
    </div>

    <div class="footer">
        Network Speed Monitor Dashboard
    </div>


<script>

let speedChart
let pingChart

async function loadData() {{

    const response = await fetch('/data')
    const data = await response.json()

    if(!speedChart){{

        const ctx = document.getElementById('speedChart').getContext('2d')

        speedChart = new Chart(ctx, {{

            type: 'line',

            data: {{
                labels: data.time,
                datasets: [
                    {{
                        label: 'Download Mbps',
                        data: data.download,
                        tension:0.4
                    }},
                    {{
                        label: 'Upload Mbps',
                        data: data.upload,
                        tension:0.4
                    }}
                ]
            }},

            options:{{
                responsive:true,
                maintainAspectRatio:false
            }}

        }})
    }}
    else{{

        speedChart.data.labels = data.time
        speedChart.data.datasets[0].data = data.download
        speedChart.data.datasets[1].data = data.upload
        speedChart.update()

    }}


    if(!pingChart){{

        const ctx2 = document.getElementById('pingChart').getContext('2d')

        pingChart = new Chart(ctx2, {{

            type: 'line',

            data: {{
                labels: data.time,
                datasets: [
                    {{
                        label: 'Ping ms',
                        data: data.ping,
                        tension:0.4
                    }}
                ]
            }},

            options:{{
                responsive:true,
                maintainAspectRatio:false
            }}

        }})

    }}
    else{{

        pingChart.data.labels = data.time
        pingChart.data.datasets[0].data = data.ping
        pingChart.update()

    }}

}}

loadData()

setInterval(loadData, 5000)

</script>

</body>
</html>
"""

    return html


if __name__ == "__main__":
    app.run(debug=True)