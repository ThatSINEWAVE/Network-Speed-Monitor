import subprocess
import time
import datetime
import os
import json
import csv
import matplotlib.pyplot as plt

# Network interfaces
network_interfaces = ["Ethernet", "Wi-Fi"]

# CSV file
csv_file = "speed_results.csv"


# CSV yoksa oluştur
if not os.path.isfile(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "time",
            "interface",
            "download_mbps",
            "upload_mbps",
            "latency_ms",
            "isp",
            "server"
        ])


def generate_graph():

    times = []
    download = []
    upload = []

    try:
        with open(csv_file, "r") as f:

            reader = csv.DictReader(f)

            for row in reader:

                try:
                    times.append(row["time"])
                    download.append(float(row["download_mbps"]))
                    upload.append(float(row["upload_mbps"]))
                except:
                    continue

        if len(times) == 0:
            return

        plt.figure()

        plt.plot(download, label="Download Mbps")
        plt.plot(upload, label="Upload Mbps")

        plt.xlabel("Test Number")
        plt.ylabel("Speed (Mbps)")
        plt.title("Internet Speed Monitor")

        plt.legend()
        plt.tight_layout()

        plt.savefig("speed_graph.png")

        plt.close()

        print("Graph updated: speed_graph.png")

    except Exception as e:
        print("Graph generation error:", e)


def run_speedtest(interface):

    print(f"Starting Speedtest on interface: {interface}...")

    command = ["python", "-m", "speedtest", "--json"]

    result = subprocess.run(command, capture_output=True, text=True)

    try:

        if result.stdout.strip() == "":
            raise Exception("Speedtest output empty")

        data = json.loads(result.stdout)

        server_name = data.get("server", {}).get("name", "Unknown")
        server_country = data.get("server", {}).get("country", "Unknown")

        client_ip = data.get("client", {}).get("ip", "Unknown")
        client_isp = data.get("client", {}).get("isp", "Unknown")

        download_speed = data.get("download", 0) / 1_000_000
        upload_speed = data.get("upload", 0) / 1_000_000

        latency = data.get("ping", 0)

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result_text = (
            f"Time: {current_time}\n"
            f"Interface: {interface}\n"
            f"Server: {server_name}, {server_country}\n"
            f"Client IP: {client_ip}\n"
            f"ISP: {client_isp}\n"
            f"Download Speed: {download_speed:.2f} Mbps\n"
            f"Upload Speed: {upload_speed:.2f} Mbps\n"
            f"Latency: {latency} ms\n"
        )

        print(result_text)

        # CSV kayıt
        with open(csv_file, "a", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                current_time,
                interface,
                round(download_speed, 2),
                round(upload_speed, 2),
                round(latency, 2),
                client_isp,
                server_name
            ])

        # Grafik üret
        generate_graph()

    except Exception as e:

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result_text = (
            f"Time: {current_time}\n"
            f"Interface: {interface}\n"
            f"Error: {str(e)}\n"
        )

        print("Error while parsing Speedtest results:", e)

    # TXT log
    with open(f"speedtest_log_{interface}.txt", "a") as file:
        file.write(result_text + "\n")


# Test interval (5 dakika)
interval = 300


while True:

    for interface in network_interfaces:

        run_speedtest(interface)

        print(f"Completed test on {interface}")
        print(f"Waiting {interval/60} minutes...\n")

        time.sleep(interval)