import smtplib
import imghdr
from email.message import EmailMessage
from datetime import datetime, timedelta
# change shipping to delivery 

dt = datetime.now()
prep_days = timedelta(days=7)
shipping_days = timedelta(days=14)
ship_out_date = dt + prep_days
arrival_date= dt + shipping_days

#testing accounts
swapout={"name":"swapout","email":"swapoutgoods@gmail.com"}
offeror={"name":"Customer_A","email":"12345678@gmail.com"}
receiver={"name":"Might Lee", "email": "mightlee123@gmail.com"}




#make offer
def email_offer(swapout,offeror, receiver):
    emsg=EmailMessage()
    emsg["Subject"] = f"Here is an trading offer from {offeror["name"]}."
    emsg["From"] = swapout["email"]
    emsg["To"] = receiver["email"]
    s= smtplib.SMTP("localhost")
    s.send_message(emsg)
    s.quit()

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
