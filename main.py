import smtplib
import  datetime as dt
import random
import pytz

country_time_zone = pytz.timezone('Iran')
country_time = dt.datetime.now(country_time_zone)
iran_time= country_time.strftime(" %H:%M:%S")
print(iran_time)




my_email = "***********@gmail.com"
password = "************"
# edited

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="**********@gmail.com",
                        msg=f"Subject: Hello\n\nIt's {iran_time} "
                        )
