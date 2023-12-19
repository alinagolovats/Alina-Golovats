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
  

try:
    hind=float(input("Sisesta hind: "))
    if hind>=700:
       hind*=0.7
       print(hind)
    else:
        print(hind)
except:
    print("Viga")


