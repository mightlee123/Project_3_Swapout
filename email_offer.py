import smtplib
from email.mime.text import MIMEText
from save_jpg_base64 import image
import os
import config

#swapout email account
#swapout_email_address = os.environ.get("email_username")
#swapout_email_password = os.environ.get("email_password")

offeror={"name":"Customer_A" , "item":"Honda"}
receiver={"name":"Might Lee", "email": "mightlee123@gmail.com" , "item":"Toyota"}
youtube_link= "https://www.youtube.com/watch?v=JRCJ6RtE3xU&t=1497s"
def email_offer(subject, msg):
    #try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(config.email_username, config.email_password)
        message = 'Subject:{}\n\n{}'.format(subject,msg)
        server.sendmail(config.email_username, "mightlee123@gmail.com", message )
        server.quit()
        #print("True")
    #except:
        #print("False")


subject="You Have an Offer!"
msg = f"{offeror['name']} is wanting to trade your {receiver['item']} with a {offeror['item']}.\
        Please accept the offer within 24 hours.\n {youtube_link}"
#picture
#msg.attach(MIMEText("data:image.jpg;base64,{image}><p><body><html>", "html","utf-8"))

email_offer(subject,msg)
