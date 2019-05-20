#/usr/bin/python3
"""learning to automate email"""
import smtplib
import getpass

def main():
    content = "From:pythonstudent01@mail.com\r\nSubject:My emails have subject lines!\r\nThis is the last day of class"

        mail = smtplib.SMTP("smtp.mail.com", 587)

        mail.starttls()

        mail.login('phythonstudent01@mail.com', getpass.getpass("Enter your password: ")

        mail.sendmail('phythonstudent01@mail.com', 'rzfeeser@gmail.com',content)
        
        mail.quit()

main()

