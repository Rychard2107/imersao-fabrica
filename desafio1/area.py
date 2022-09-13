import modulo

modulo.titulo('Calculador de Área')
n = int(input('Digite 1 para Quadrado\nDigite 2 para Triângulo retangulo\nDigite 3 para Círculo\nDigite aqui: '))

if n == 1:
    l1 = float(input('Digite o primeiro lado: '))
    l2 = float(input('Digite o segundo lado: '))
    print(f'A área do quadrado é {modulo.areaQ(l1, l2)}')
elif n == 2:
    l1 = float(input('Digite o primeiro lado: '))
    l2 = float(input('Digite o segundo lado: '))
    print(f'A área do triângulo é {modulo.areaT(l1, l2)}')
elif n == 3:
    r = float
    print(f'A área do circulo é {modulo.areaC(r)}')
else:
    print('\033[1;31mnúmero invalido\n033[m')
