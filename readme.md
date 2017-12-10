# Automated Email Communication
This project attempts to arrange an automated email communication based on the following user story.

John is a guitar instructor who loves to teach the guitar, He want to automate the process of sending emails to his students, he has a portal where his students can register to different courses and learn.There is a content team for him who shares the content with him via email. In the subject line, there is going to be a code followed by the username (327778_tagore). Every day John has to share some pdf notes to his students via email. The problem he is facing is for each student he needs to Edit the pdf course material add the logo and some content to the pdf, attach this to the email and send to respective students. In the beginning, he had only 5 students which are not difficult for him to do it manually, now he had more students every day he needs to send the emails to 100 - 150 students which are going be an impossible task for him. 

He wanted to automate the process, This is the overview what he wanted to do.
As his portal supports to download the student's list in excel sheet, he wants to parse the excel sheet and match the subject line with the student, read the email get the attachment append the logo and text to the PDF and attach this to email with some content and send it to respective students.

In the excel sheet of students, he had columns named as follows
Serial ID - it is a number
Course ID - it is a number
email - it is in some format which JOHN doesn't understand (need to figure it out and fetch the email from it)
encoded_code - (he got to know that this code is generated by using Serial ID and Course ID, it is generated by adding the hexadecimal values of Serial Id and Course ID)

and the code on the email subject followed is obtained by converting the encode_code to a decimal value.


The content team is going to send an email from a standard email 'x@gmail.com' to his email id 'y@gmail.com' and the subject line for the above student is 327778_tagore_navabothu

x@gmail.com and y@gmail.com should be configurable by him.

The script should able to login to his email (email id and password is going to be configured by him and he is going to give access permissions to script to allow to login to his email)
read the emails from x@gmail.com by matching the subject line from the sheet
get the attachment and append the logo and content to the attachment
create an email body and add this attachment to email body and send it to the recpective student.

After sending emails it should write the (sent/unsent) status back to the same excel sheet in a new column. font color for sent status is green and unsent is red. If john finds any unsent again he gives the same excel sheet, but this time it selects only unsent student details


## Getting Started

All the config details are to be maintained in the **config.py** file.

1.ORG_EMAIL     = "@gmail.com"
1.FROM_EMAIL    = "<x@gmail.com>" + ORG_EMAIL # John's email
1.FROM_PWD      = "<Password for x@gmail.com>" # Password for John's email
1.SMTP_SERVER   = "imap.gmail.com"
1.SMTP_PORT     =  993
1.CONTENT_EMAIL = "<y@gmail.com>"  # Content team's email
1.EXCEL_CONFIG  = './input_data.xlsx' # Location of student excel file
1.LOGO          = 'input_logo.jpg'    # Location of Logo file

### Prerequisites / Installation Steps
This project is built with Python 3.6.2 and all modules need to be python 3 compatible.
The python modules mentioned in the **requirements.txt**, should be available.
Use the following command.
```
pip install -r requirements.txt
```
The pandas module is difficult to install in first go. 
Kindly refer to the following [link](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04) if you need help with it. It is recommended to install it with Anaconda for ease of installation.

### Important parts of the solution
There are following three major parts of the solution.
1. Reading John's gmail inbox and finding messages from the content team's email and saving the attachment.
    a. Refer to **readmail.py**. Currently, search operations on gmail inbox do not support string search they support word search only, hence it is important to provide the full subject word.
2. Processing the attachment to add requisite figures and text as per requirements.
    a. Refer to **pdf_gen.py**. The attachment is saved and processed by using reportlab, here the pdf is mangaed as a series of pages.
    In each page we use a canvas object to insert/modify content.
3. Sending the mail to the user, whose email ID is obtained from the student excel. 
   a. Refer to **sendMail.py**. The mail is sent to the user after attaching a MIMEMultiPart object.
   After the mail is send the data is updated in the student excel sheet and the color is also changed.


## A conceptual walkthrough

1. Consider the first row of **input_data.xslx** sheet, and lines in orchestra.py . The numbers in square bracket denote the lines in **orchestra.py**.
2. Here for the enoced code 327778, the subject word would be  '327778_tagore_navabothu'. [10]
3. If the status of the row is Not Sent, then the receiver's mail is decrypted and valuse is 'tagore@hod.life'.[12]
1. The subject line is created and the inbox is searched. [15,16]
1. If the attachment is found and saved, then it is modified using the logo file path.[18]
1. Else the process is exited. [20-22]
1. The message body is prepared and the mail is sent. [23-27]
1. Status is updated in excel sheet and colors are remarked. [29-33]

