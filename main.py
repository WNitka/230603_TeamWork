import math

def objetosc_stozka(r, h):
    objetosc = (1/3) * math.pi * r**2 * h
    return round(objetosc, 2)

print(objetosc_stozka)

assert objetosc_stozka(4, 6) == 100.53
assert objetosc_stozka(5, 10) == 261.80

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

assert objetosc_szescian(3) == 27
assert objetosc_szescian(5) == 125
assert objetosc_szescian(0) == 0

assert pole_powierzchni(3) == 54
assert pole_powierzchni(5) == 150
assert pole_powierzchni(0) == 0

def ostroslup (a,b,h): 
    objetosc=(1/3)*a*b*h
    objetosc_za=round(objetosc,2)
    return objetosc_za

assert ostroslup (10,10,10) == 333.33
assert ostroslup (8,4,12) == 128