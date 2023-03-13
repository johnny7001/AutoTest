from email.mime.text import MIMEText
import smtplib

# SMTP
account = "theforeverwen@gmail.com"
password = "zlyxvgqvawbsgljt"

# 收信寄信人的資料
to_email = "johnnytseng7001@gmail.com"
from_email = "theforeverwen@gmail.com"

# MIME
subject = "測試信件"
message = "哈囉可以了嗎"
msg = MIMEText(message, "html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email

# 寄信
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)
server.send_message(msg)
server.quit()
