#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import re
import json
import smtplib
from email.message import EmailMessage


#lets start a Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to API Server"

@app.route("/upload")
def upload_file():
    return render_template("upload.html")

#make an API that allows for file attachments / /uploads
@app.route("/uploader", methods = ["GET", "POST"])
def uploader():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        #return "File successfully uploaded!"
        return redirect(url_for ("success"))
#after upload edirect to new API

#new API parses uploaded data and returns JSON

#snippet uploaded JSON from a packet trace (*pcap)

#use regex to.....

#sip:+17174608095@[938::38:123:0]:9130; other garbage; even more stuff

#every user (phone number) every IP (ipv6) ever port (9130)

@app.route("/success")
def success():
    sipjson = []
    with open("fakesip.log") as siplog:
        for line in siplog:
            sipobj = re.search(r"sip:\+(\d+)@\[(.*)\]:?(\d+)?", line)
            if sipobj:
                tinydancer = []
                tinydancer.append(sipobj.group())
                tinydancer.append(sipobj.group(1))
                tinydancer.append(sipobj.group(2))
                tinydancer.append(sipobj.group(3))
                sipjson.append(tinydancer)
        return json.dumps(sipjson)        
#build an API that sends an email
@app.route("email/sender")
def emailsender():
    msg.MIMEMultipart()
    msg.attach(MIMEImage(file("2019-05-17-outage.png").read()))

    with open("emailpassword.txt") as emailpass:
        myemailpass = emailpss.read()
        content = "From:pythonstudent01@mail.com\r\nSubject:My emails have subject lines!\r\nThis is the last day of class"
        mail = smtplib.SMTP("smtp.mail.com", 587)
        mail.starttls()
        mail.login('phythonstudent01@mail.com', myemailpass)
        mail.sendmail('phythonstudent01@mail.com', 'rzfeeser@gmail.com',content)
        mail.quit()
        return "SPAMMMM SENT!!!!"
if __name__ == '__main__':
    app.run(port = 9107)

