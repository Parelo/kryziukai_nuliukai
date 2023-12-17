
import os
from fgth import nupiesta , tikrinimas , geri_variantai
lenta = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

zaidimas = True #zaidimas , kad testusi , prisiskyriau kintamajam true false
ejimas = 0
coplete = False




while zaidimas: ### siuo momemtu while ciklas inputui

    nupiesta(lenta)### rodom lenta
    user = input() ###### eiliskumas , kad useris suveda info
    if user == "":  #### While loop eina stringas vistiek galioja
        print("repeat")
    elif str.isdigit(user) and int(user) in lenta:
            ejimas += 1
            lenta[int(user)] = tikrinimas(ejimas)
    if geri_variantai(lenta):
        zaidimas, coplete = False, True












