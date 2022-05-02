import smtplib

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "youcanical@gmail.com"  # Enter your address
receiver_email = "igoyal@olin.edu"  # Enter receiver address
password = 'uehiuheiufhureihweui34297238974898hdioj3hui4wehdogwalkedthedock'
message = """\
Subject: Hi there

This message is sent from sea potatoes."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    print("It worked")
    server.sendmail(sender_email, receiver_email, message)
