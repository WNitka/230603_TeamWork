import math

def objetoscKuli(promien):
    objetosc = (4/3)* math.pi * promien**3
    return objetosc

promienKuli = 4
objetosc = objetoscKuli(promienKuli)

print(objetosc)