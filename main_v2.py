import subprocess
import time
import datetime
import os
import json

# List of network interfaces, replace with your actual interface names
network_interfaces = ["Ethernet", "Wi-Fi"]


def run_speedtest(interface):
    # Path to the speedtest executable
    speedtest_executable = os.path.join(os.getcwd(), "speedtest", "speedtest.exe")

    print(f"Starting Speedtest on interface: {interface}...")

    # Command to run the Speedtest CLI with the specified interface
    command = [speedtest_executable, "--interface", "Interface-Name", "-f", "json"]

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Parse the JSON output
    try:
        data = json.loads(result.stdout)

        # Extract detailed metrics
        server_name = data["server"]["name"]
        server_location = data["server"]["location"]
        server_country = data["server"]["country"]
        client_ip = data["interface"]["externalIp"]
        client_isp = data["isp"]
        download_speed = data["download"]["bandwidth"] * 8 / 1_000_000  # Convert to Mbps
        upload_speed = data["upload"]["bandwidth"] * 8 / 1_000_000  # Convert to Mbps
        latency = data["ping"]["latency"]
        jitter = data["ping"]["jitter"]
        packet_loss = data.get("packetLoss", 0)  # Default to 0 if not available

        # Format the results
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_text = (
            f"Time: {current_time}\n"
            f"Interface: {interface}\n"
            f"Server: {server_name}, {server_location}, {server_country}\n"
            f"Client IP: {client_ip}\n"
            f"ISP: {client_isp}\n"
            f"Download Speed: {download_speed:.2f} Mbps\n"
            f"Upload Speed: {upload_speed:.2f} Mbps\n"
            f"Latency: {latency} ms\n"
            f"Jitter: {jitter} ms\n"
            f"Packet Loss: {packet_loss}%\n"
        )

        print("Speedtest completed successfully.")

    except json.JSONDecodeError:
        result_text = f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nError: Unable to parse Speedtest results\n"
        print("Error: Unable to parse Speedtest results.")

    # Log the output to a file
    with open(f"speedtest_log_{interface}.txt", "a") as file:
        file.write(result_text + "\n")


# Interval (in seconds)
interval = 300  # 5 minutes

# Loop for tests on each interface
while True:
    for interface in network_interfaces:
        run_speedtest(interface)
        print(f"Completed test on {interface}. Waiting {interval / 60} minutes for the next test...")
        time.sleep(interval)
