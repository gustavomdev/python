a1 = int(input('Primeiro termo de uma PA:'))
r = int(input('Razão de uma PA:'))
termo = a1
c = 1
while c <= 10:
    print(f'{termo}',end='')
    print(' -> ' if c < 10 and c > 0 else'',end='')
    termo += r
    c+=1
    