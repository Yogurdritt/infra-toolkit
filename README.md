# Infra Toolkit

A lightweight command-line toolkit written in Python that provides common infrastructure and networking utilities. This project was built as a hands-on learning exercise to strengthen Python programming, Git workflows, and networking fundamentals while creating a practical portfolio project.

---

## Features

### DNS Lookup

Query DNS records for a given domain.

Supported record types:

* A
* AAAA
* CNAME
* MX
* NS
* TXT
* SOA

You can query either a specific record type or all supported records at once.

---

### PTR Record Lookup (Reverse DNS)

Perform reverse DNS lookups by providing an IPv4 address and retrieving its associated hostname, if one exists.

---

### ICMP IPv4 Ping

Send ICMP Echo Requests to an IPv4 address or hostname and display the result.

The tool validates IPv4 addresses before performing the request and reports common connectivity errors.

---

### ICMP IPv4 Traceroute

Trace the route taken by packets to an IPv4 address or hostname.

On Windows, the tool uses the native `tracert` utility.

On Linux, it uses the native `traceroute` command.

---

## Project Structure

```text
infra-toolkit/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tools/
    ├── __init__.py
    ├── dns_tools.py
    └── icmp_tools.py
```

---

## Requirements

* Python 3.10 or newer
* Internet connection
* Administrator/root privileges may be required for some ICMP operations depending on the operating system.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Yogurdritt/infra-toolkit.git
```

Move into the project directory:

```bash
cd infra-toolkit
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Start the application with:

```bash
python main.py
```

---

## Example Menu

```text
====================
Infra Toolkit
====================

Available tools:

1. DNS Lookup
2. PTR Record Lookup (Reverse DNS)
3. ICMP IPv4 Ping
4. ICMP IPv4 Traceroute
```

---

## Dependencies

* dnspython
* icmplib

---

## Technologies

* Python
* Git
* GitHub
* DNS
* ICMP
* CLI Applications

---

## Purpose

This project was developed as part of my infrastructure engineering portfolio. Its primary goal is to strengthen practical skills in:

* Python programming
* Networking fundamentals
* DNS operations
* ICMP diagnostics
* Software modularization
* Exception handling
* Git version control and branching workflows

Rather than implementing networking protocols from scratch, the project focuses on building a clean, maintainable command-line application using industry-standard Python libraries and development practices.

---

## Future Improvements

Potential future additions include:

* WHOIS lookups
* Port scanner
* HTTP/HTTPS requests
* SSL/TLS certificate inspection
* JSON output mode
* Logging support
* Configuration file support

---

## License

This project is intended for educational and portfolio purposes.
