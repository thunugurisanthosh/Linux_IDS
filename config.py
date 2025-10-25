
# ----------------------------
# Linux IDS Configuration
# ----------------------------
LOG_FILE = "/var/log/auth.log"   # Path to auth log
THRESHOLD = 3                    # Failed attempts before block
BLOCK_DURATION = 3600            # Block duration in seconds (optional)
EMAIL_ALERT = True                # Enable email notifications

# Email settings
SENDER_EMAIL = "your_email@gmail.com"       # From address (must match SMTP_USER)
ADMIN_EMAIL = "your_email@gmail.com"        # Your inbox to receive alerts
SMTP_SERVER = "smtp.gmail.com"              # Gmail SMTP server
SMTP_PORT = 587                             # TLS port
SMTP_USER = "your_email@gmail.com"          # Your Gmail login
SMTP_PASS = "your_app_password"

# Log file for blocked IPs
BLOCK_LOG_FILE = "blocked_ips.log"
