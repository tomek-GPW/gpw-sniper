import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header

def send_email(subject: str, body: str) -> None:
    to_email = os.environ["ALERT_TO_EMAIL"]
    from_email = os.environ["ALERT_FROM_EMAIL"]
    user = os.environ["GMAIL_SMTP_USER"]
    app_pass = os.environ["GMAIL_SMTP_APP_PASSWORD"]

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user, app_pass)
        smtp.sendmail(from_email, [to_email], msg.as_string())

if __name__ == "__main__":
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    subject = f"GPW SNIPER TEST — {now}"
    body = (
        "To jest mail testowy z Render.\n\n"
        "Jeśli to widzisz, kanał powiadomień działa.\n"
        "Następny krok: podpinamy dane i logikę setupów.\n"
    )
    send_email(subject, body)
    print("OK: mail wysłany")
