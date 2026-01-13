import requests
from datetime import datetime, timezone
import smtplib
import time


MY_LAT=112.866300582885742
MY_LONG=717.52478790283203
my_email="pleaseenteryourownemailandpassword@gmail.com"
my_password="fkfdee  fek,dof frvmogtmf"
location_link=requests.get(url="http://api.open-notify.org/iss-now.json#")
location_link.raise_for_status()
data=location_link.json()
longitude=float(data["iss_position"]["longitude"])
latitude=float(data["iss_position"]["latitude"])
coordinates=(longitude, latitude)
parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now= datetime.now(timezone.utc)
hour=time_now.hour

while True:
    time.sleep(60)
    if abs(latitude-MY_LAT)<=5.0 and abs(longitude-MY_LONG)<=5.0 and (hour>sunset or hour<sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Look up!\n\n\nWoah look up at the sky theres an iss station above!"
        )


