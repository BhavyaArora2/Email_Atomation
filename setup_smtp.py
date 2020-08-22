import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from read_contacts import get_contacts
from read_template import read_template

MY_ADDRESS = 'sender@example.com'
PASSWORD = 'password'

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)


def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')
    special_message_template = read_template('message1.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())
        message1 = special_message_template.substitute(PERSON_NAME=name.title())

        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "This is TEST"

        if name.title() == 'Person2':
            msg.attach(MIMEText(message, 'plain'))
        else:
            msg.attach(MIMEText(message1, 'plain'))

        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
