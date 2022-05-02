import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "youcanical@gmail.com"
toaddr = "igoyal@olin.edu"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "EMAIL SUBJECT"

body = "EMAIL BODY"

msg.attach(MIMEText(body, 'plain'))

filepath = "test_icals/potato_test.ics" # make sure that the two file paths in this line
attachment = open(filepath, "rb") # and this line, match

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filepath)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "uehiuheiufhureihweui34297238974898hdioj3hui4wehdogwalkedthedock")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()