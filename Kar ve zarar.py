import pandas as panda
import requests
from bs4 import BeautifulSoup

class cozum:
    def maksimum_kar(self,endusuk_fiyat,enbuyuk_kar,fiyatlar):
        self.endusuk_fiyat = endusuk_fiyat
        self.enbuyuk_kar = enbuyuk_kar
        self.fiyatlar = fiyatlar


    def kar_hesapla(self):
        for fiyat in self.fiyatlar:
            if fiyat < endusuk_fiyat:
                endusuk_fiyat = fiyat

            kar= fiyat - endusuk_fiyat

            if kar > enbuyuk_kar:
                enbuyuk_kar = kar






link = requests.get('https://www.paribu.com/markets')
soup = BeautifulSoup(link.content,'html.parser')

kayitlar=soup.find_all("div",attrs={"class":"pg-left wide-682"})

for kayıt in kayitlar:
    kar = cozum.kar_hesapla()