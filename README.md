# Advanced Linux IDS

## Overview
Advanced Linux IDS is a Python-based Intrusion Detection System (IDS) for Linux servers. It monitors login attempts via `/var/log/auth.log`, automatically blocks malicious IPs using UFW, and sends email alerts when an IP is blocked.  

Designed for **EC2, Ubuntu, or any Linux server**, with email alerts via Gmail SMTP.

---

## Features
- Monitors `/var/log/auth.log` for failed SSH login attempts.  
- Automatically blocks IPs after a configurable threshold using UFW.  
- Configurable block duration (temporary or permanent).  
- Sends email alerts to administrators when an IP is blocked.  
- Fully configurable via `config.py`.  
- Can run as a background service or via systemd.

---

