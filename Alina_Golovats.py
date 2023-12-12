from pickle import TRUE
from random import randint
from stringprep import c22_specials, c6_set


#arv1=float(input("Arv1: "))
#t=input("Tehe: ")
#arv2=float(input("Arv2: "))
#vastus=eval(str(arv1)+t+str(arv2)) #читает в формате текст, а выдаст в формате результата и преобразует
#print(str(arv1)+t+str(arv2)+"="+str(vastus))
#print(arv1,t,arv2,"=",vastus,sep="")
#print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))



#nimi=input("Mis on sinu nimi?").capitalize() #alina->Alina - формат для большой буквы сначала по умолчанию
#print("Tere "+nimi+"!")#print("Tere maailm!".center(75,"-"))  #текст по центру, то что в "" знаки которые будут заполнять пустоту либо пробел
#print("Tere" ,nimi+"!")
#print("Tere {0}!".format(nimi))
#vanus=int(input("Kui vana sa oled?"))        #"21"!=21
#print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja nimi=",nimi,type(nimi)) #обозначение класса переменной вместе с ее значением
#print("Muutuja vanus=",vanus,type(vanus)) #обозначение переменной без ее значения


#vanus=18
#eesnimi="Jaak"
#pikkus=16.5
#kas_käib_koolis=True 

#print("Muutuja vanus=",vanus,"on",type(vanus))
#print("Muutuja eesnimi=",eesnimi,"on",type(eesnimi))
#print("Muutuja pikkus=",pikkus,"on",type(pikkus))
#print("Muutuja kas_käib_koolis=",kas_käib_koolis,"on",type(kas_käib_koolis))


#from random import *
#from math import *
#kokku=randint(1,100)
#print("Laua peal on",kokku,"kommid. Mitu tahad süüa?")
#kommid=int(input())
#kokku-=kommid
#print("Nüüd kokku on",kokku)


#u=float(input("Ümbermõõt: ")) #L=pi*2*r=pi*d
#d=round(u/pi,2)
#print("Läbimõõt =",d)


#N=float(input("Sisesta ristküliku laius (N meetrites): "))
#M=float(input("Sisesta ristküliku pikkus (M meetrites: "))
#d=sqrt(N**+M**2)
#print("Diagonaal=",d,"m")


#try:
#    aeg = float(input("Mitu tundi kulus sõiduks? "))
#except :
#    print("On vaja ainult numbrid sisastada")
#    try:
#        teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#        kiirus = teepikkus/aeg
#        print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    except :
#        print("Viga andmetaga")
#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg
#print("Sinu kiirus oli " + str(kiirus) + " km/h")


#try:
#    min_=int(input("Min: "))
#except :
#    print("On vaja täisarv kasutada!")
#try:
#    max_=int(input("Max: "))
#except :
#    print("Viga max_ muutujaga!")


#a1=randint(min_,max_)
#a2=randint(min_,max_)
#a3=randint(min_,max_)
#a4=randint(min_,max_)
#a5=randint(min_,max_)
#keskmine=(a1+a2+a3+a4+a5)/5
#print("Arvud: {0},{1},{2},{3},{4}. Aritmetiline keskmine on: {5}".format(a1,a2,a3,a4,a5,keskmine))


#print("@..@".center(10," "))
#print("(----)".center(10," "))
#print("( \__/ )".center(10," "))
#print('^^ "" ^^'.center(10," "))


#try:
#    a=float(input("a: "))
#except :
#    print("On vaja täisarv kasutada!")
#try:
#    b=float(input("b: "))
#except :
#    print("Viga muutujaga!")
#try:
#    c=float(input("c: "))
#except :
#    print("Viga c muutujaga!")
#P=a+b+c
#print("Perimetr/Ümbermõõt: ",P)

try:
    P=int(input("Sõbrade kogus: "))
except :
    print("Kogus on täisarv")
hind=12.90
hind*=hind*1.1 #hind+10%
print("Igaüks maksab",hind/P)
