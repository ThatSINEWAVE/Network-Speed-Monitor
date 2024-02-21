# Network Speed Monitor

A Python-based tool for monitoring and logging your network's speed, utilizing the Speedtest CLI by Ookla. This local utility periodically checks your network's latency, download, and upload speeds, and logs the results for review.

## Features

- **Automated Speed Tests**: Utilizes the Speedtest CLI for accurate network speed measurements.
- **Configurable Intervals**: Set the interval between consecutive network speed tests.
- **Detailed Logging**: Maintains logs for different network types (Ethernet, Wi-Fi) to track performance over time.

## Prerequisites

- Python 3.x
- Speedtest CLI (Refer to the [Speedtest CLI documentation](https://www.speedtest.net/apps/cli) for installation instructions.)

## Installation

1. Ensure the Speedtest CLI is installed and accessible from your command line.
2. Clone this repository to your local machine.
3. Install any required Python dependencies (if specified).

## Usage

Execute `main_v2.py` to start the speed monitoring process. The script will perform network speed tests at the configured intervals and log the results in designated files.

```bash
python main_v2.py
```

##Logs
Speed test results are logged in the following files:
- `speedtest_log_Ethernet.txt` for Ethernet connections
- `speedtest_log_Wi-Fi.txt` for Wi-Fi connections

## Customization
Modify the `main_v2.py` script to adjust the target file type, test intervals, or other parameters according to your requirements.

## Disclaimer
This tool is for educational and testing purposes only. It showcases the capabilities of automating network speed tests using Python and the Speedtest CLI. The author is not liable for any misuse or for any network disruptions or damages caused by using this tool.

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute as needed.
