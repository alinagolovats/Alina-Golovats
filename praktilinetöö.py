#eesnimi=input("Mis on sinu nimi?").capitalize()
#if eesnimi=="Juku":
#    try: 
#       vanus=int(input("Kui vana sa oled?"))
#       print("Jukule ostame" , end="")
#       if 0<vanus<=6:
#           print("tasuta pilet")
#       elif 6<=vanus<=14:
#           print("Lastepilet")
#       elif 14<=vanus<=65:
#           print("Täispilet")
#       elif 65<=vanus<=100:
#           print("Sooduspilet")
#       else:
#           print("Mitte midagi")
#    except:
#       print("Int andmetüüp on vaja kasutada!")

#else:
#    print("Mine ise kinno!")


#eesnimi=input("Mis on 1. nimi?").capitalize() #"Eldar" "Artur"
#eesnimi=input("Mis on 2. nimi?").capitalize()
#if (eesnimi=="Eldar" and eesnimi2=="Artur") or (eesnimi=="Artur" and eesnimi=="Eldar"):
#    print("Need on pinginaaabrid")
#else:
#    print("Rühmakaaslased")

#if (eesnimi!=eesnimi2) and eesnimi1 and eesnimi2 in["Eldar", "Artur"]: #[]-список
#    print("Need on pinginaaabrid")
#else:
#    print("Rühmakaaslased")


#try:
#    pikkus=float(input("Pikuus: "))
#    try:
#        laius=float(input("Laius: "))
#        S=pikkus*laius
#        print("Pindala võrdub", S)
#        soov=input("Kas tahad remondi teha?").lower #jah,Jah,JAH->jah  upper->JAH
#        if soov=="jah" or soov=="да":
#            hind=float(input("Ruutmeetri hind: "))
#            summa=hind*S
#            print("Remondi summa on", summa)
#        else:
#            print("Head aega")
#    except:
#        print("Viga")
#except:
#    print("Viga")
  

#try:
#    hind=float(input("Sisesta hind: "))
#    if hind>=700:
#       hind*=0.7
#       print(hind)
#    else:
#       print(hind)
#except:
#    print("Viga")


#sugu=input("Kas sa oled mees või naine?").lower()
#if sugu=="naine" or sugu=="n":
#    l1=155
#    l2=170
#    l3=255
#elif sugu=="mees" or sugu=="m":
#    l1=160
#    l2=180
#    l3=255
#else:
#    l1=0
#    print("Viga")
#if l1!=0:
#  try:
#    pikkus=int(input("Sisesta oma pikkus"))
#    if pikkus>29 and pikkus<155: #100
#        vastus="lühike"
#    elif pikkus>=l1 and pikkus<l2: #165
#        vastus="keskmine"
#    elif pikkus>=l2 and pikkus<=l3: #200
#        vastus="pikk"
#    else:
#        vastus="tundmatu"
#    print("Sinu pikkus on {0}" .format(vastus))
#  except:
#    print("Vale andmete formaat!")


from datetime import *
from random import *
arve_nr=datetime.now() #date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa/n"
summa=0
toode1="piim"
hind=randint(50,150)/100
v=input("Toode:"+toode1+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
    summa+=mitu*hind
print(tsekk)
toode2="mahl"
hind=randint(50,150)/100
v=input("Toode:"+toode2+" Hind:"+str(hind)+"\nKas tahad osta?").lower
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode1+" ",+str(hind)," ",+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
print(tsekk)
toode3="vesi"
hind=randint(50,150)/100
v=input("Toode:"+toode3+" Hind:"+str(hind)+"\nKas tahad osta?").lower
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode3+" ",+str(hind)," ",+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)

