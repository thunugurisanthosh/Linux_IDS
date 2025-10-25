#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from config import SENDER_EMAIL, ADMIN_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS

def send_alert(ip, reason="Multiple failed login attempts"):
    try:
        msg = MIMEText(f"IP {ip} blocked. Reason: {reason}")
        msg['Subject'] = 'Security Alert: Linux IDS'
        msg['From'] = SENDER_EMAIL
        msg['To'] = ADMIN_EMAIL

        # Connect to Gmail SMTP with TLS
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()              # Identify yourself to the server
        server.starttls()          # Start TLS encryption
        server.ehlo()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
        server.quit()

        print(f"[ALERT] Email sent for blocked IP: {ip}")

    except Exception as e:
        print(f"[ERROR] Email alert failed: {e}")
