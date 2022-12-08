#Bu kısımda gerekli kütüphaneleri içe aktarıyoruz.
from twilio.rest import Client
from bs4 import BeautifulSoup
import requests

#Bu kısımda Twilio API anahtarlarını tanımlıyoruz.
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

#Bu kısımda Twilio API'sini kullanarak bir WhatsApp mesajı gönderiyoruz.
client = Client(account_sid, auth_token)

#Bu kısımda bir konum girilmesini istiyoruz.
konum = input("Lütfen bir konum giriniz: ")

#Bu kısımda verilen konum için hava durumu bilgisi alınmaya çalışılır.
#Bu işlem için OpenWeatherMap API'sini kullanıyoruz.
url = "https://api.openweathermap.org/data/2.5/weather?q=" + konum
