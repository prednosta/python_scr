#!/usr/bin/env python3
import sys
from random import randrange

print("dp2.0")
print(sys.version_info)
print("na cli python3 --version")

print(" ")

print("dp2.6")

a = 2852	#strana
povrchKrychle = 6*(a**2) #povrch
objemKrychle = a**3 #objem

print("Delka hrany krychle je: ", a , " cm. Jeji povrch S= ", povrchKrychle , "cm2. A objem: ", objemKrychle , "cm3.")

print(" ")

print("dp.2.7")

zadana=int(input("Jakou chces delku hrany krychle? "))
povrchKrychle = 6*(zadana**2)
objemKrychle = zadana**3

print("Delka hrany krychle je: ", zadana , " cm. Jeji povrch S= ", povrchKrychle , "cm2. A objem: ", objemKrychle , "cm3.")

print(" ")

print("dp.2.8")

cislo = randrange(3)
print(cislo, "nahodne cislo 0-2")

print(" ")

print("dp.2.9")

tahCislo = randrange(3)
if(tahCislo == 0):
	tah_pocitace = "kamen"
elif(tahCislo == 1):
	tah_pocitace = "nuzky"
else:
	tah_pocitace = "papir"

print(tah_pocitace)

print(" ")
