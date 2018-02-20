#email scheduling
import smtplib
s= smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("amusmiley16@gmail.com","icantforgetu")
msg="hi how are you"
s.sendmail("amusmiley16@gmail.com","amusmiley16@gmail.com",msg)
print("sucess")
s.quit()
