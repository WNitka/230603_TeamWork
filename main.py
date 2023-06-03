def ostroslup (a,b,h): 
    objetosc=(1/3)*a*b*h
    objetosc_za=round(objetosc,2)
    return objetosc_za

assert ostroslup (10,10,10) == 333.33

assert ostroslup (8,4,12) ==128