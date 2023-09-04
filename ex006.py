# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num1 = int(input('Digite um numero: '))
# minimização do codigo
# d = num1 * 2
# t = num1 * 3
# r = num1 ** (1/2)
# (num1**(1/2))))
print('O Dobro de {} vale {}.'.format(num1, (num1 * 2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(num1, (num1 * 3), num1,
                                                                               pow(num1, (1 / 2))))
