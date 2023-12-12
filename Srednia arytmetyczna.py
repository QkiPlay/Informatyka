import random
wszystkie=[]
for i in range(100):
    wszystkie.append(random.randint(1,10000))

suma = 0                                   #Zmienna do zapisania sumy
for i in wszystkie:                        #Pętla for która powtórzy się tyle razy ile elementów jest na liscie
    suma += i                              #Dodanie wartosci do sumy
sr_arytmetyczna = suma / len(wszystkie)    #Policzenie sredniej
print(sr_arytmetyczna)                     #Wypisanie sredniej
