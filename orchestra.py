from readMail import *
from config import FROM_EMAIL,EXCEL_CONFIG,CONTENT_EMAIL,LOGO
from excel_manager import *
from sendMail import *
from pdf_gen import *

excel_dict = read_pdf_in(EXCEL_CONFIG)

for key,value in excel_dict.items():
    if value['Status'] == 'Not Sent':
        names = [i.lower() for i in value['User Name'].split(' ')]
        student_email = ''.join([chr(int(i,base=2)) for i in value['email'].split(' ')])
        print("User email decrypted as {}".format(student_email))
        student_email = 'shrishty123chandra@gmail.com'
        student_subject = '{}_{}_{}'.format(key,*names)
        sub_to_file = read_email_from_gmail(CONTENT_EMAIL,student_subject)
        if student_subject in sub_to_file:
           saved_file = gen_pdf(key,sub_to_file[student_subject][:-4],LOGO)
        else:
            print("No attachment found in the email")
            print("Exiting")    
            break
        msg_text="""Hey {},\n\n\nGood to see the progress, Please find the attachment of your previous session.\n\n\nThank you,\nJohn """.format(value['User Name'])
        sub_to_send = "Your course material {}".format(key)

        print("Sending mail to {}".format(student_email))
        send_mail(FROM_EMAIL,[student_email],sub_to_send,msg_text,saved_file)

        print("Updating status in row {}".format(value['index']+2))
        update_excel(EXCEL_CONFIG,value['index']+2)

        print("Changing color as per statuses")
        change_color(EXCEL_CONFIG)
        
        print("Success !!")