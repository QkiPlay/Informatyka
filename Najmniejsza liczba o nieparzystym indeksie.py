import random
wszystkie=[]
for i in range(100):
    wszystkie.append(random.randint(1,10000))
  
Najmniejsza_liczba_np = max(wszystkie)+1          #Zmienna do zapisania wartosci
IndeksNieParzystyNajmniejszej = -1                #Zmienna do zapisania numeru indeksu

for i in range(len(wszystkie)):                   #Pętla for która wykona się tyle razy ile elementów jest w liscie
    if i % 2 == 1:                                #Sprawdzenie czy indeks jest NieParzysty
        if(Najmniejsza_liczba_np > wszystkie[i]): #Sprawdzenie czy liczba jest mniejsza niż zmienna,
                                                  #w 1 przejsciu zawsze bedzie
            Najmniejsza_liczba_np = wszystkie[i]  #Jesli jest mniejsza, zapisz ją do zmiennej
            IndeksNieParzystyNajmniejszej = i     #Zapisz ktory numer indeksu ma najmniejsza liczba
print('Najmniejsza liczba o NieParzystym indeksie to', Najmniejsza_liczba_np, 'z indeksem numer', IndeksNieParzystyNajmniejszej)
