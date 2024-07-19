# Python Port Scanner

This Python script is a simple yet effective port scanner that allows you to check for open ports on a specified target. The script resolves both IP addresses and hostnames, performs banner grabbing to gather information about the services running on open ports, and can scan a range of ports for multiple targets.

## Features

- Resolves IP addresses and hostnames.
- Scans a range of ports for open ports.
- Performs banner grabbing to gather information about services running on open ports.
- Allows scanning of multiple targets.

## Requirements

- Python 3.x
- IPy module (`pip install IPy`)

## Usage

### As a Script

1. Save the script as `portscanner.py`.
2. Run the script from the command line:

```bash
python portscanner.py
```

3. Enter the target(s) to scan when prompted. Separate multiple targets with spaces.

```plaintext
[+] Enter target/s to scan (separate targets with space): example.com 192.168.1.1
```

## Code Explanation

### Import Libraries

```python
from IPy import IP
import socket
```

### Check IP or Resolve Hostname

```python
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)
```

- `check_ip(ip)`: Checks if the input is an IP address. If not, it resolves the hostname to an IP address.

### Banner Grabbing

```python
def get_banner(s):
    return s.recv(1024)
```

- `get_banner(s)`: Receives up to 1024 bytes of data from the socket to gather service information.

### Scan a Specific Port

```python
def scan_port(ipaddr, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddr, port))
        try:
            banner = get_banner(sock)
            print("[+] Open Port " + str(port) + " : " + str(banner.decode()))
        except:
            print("[+] Open Port " + str(port))
    except:
        pass
```

- `scan_port(ipaddr, port)`: Tries to connect to the specified port. If successful, it attempts to grab the banner and print information about the service.

### Scan a Range of Ports on a Target

```python
def scan(target):
    converted_ip = check_ip(target)
    for port in range(1, 1000):
        scan_port(converted_ip, port)
```

- `scan(target)`: Scans ports 1 to 999 on the given target.

### Main Function

```python
if __name__ == "__main__":
    targets = input("[+] Enter target/s to scan (separate targets with space) ")
    for ipaddr in targets.split(" "):
        converted_ip = check_ip(ipaddr)
        print("[ 0 - Scanning ] " + str(ipaddr))
        for port in range(1, 85):
            scan_port(converted_ip, port)
```

- When run directly, the script prompts for targets, resolves them, and scans ports 1 to 84 on each target.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
