import random
wszystkie=[]
for i in range(100):
    wszystkie.append(random.randint(1,10000))
  
Najwieksza_liczba_np = min(wszystkie)-1
IndeksNieParzystyNajwiekszej = -1

for i in range(len(wszystkie)):
    if i % 2 == 1:
        if(Najwieksza_liczba_np < wszystkie[i]):
            Najwieksza_liczba_np = wszystkie[i]
            IndeksNieParzystyNajwiekszej = i 
print('Największa liczba o NieParzystym indeksie to', Najwieksza_liczba_np, 'z indeksem numer', IndeksNieParzystyNajwiekszej)
