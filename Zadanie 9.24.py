x = int(input('Wprowadź liczbę X: '))
l_pierwsze = 0
for i in range(0,x+1):
    czy = 0
    for w in range(1,i+1):
        if i%w == 0:
            czy += 1
    if czy == 2:
        l_pierwsze += 1
print('Pomiędzy 0 a',x,'jest',l_pierwsze,'liczb pierwszych.')