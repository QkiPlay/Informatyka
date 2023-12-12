l_pasazerow = int(0)
k_wycieczki = int(0)
k_paliwa = float(0)
while True:
    print('Wprowadź koszt paliwa:', end=' ')
    k_paliwa = float(input())
    print('Wprowadź liczbę pasażerów:', end=' ')
    l_pasazerow = int(input())
    if l_pasazerow == 0:
        print('Koszt wycieczki to', k_paliwa, 'PLN')
    else:
        k_wycieczki = (k_paliwa+1)/(l_pasazerow+1)
        print('Twój koszt wycieczki to ', round(k_wycieczki, 2))
    x = input('Czy chcesz przerwać działanie programu? (T/N): ')
    while x != 'T' and x != 'N':
        print('Nieprawidłowo wprowadzone dane. Wybierz opcję "T" albo "N"')
        x = input('Czy chcesz przerwać działanie programu? (T/N): ')
    if x == 'T':
        break
        