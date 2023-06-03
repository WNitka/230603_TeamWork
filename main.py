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

assert objetosc_szescian(3) == 27
assert objetosc_szescian(5) == 125
assert objetosc_szescian(0) == 0

assert pole_powierzchni(3) == 54
assert pole_powierzchni(5) == 150
assert pole_powierzchni(0) == 0