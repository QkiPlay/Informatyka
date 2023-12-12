#Okreslenie największej liczby o parzystym indeksie
import random
wszystkie=[]
for i in range(100):
    wszystkie.append(random.randint(1,10000))

Najwieksza_liczba_p = min(wszystkie)-1
IndeksNieParzystyNajwiekszej = -1

for i in range(len(wszystkie)):
    if i % 2 == 0:
        if(Najwieksza_liczba_p < wszystkie[i]):
            Najwieksza_liczba_p = wszystkie[i]
            IndeksNieParzystyNajwiekszej = i 
print('Największa liczba o Parzystym indeksie to', Najwieksza_liczba_p, 'z indeksem numer', IndeksNieParzystyNajwiekszej)
