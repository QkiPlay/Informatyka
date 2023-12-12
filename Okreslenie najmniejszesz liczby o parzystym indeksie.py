import random
wszystkie=[]
for i in range(100):
    wszystkie.append(random.randint(1,10000))

Najmniejsza_liczba_p = max(wszystkie)+1       #Zmienna do zapisania wartosci
IndeksParzystyNajmniejszej = -1               #Zmienna do zapisania numeru indeksu

for i in range(len(wszystkie)):                       #Pętla for która wykona się tyle razy ile elementów jest w liscie
    if i % 2 == 0:                                    #Sprawdzenie czy indeks jest parzysty
        if(Najmniejsza_liczba_p > wszystkie[i]):      #Sprawdzenie czy liczba jest mniejsza niż zmienna,
                                                      #w 1 przejsciu zawsze bedzie
            Najmniejsza_liczba_p = wszystkie[i]       #Jesli jest mniejsza, zapisz ją do zmiennej
            IndeksParzystyNajmniejszej = i            #Zapisz ktory numer indeksu ma najmniejsza liczba
print('Najmniejsza liczba o parzystym indeksie to', Najmniejsza_liczba_p, 'z indeksem numer', IndeksParzystyNajmniejszej)
