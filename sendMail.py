import smtplib
from config import FROM_EMAIL,FROM_PWD
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(from_user,to_user,subject,text,attachName):
    """
    Used to sent the email to a certain email ID and the attachm
    """
    assert isinstance(to_user, list)

    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = COMMASPACE.join(to_user)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    with open('./{}'.format(attachName), "rb") as fil:
        part = MIMEApplication(
                fil.read(),
                Name=basename('./{}'.format(attachName))
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename('./{}'.format(attachName))
        msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(FROM_EMAIL,FROM_PWD)
    server.sendmail(from_user,to_user,msg.as_string())
    server.quit()



# send_mail('anitoshri@gmail.com',['animesh.mukherjeei323460@gmail.com'],"Email Attachment test","Hi this is a dummy message to check if attachments work or not!!")