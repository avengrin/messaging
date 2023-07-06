import smtplib
from email.message import EmailMessage

# AV
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    user = env("EMAIL_HOST_USER")
    msg["from"] = env("EMAIL_FROM")
    password = env("EMAIL_HOST_PASSWORD")

    server = smtplib.SMTP(env("EMAIL_HOST"), env("EMAIL_PORT"))
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == "__main__":
    subject = "Predmet emailu"
    with open('body.txt', 'r') as f:
        body = f.read()
    to = "alexander.vengrin@gmail.com"
    email_alert(subject, body, to)


