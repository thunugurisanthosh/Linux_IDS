
#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from config import SENDER_EMAIL, ADMIN_EMAIL, SMTP_SERVER, SMTP_PORT

def send_alert(ip, reason="Multiple failed login attempts"):
    try:
        msg = MIMEText(f"IP {ip} blocked. Reason: {reason}")
        msg['Subject'] = 'Security Alert: Linux IDS'
        msg['From'] = SENDER_EMAIL
        msg['To'] = ADMIN_EMAIL

        s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        s.send_message(msg)
        s.quit()
        print(f"[ALERT] Email sent for blocked IP: {ip}")
    except Exception as e:
        print(f"[ERROR] Email alert failed: {e}")
