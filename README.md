TCP Port Scanner :-

A multi-threaded TCP port scanner built using Python for fast and efficient network scanning and service detection.

# Overview

This project is a Python-based TCP port scanner that allows users to identify open ports on a target system. It uses socket
programming and multi-threading to perform fast scans and includes banner grabbing for basic service identification.
Port scanning is a fundamental technique in cybersecurity used to discover open services running on a system, which may 
expose potential vulnerabilities.

# Features

* Multi-threaded scanning for improved performance
* Scans TCP ports on a target host
* Detects open ports
* Banner grabbing for service detection
* Simple command-line interface
* Lightweight and easy to use

# Technologies Used

* Python 3
* socket module
* threading module

# Project Structure

```bash
TCP-Port-Scanner/
│── port_scanner.py
│── README.md
```

# Installation

Clone the repository:

```bash
git clone https://github.com/karanrajput15432-hub/TCP-Port-Scanner.git
cd TCP-Port-Scanner
```

# Usage

Run the script:

```bash
python port_scanner.py
```

Enter the target IP address or domain when prompted.

# Example

* Target: scanme.nmap.org
* Output: Displays open ports and detected services

# Disclaimer

This project is intended for educational purposes only.
Unauthorized scanning of networks may be illegal. Always ensure you have proper permission before scanning any system.

# Future Improvements

* Add UDP port scanning
* Add graphical user interface (GUI)

