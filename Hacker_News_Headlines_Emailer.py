import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # Carica .env automaticamente


now = datetime.datetime.now()

content = ""

def extract_news(url):
    print("Extracting Hacker News Stories...")
    cnt = ""
    cnt += ("<b>HN Top Stories:</b>\n" + "<br>" + '-'*50 + "<br>")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    for i, tag in enumerate(soup.find_all("span", attrs={"class":"titleline"})):
        href = tag.a.get("href")
        cnt += ((str(i+1)+' :: '+tag.text + ' ' + 'link: ' + href + '\n' + '<br>') if tag.text != 'More' else "" )
    return cnt
cnt = extract_news("https://news.ycombinator.com/")
content += cnt
content += ("<br>------<br>")
content += ("<br><br>End of Message")

print("Composing Email...")

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = os.getenv('email')
TO = os.getenv('email')
APP_PASS = os.getenv('password')

msg = MIMEMultipart()
msg['Subject'] = 'Top News Stories HN [Automated Email]' + " " + str(now.day) + "-" + str(now.month) + "-" + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print("Sending Email...")
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, APP_PASS)
server.sendmail(FROM, TO, msg.as_string())
print("Email Sent...")
server.quit()
