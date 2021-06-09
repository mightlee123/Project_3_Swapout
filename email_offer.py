import smtplib
from email.mime.text import MIMEText
from save_jpg_base64 import image
import os
from datetime import datetime, timedelta
#date 
dt = datetime.now()
prep_days = timedelta(days=7)
shipping_days = timedelta(days=14)
ship_out_date = dt + prep_days
arrival_date= dt + shipping_days

#swapout email account
swapout_email_address = os.environ.get("email_username")
swapout_email_password = os.environ.get("email_password")

offeror={"name":"Customer_A" , "item":"Honda"}
receiver={"name":"Might Lee", "email": "mightlee123@gmail.com" , "item":"Toyota"}
def email_notification(subject, msg, user_email):
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(swapout_email_address, swapout_email_password)
    message = 'Subject:{}\n\n{}'.format(subject,msg)
    server.sendmail(swapout_email_address, user_email, message )
    server.quit()

def make_offer(offeror, receiver):
    user_email = receiver["mail"]
    subject = "You Have an Offer!"
    msg = f"{offeror['name']} is wanting to trade your {receiver['item']} with a {offeror['item']}.\
        Please accept the offer within 24 hours."
    email_notification(subject, msg, user_email)
#picture
#msg.attach(MIMEText("data:image.jpg;base64,{image}><p><body><html>", "html","utf-8"))

def reject_offer(offeror, receiver):
    user_email = offeror["email"]
    subject = "Offer Denied"
    msg = f"Your trade offer for {receiver['name']}'s {receiver['Item']}has been turned down."
    email_notification(subject, msg, user_email)

#trade confirmation email to offeror
def trade_confirmation_1(offeror,receiver):
    user_email = offeror["email"]
    subject = "Confirm Trade"
    msg = f"Your offer has been accepted! Please deliver your vehicle before {ship_out_date}\
         to the following address: {receiver['address']}."
    email_notification(subject, msg, user_email)

#trade confirmation email to receiver
def trade_confirmation_2(offeror, receiver):
    user_email = receiver["email"]
    subject = "confirm Trade"
    msg = f"You got yourself a deal! Please deliver your vehicle before {ship_out_date}\
         to the following address: {offeror['address']}."
    email_notification(subject, msg, user_email)

