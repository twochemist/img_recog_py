'''
this file sends an email from the raspberry pi
Email contains a picture taken by the raspi camera module

main function "sendpic()" takes 1 input -> name. This name must be an existing
jpg file in the same folder where email is located.
'''

import email, smtplib, ssl, getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# the following code executes for all functions

# get current time for timestamp
now = datetime.now()

# define subject for the
subject = 'Raspi Picture taken at '+ datetime.now().strftime("%H:%M hrs on %Y-%m-%d")
body = "Here is the picture you just took using the raspi camera module!"
sender_email = "fidelignacio21@gmail.com"    # Enter your address
receiver_email = "fidelignacio21@gmail.com"  # Enter receiver address
password = '1windsurfing'
#password = getpass.getpass("Type your password and press enter: ") # Password is enter in hidden view

def sendpic(name):

    try:
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # attach the photo just taken
        filename = name+'.jpg'

        # Open JPG file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part

        # NOTE this has been changed for raspi, because the python3.5 it runs does not support f"strings..."
        # Instead, the format was changed to "string {}".format(variable)
        part.add_header(
            "Content-Disposition",
            "attachment; filename= {}".format(filename),
            )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()

        # Trying to write without the with statement
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        '''
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            server.close()
            '''
        print('omission successful')

    except:
        print('an error occurred')
