#!/usr/bin/python3
import schedule
import time
import GetEmailText
import SendEmail

def GetEmailTextJob():
    GetEmailText.BuildHtmlEmailText();


def SendEmailJob():
    SendEmail.send_mail();





if __name__ =="__main__":

    schedule.every().day.at("14:25").do(GetEmailTextJob)
    schedule.every().day.at("14:30").do(SendEmailJob)

    while True:
        schedule.run_pending()
        time.sleep(1)