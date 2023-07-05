import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = 'your_email@example.com'
receiver_email = 'recipient_email@example.com'
subject = 'Hello from Python'
message = 'This is a test email sent using Python.'

# Create the email message
msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# SMTP server details
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'

# Create an SMTP connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully.')
