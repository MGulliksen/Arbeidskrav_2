# -*- coding: utf-8 -*-
"""
I denne filen vil du finne totalt 6 koder som løser forskjellige oppgaver fra 1 til 6. 
Det er tatt høyde for at oppgavene kjøres fra samme sted, slik at dersom f.eks. import numpy as np er skrevet inn 
i en oppgave er den ikke lagt inn på ny dersom det er behov for det senere. 

Created on Sun Jan 12 20:12:36 2025

@author: Marianne Gulliksen ma_gulliksen@hotmail.com
"""

""" 
Oppgave 1 - Viser et program som regner ut hvor gammel en person ble i løpet av 2024, basert på en når personen ble født.
"""

"""Spørsmål_1"""
fødselsår =int(input("Hvilket år er du født?"))

"""Utregning"""
nåværende_alder = 2024 - fødselsår

"""Endelig svar"""
print(f"Basert på ditt svar så ble du {nåværende_alder} år i 2024!")


"""
Oppgave 2 - Viser et program som regner ut hvor mange pizzaer som skal handles inn til fest, basert på antall gjester. 
Programmet skal ta høyde for at det kun kjøpes hele pizzaer og at antallet skal vises uten kommategn. 
"""

"""Spørsmål_2"""
antall_elever =int(input("Skriv inn antall elever:"))
 
"""diverse informasjon"""
import math
en_porsjon = 0.25
en_pizza = en_porsjon * 4
 
"""Regnestykket"""
antall_pizza = math.ceil(antall_elever * en_porsjon)

print(f"Det må handles inn {antall_pizza} pizzaer til klassefesten!")
 

"""
Oppgave 3 - Viser et program som regner om fra grader til radianer. 
"""

"""Spørsmål_3"""

import numpy as np

"""Definiasjon"""
def grader_til_radianer(v_grad):
    v_rad = v_grad * np.pi / 180
    return v_rad

"""Regnestykket"""
v_grad = float(input("Skriv inn gradtallet:"))
v_rad = grader_til_radianer(v_grad)


"""Endelig svar"""
print(f"Når graden er {v_grad}, så er radiantallet {v_rad}.")


"""
Oppgave 4 a) -  Viser en dictionary med ulike land som nøkkel, og som gir informasjon om hovedstaden i landet og antall
innbyggere i million i hovedstaden. 
"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161], 
        "Italia": ["Roma", 2.873]
        }

"""
Oppgave 4 b) - Viser et program som skriver ut informasjon om hovedstad og antall innbyggere basert på ønsket land hentet
    fra dictionaryen min i oppgave 4a) OBS! Dictionaryen er ikke lagt inn en gang til her, sånn at oppgave a og b må sees sammen. 
"""

land = input("Skriv inn navnet på et land: ")

if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")


"""
Oppgave 4 c) - Viser et program som lar en bruker opprette ny data, og deretter oppdaterer dictionaryen fra tidligere i oppgaven. 
"""
"""Dette programmet tar utgangspunktet i samme program som oppgave B, men bygger på videre"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161], 
        "Italia": ["Roma", 2.873]
        }


land = input("Skriv inn navnet på et land: ")

if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")
else:
    print("\nLandet er ikke i oversikten, det er veldig fint om du kan oppgi den aktuelle informasjonen, så oppdaterer vi listen.")
    hovedstad = input("\nSkriv inn hovedstaden i det aktuelle landet: ")
    innbyggere = float(input("\nSkriv inn antall millioner innbyggere i hovedstaden: "))
    data[land] = [hovedstad, innbyggere]
    print(f"\nTakk! Listen er nå oppdatert med landet {land}, der hovedstaden er {hovedstad}, og inneholder {innbyggere} mill. innbyggere.")

print("\nOppdatert oversikt:\n")
for land, info in data.items():
    print(f"{land}: Hovedstad - {info[0]}, Innbyggere - {info[1]} mill.")


"""
Oppgave 5 - Viser et program som regner ut arealet og ytre omkrets av en figur som er satt sammen av en rettvinklet trekant og 
en halvsirkel basert på valgte a- og b argumenter. 
"""

import math

def beregn_areal_omkrets(a, b):
    radius = a / 2
    hypotenus = math.sqrt(a**2 + b**2)
    
    areal_sirkel = (math.pi * radius**2) / 2
    omkrets_sirkel = (math.pi * radius) / 2 
    areal_trekant = (a * b) / 2
    omkrets_trekant = b + hypotenus 
    
    areal_totalt = areal_sirkel + areal_trekant
    omkrets_totalt = omkrets_sirkel + omkrets_trekant
    
    return areal_totalt, omkrets_totalt

"""Test av programmet"""
a = float(input("Skriv inn ønsket verdi for a: "))
b = float(input("Skriv inn ønsket verdi for b: "))
L = beregn_areal_omkrets(a, b)
areal = L[0]
omkrets = L[1]

"""Endelig svar"""
print("Arealet på figuren er", areal)
print("Omkretsen på figuren er", omkrets)


"""
Oppgave 6  Viser en kode som plotter ønskede funksjoner på intervall. 
"""

"""Funksjonen som skal plottes er f(x)=-x**2-5, for x på intervallet [-10, 10]"""


import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
fx = -x**2 - 5

# Plot funksjonen
plt.plot(x, fx, '*', color='green', linewidth = 2, label='f(x) = -x^2 - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("""f(x)=x**2-5,for x på intervallet [10,10]""")
plt.legend()
plt.show()



    

















