import imaplib
import email
from config import SMTP_SERVER, FROM_EMAIL, FROM_PWD

def read_email_from_gmail(content_email, subject):
    """ Reads the email using  a prescribed email 
    id and subject 
    """
    details = {}
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select('inbox')

    typ, data = mail.search(None, "From \"{}\" Subject \"{}\"".format(content_email, subject))
    mail_ids = data[0]
    id_list = mail_ids.split()
    for i in id_list:
        t, data = mail.fetch(i, '(RFC822)')
        for response in data:
            if isinstance(response, tuple):
                msg = email.message_from_string(response[1].decode('utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                print('Email found from :{} with subject :{}\n'.format(email_from, email_subject))
                for part in msg.walk():
                #find the attachment part
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                #save the attachment in the program directory
                    filename = part.get_filename()
                    fp = open(filename, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                    print('Attachment saved!, file: {}'.format(filename))
                    details[subject] = filename
    return details

""" Dummy test code """
# # subjects = read_email_from_gmail("animesh.mukherjeei323460@gmail.com","3765_ani")
# subjects = read_email_from_gmail("animesh.mukherjeei323460@gmail.com","327778_ani_mkjee")
# print(subjects)