# -*- coding: utf-8 -*-
import cv2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


sender_email = "iotcti2020@gmail.com"
receiver_email = "fkalyousefi@gmail.com"
password = 'Faisal0720'

message = MIMEMultipart("alternative")
message["Subject"] = "تمت ملاحظة شخص"
message["From"] = sender_email
message["To"] = receiver_email


def send_gmail(filename):

  attachment = filename

  # msgText = MIMEText('<b>Body</b><br><img src="cid:%s"><br>' % (attachment), 'html')  
  # msg.attach(msgText)


  # Create the plain-text and HTML version of your message
  text = """\
    """
  html = """\
  <html dir="rtl">
    <body>
      <p>هام: <br>
      وجدنا شخصًا بالقرب من الكاميرا<br>
      <br>
         <br><img src="cid:image.png"><br>
      </p>
    </body>
  </html>
  """

  fp = open(attachment, 'rb')                                                    
  img = MIMEImage(fp.read())
  fp.close()
  img.add_header('Content-ID', '<{}>'.format(attachment))
  # msg.attach(img)


  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)
  message.attach(img)

  # Create secure connection with server and send email
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login(sender_email,password)
  server.sendmail(sender_email, receiver_email, message.as_string())
  server.quit()