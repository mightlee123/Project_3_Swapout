# change shipping to delivery 
import os
from email.mime.text import MIMEText
import smtplib
from save_jpg_base64 import image_base64
from email.message import EmailMessage
from datetime import datetime, timedelta

#dates
dt = datetime.now()
prep_days = timedelta(days=7)
shipping_days = timedelta(days=14)
ship_out_date = dt + prep_days
arrival_date= dt + shipping_days

#swapout email account
swapout_email_address = os.environ.get("email_username")
swapout_email_password = os.environ.get("email_password")
#testing accounts
offeror={"name":"Customer_A" , "item":"Honda"}
receiver={"name":"Might Lee", "email": "mightlee123@gmail.com" , "item":"Toyota"}

#make offer
def email_offer(swapout_email_address, swapout_email_password, offeror, receiver):
    msg=EmailMessage()
    msg["Subject"] = "You Have an Offer!"
    msg["From"] = swapout_email_address
    msg["To"] = receiver["email"]

    #email content
    msg.set_content= (f"{offeror['name']} is wanting to trade your {receiver['item']} with a {offeror['item']}. Please accept the offer within 24 hours.")
    #html image
    msg.attach(MIMEText(f'<html><body><p><img src="data:image.jpg;base64,{image_base64}><p><body><html>, "html","utf-8"'))

    with smtplib.SMTP_SSL("smtp.gmail.com" , 465) as smtp:
        smtp.login(swapout_email_address , swapout_email_password)
        smtp.send_message(msg)
        smtp.quit()

email_offer


#offer denied
#def email_rejection(swapout, offeror, receiver):
#    emsg=EmailMessage()
#    emsg["Subject"] = f"{receiver.name} has turned down your offer"
#    emsg["From"] = swapout.email
#    emsg["To"] = offeror.email
#    s= smtplib.SMTP("localhost")
#    s.send_message(emsg)
#    s.quit()#

#offer accepted
#def email_instrustions(swapout, offeror, receiver, car_image, ship_out_date, arrival_date):
#    offeror_msg=EmailMessage()
#    offeror_msg["Subject"] = f"Your offer to {receiver.name} has been accepted. \
#                             Please ship your car to {receiver.shipping_address} by {ship_out_date}.\
#                             When you have received the car, click 'arrived',or else choose 'not received'"
#    offeror_msg["From"] = swapout
#    offeror_msg["To"] = offeror
#    s= smtplib.SMTP("localhost")
#    s.send_message(offeror_msg)
#    
#    reveiver_msg= EmailMessage()
#    reveiver_msg["Subject"] = f"Your offer to {offeror.name} has been accepted. \
#                             Please ship your car to {offeror.shipping_address} by {ship_out_date}.\
#                             When you have received the car, click 'arrived',or else choose 'not received'"
#    reveiver_msg["From"] = swapout
#    reveiver_msg["To"] = receiver
#    s= smtplib.SMTP("localhost")
#    s.send_message(reveiver_msg)
