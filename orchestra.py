from readMail import *
from config import FROM_EMAIL,EXCEL_CONFIG,CONTENT_EMAIL,LOGO
from excel_manager import *
from sendMail import *
from pdf_gen import *

excel_dict = read_pdf_in(EXCEL_CONFIG)

for key,value in excel_dict.items():
    
    # Check if the row status is Not Sent
    if value['Status'] == 'Not Sent':
        
        # Make a list of firstnames and username in lowercase
        names = [i.lower() for i in value['User Name'].split(' ')]

        # Decrypt the Student Email
        student_email = ''.join([chr(int(i,base=2)) for i in value['email'].split(' ')])
        print("User email decrypted as {}".format(student_email))

        # Dummy sender fixing code
        student_email = 'shrishty123chandra@gmail.com'

        # Creating student subject text
        student_subject = '{}_{}_{}'.format(key,*names)

        # Read the email from CONTENT_EMAIL with the subject and save the attachment
        sub_to_file = read_email_from_gmail(CONTENT_EMAIL,student_subject)

        # If the subject is in sub_to_file, then it means that the attachment is saved successfully
        if student_subject in sub_to_file:
            
            # Modify the saved file with logo and the text
           saved_file = gen_pdf(key,sub_to_file[student_subject][:-4],LOGO)

        else:
        # There has been error and it needs to be exited.
            print("No attachment found in the email")
            print("Exiting")    
            break

        # Create the message output body
        msg_text="""Hey {},\n\n\nGood to see the progress, Please find the attachment of your previous session.\n\n\nThank you,\nJohn """.format(value['User Name'])
        
        # Subject to send to the email
        sub_to_send = "Your course material {}".format(key)

        # Send the email
        print("Sending mail to {}".format(student_email))
        send_mail(FROM_EMAIL,[student_email],sub_to_send,msg_text,saved_file)

        # Update the excel sheet
        print("Updating status in row {}".format(value['index']+2))
        update_excel(EXCEL_CONFIG,value['index']+2)

        # Update the color changes
        print("Changing color as per statuses")
        change_color(EXCEL_CONFIG)
        
        # Print the final success message
        print("Success !!")