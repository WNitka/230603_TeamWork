def pole_powierzchni(bok):
    pole_pow = 0
    pole_pow = 6*bok*bok
    pole_pow_za = round(pole_pow,2)
    return pole_pow_za

def objetosc_szescian(bok):
    objetosc = 0
    objetosc = bok*bok*bok
    objetosc_za = round(objetosc, 2)
    return objetosc_za

bok = 3.4
pole_pow_za = pole_powierzchni(bok)
objetosc_za = objetosc_szescian(bok)

print(pole_pow_za)
print(objetosc_za)