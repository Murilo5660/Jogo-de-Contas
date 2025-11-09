import random
nome = str(input('Qual seu nome? '))
for _ in range(random.randint(1,10)):
        a = random.randint(1,10)
        b = random.randint(1,10)
        print(f'{a} + {b} = ?')
        c = int(input('Digite o resultado: '))
        
        while c != a + b:
            print('Tente novamente!')
            c = int(input('Digite o resultado: '))

print('\nEstá correto!')
print(f'Você venceu! Parabéns {nome:=^20}')