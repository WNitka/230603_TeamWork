import math

def objetoscKuli(promien):
    objetosc = (4/3)* math.pi * promien**3
    objetosc_za = round(objetosc, 2)
    return (objetosc_za)

promienKuli = 4
objetosc = objetoscKuli(promienKuli)

print(objetosc)

assert objetoscKuli(promienKuli) == 268.08

promienKuli_2 = 12
objetosc_2 = objetoscKuli(promienKuli_2)

print(objetosc_2)

assert objetoscKuli(promienKuli_2) == 7238.23


