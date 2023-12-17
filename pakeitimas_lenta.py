def nupiesta(lenta):

    print((lenta[1]) + (lenta[2]) + (lenta[3])) ####Atliekamas veiksmas su masyvais
    print((lenta[4]) + (lenta[5]) + (lenta[6]))
    print((lenta[7]) + (lenta[8]) + (lenta[9]))



### Dalinantis 9 is dvieju lieka vienas
#### jeigu ejimas dalinas is dvieju grys 0 jeigu jeigu liks remainingas x


def tikrinimas(ejimas):
    if ejimas % 2 == 0:
        return "O"
    else:
        return "X"

...
def geri_variantai(lenta):

    if (lenta[1]) == (lenta[2]) == (lenta[3]) \
        or (lenta[4]) == (lenta[5]) == (lenta[6]) \
        or (lenta[7]) == (lenta[8]) == (lenta[9]):
        return True
    elif (lenta[1]) == (lenta[4]) == (lenta[7]) \
        or (lenta[2]) == (lenta[5]) == (lenta[8]) \
        or (lenta[3]) == (lenta[6]) == (lenta[9]):
        return True
    elif (lenta[1]) == (lenta[5]) == (lenta[9]) \
        or (lenta[7]) == (lenta[5]) == (lenta[3]):
        return True
    else:
        return False
