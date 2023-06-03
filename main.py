def pole_powierzchni(bok):
    pole_pow = 0
    pole_pow = 6*bok*bok
    return pole_pow

def objetosc_szescian(bok):
    objetosc = 0
    objetosc = bok*bok*bok
    return objetosc

bok = 5
pole_pow = pole_powierzchni(bok)
objetosc = objetosc_szescian(bok)

print(pole_pow)
print(objetosc)