import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_user = 'almanzar.angel03@gmail.com'
email_pass = ''
email_receiver = 'alonzosoto12k@gmail.com'
subject = 'Test'


msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_receiver
msg['Subject'] = subject 
body = 'Test Mail from Python'

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_pass)



server.sendmail(email_user,email_receiver,text)
server.quit()
