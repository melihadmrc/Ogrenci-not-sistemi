import pandas as pd


class ogrenci():
    def __init__(self,ad,soyad, numara, dersnot,harfnotu, gecmedurum):
        self.ad=ad
        self.soyad=soyad
        self.numara=numara
        self.dersnot=dersnot
        self.harfnotu=harfnotu
        self.gecmedurum=gecmedurum

    dersnot= []
    soyad = []
    numara = []
    ad = []
    harfnotu = []
    gecmedurum=[]

def ogrenci_listesi():
      ogrenci.ad.append(input("isim giriniz"))
      ogrenci.soyad.append(input("soyad giriniz"))
      ogrenci.numara.append(int(input("numara giriniz")))
      ogrenci.dersnot.append(input("ders notu giriniz"))


while True:
    ogrenci_listesi()
    print("öğrenci eklemek istiyorsanız y'ye , istemiyorsanız herhangi bir tuşa basınız")
    if input()=="y":
        continue
    else:
        break

ogrenci.dersnot=list(map(int,ogrenci.dersnot))
for j in range(0,len(ogrenci.dersnot)):

    if  ogrenci.dersnot[j] >= 90 and ogrenci.dersnot[j] <=100:
        ogrenci.harfnotu.append("AA")
    elif ogrenci.dersnot[j] >= 85 and ogrenci.dersnot[j] < 90:
        ogrenci.harfnotu.append("BA")
    elif ogrenci.dersnot[j] >= 80 and ogrenci.dersnot[j] < 85:
        ogrenci.harfnotu.append("BB")
    elif ogrenci.dersnot[j] >=70 and ogrenci.dersnot[j] < 80:
        ogrenci.harfnotu.append("CB")
    elif ogrenci.dersnot[j] >=60 and ogrenci.dersnot[j] < 70:
        ogrenci.harfnotu.append("CC")
    elif ogrenci.dersnot[j] >= 55 and ogrenci.dersnot[j] <60:
        ogrenci.harfnotu.append("DC")
    elif ogrenci.dersnot[j] >=50 and ogrenci.dersnot[j] < 55:
        ogrenci.harfnotu.append("DD")
    elif ogrenci.dersnot[j] >=40 and ogrenci.dersnot[j] <50:
        ogrenci.harfnotu.append("FD")
    else:
        ogrenci.harfnotu.append("FF")

for i in range(0,len(ogrenci.harfnotu)):
    if ogrenci.harfnotu[i] == "FF":
        ogrenci.gecmedurum.append("Geçti")
    else:
        ogrenci.gecmedurum.append("Kaldı")

my_data={
    "Ad": ogrenci.ad,
    "Soyad": ogrenci.soyad,
    "Numara": ogrenci.soyad,
    "Ders Notu": ogrenci.dersnot,
    "Harf Notu": ogrenci.harfnotu,
    "Geçme Durum": ogrenci.gecmedurum
}

dataframe=pd.DataFrame(my_data)
dataframe.to_excel("Öğrenci Listesi.xlsx")


print(dataframe)