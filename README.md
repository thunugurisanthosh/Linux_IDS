#  Linux Security & Intrusion Detection System (IDS)

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


<img width="1920" height="506" alt="Screenshot (97)" src="https://github.com/user-attachments/assets/c149effa-1a7e-4b49-9a8d-09f69ef8ff85" />

<img width="1920" height="838" alt="Screenshot (98)" src="https://github.com/user-attachments/assets/2fca171c-e398-42b5-ba65-e3590bff3321" />
<img width="1872" height="282" alt="Screenshot (99)" src="https://github.com/user-attachments/assets/4b9bcc90-0c95-4afb-8971-de162950c36d" />
<img width="1889" height="120" alt="Screenshot (100)" src="https://github.com/user-attachments/assets/e2bdef5a-023f-403f-b97d-c19cba145b3e" />
<img width="1852" height="776" alt="Screenshot (101)" src="https://github.com/user-attachments/assets/40995b07-8489-4fb0-b19c-1c482cb6e437" />
