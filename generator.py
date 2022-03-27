# Küçük Harfler
# Büyük Harfler
# Rakamlar
# Özel işaretler
# Rastgele Komutları

import random
import string

alfabe=[]
kucukharfler=list(string.ascii_lowercase)
buyukharfler=list(string.ascii_uppercase)

for rakam in range(0,10):
    alfabe.append(rakam)

for i in range(len(kucukharfler)):
    alfabe.append(kucukharfler[i])
    alfabe.append(buyukharfler[i])

# Şimdi sıra geldi özel karakter eklemeye (? ! # * ) ( & / [ ] % )
özelkarakterler=["?","!","#","*",")","(","%"]
for karakter in range(len(özelkarakterler)):
    alfabe.append(özelkarakterler[karakter])


uzunluk=int(input("Enter the length of password: ")) # Parolanın uzunluğun kullanıcı belirlesin.
sifre=[]
for i in range(uzunluk):
    rastgeledeger=random.randint(0,len(alfabe))
    sifre.append(alfabe[rastgeledeger])

f = open("myfile.txt", "a")
listToStr = ''.join([str(elem) for elem in sifre])
print(listToStr)
f.write(listToStr+"\n")
f.close()
