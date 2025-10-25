
# ----------------------------
# Linux IDS Configuration
# ----------------------------
LOG_FILE = "/var/log/auth.log"   # Path to auth log
THRESHOLD = 3                    # Failed attempts before block
BLOCK_DURATION = 3600            # Block duration in seconds (optional)
EMAIL_ALERT = True                # Enable email notifications

# Email settings
SENDER_EMAIL = "admin@example.com"
ADMIN_EMAIL = "your_email@example.com"
SMTP_SERVER = "localhost"
SMTP_PORT = 25

# Log file for blocked IPs
BLOCK_LOG_FILE = "blocked_ips.log"
