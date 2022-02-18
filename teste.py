from math import trunc
while True:
    o = input('Escolha sua operação: \n1 - decimal > binario \n2 - decimal > octal \n3 - decimal > hexadecimal')
    resultado = ''
    if o == '1':
        n = int(input('Digite o valor a ser convertido'))
        while True:
            if n == 1:
                resultado = str(int(n)) + resultado
                break
            resto = str(n % 2)
            n = trunc(n / 2)
            resultado = resto[-1] + resultado

    print(resultado)
    break