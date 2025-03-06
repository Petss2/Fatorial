num = int(input('Digite um número para saber o seu fatorial:  '))
f = 1
for c in range(num, 0, -1):
    f *= c
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(f)