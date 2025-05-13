lista_soldados_buzz=[]
seguir = True
while seguir:
    soldados_buzz=input()
    if soldados_buzz.isdigit():
        soldados_buzz=int(soldados_buzz)
        lista_soldados_buzz.append(soldados_buzz)

    elif soldados_buzz=="FIN":
        seguir=False
lista_buzz_original=lista_soldados_buzz
lista_soldados_zurg=[]
continuar = True
while continuar:
    soldados_zurg=input()
    if soldados_zurg.isdigit():
        soldados_zurg=int(soldados_zurg)
        lista_soldados_zurg.append(soldados_zurg)

    elif soldados_zurg=="FIN":
        continuar=False
lista_zurg_original=lista_soldados_zurg

#el malo es Zurg y el bueno es Buzz

while len(lista_soldados_buzz)!=0 and len(lista_soldados_zurg):
    if lista_soldados_buzz[0]>lista_soldados_zurg[0]:
        print("Buzz ha ganado esta ronda!")
        lista_soldados_zurg.pop(0)
        lista_soldados_buzz[0]=lista_soldados_buzz[0]-1

    elif lista_soldados_buzz[0]<lista_soldados_zurg[0] or lista_soldados_buzz[0]==lista_soldados_zurg[0]:
        print("Zurg ha ganado esta ronda!")
        lista_soldados_buzz.pop(0)
        lista_soldados_zurg[0]=lista_soldados_zurg[0]-1


if len(lista_buzz_original)<len(lista_zurg_original):
    print("El malvado emperador Zurg tomara control de la Unimente!")
else:
    print("Buzz! Nos has salvado, estamos agradecidos!")