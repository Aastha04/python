import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("s.frozenstar18@gmail.com","//password")
Msg="le jayenge le jayenge dilwale dulhaniya le jayenge......."
s.sendmail("s.frozenstar18@gmail.com","piyush.sh99@gmail.com",Msg)
print("mailed sucessfully,check inbox")
s.quit()