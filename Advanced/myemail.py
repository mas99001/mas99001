import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
email = input("Enter your email: ")
#password = input("Enter your password: ")
import getpass
#email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email, password)

recipient = input("Enter recipient email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")
smtp_object.sendmail(email, recipient, f"Subject: {subject}\n\n{message}")
smtp_object.quit()
