import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "iotcti2020@gmail.com" # the email where you sent the email
password = "Faisal0720"
send_to_email = "fkalyousefi@gmail.com" # for whom
subject = "Gmail"
message = "This is a test email sent by Python. Isn't that cool?!"

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = send_to_email
msg["Subject"] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()