
#!/usr/bin/env python3
import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alert import send_alert
import threading
from config import LOG_FILE, THRESHOLD, BLOCK_LOG_FILE, EMAIL_ALERT, BLOCK_DURATION

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ATTEMPTS = {}
BLOCKED_IPS = {}

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == LOG_FILE:
            try:
                with open(LOG_FILE, 'r') as f:
                    lines = f.readlines()[-50:]
                    for line in lines:
                        if "Failed password" in line or "authentication failure" in line:
                            parts = line.strip().split()
                            ip = parts[-4]
                            ATTEMPTS[ip] = ATTEMPTS.get(ip, 0) + 1

                            if ATTEMPTS[ip] >= THRESHOLD and ip not in BLOCKED_IPS:
                                os.system(f"sudo ufw deny from {ip}")
                                BLOCKED_IPS[ip] = time.time()
                                print(f"[BLOCKED] IP {ip} blocked after {THRESHOLD} failed attempts")

                                with open(BLOCK_LOG_FILE, 'a') as log:
                                    log.write(f"{time.ctime()} - Blocked IP: {ip}\n")

                                if EMAIL_ALERT:
                                    send_alert(ip)

                                ATTEMPTS[ip] = 0

                                if BLOCK_DURATION > 0:
                                    threading.Thread(target=unblock_ip_after_delay, args=(ip,)).start()
            except Exception as e:
                print(f"[ERROR] Failed to read log file: {e}")

def unblock_ip_after_delay(ip):
    time.sleep(BLOCK_DURATION)
    os.system(f"sudo ufw delete deny from {ip}")
    print(f"[INFO] IP {ip} automatically unblocked after {BLOCK_DURATION} seconds")
    with open(BLOCK_LOG_FILE, 'a') as log:
        log.write(f"{time.ctime()} - Unblocked IP: {ip}\n")
    BLOCKED_IPS.pop(ip, None)

if __name__ == "__main__":
    observer = Observer()
    event_handler = LogHandler()
    observer.schedule(event_handler, path="/var/log", recursive=False)
    observer.start()
    print("[INFO] Advanced Linux IDS started and monitoring auth.log...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[INFO] Linux IDS stopped by user.")
    observer.join()
