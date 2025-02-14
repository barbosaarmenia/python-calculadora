# codigo de uma calculadora simples
# num1, num2, op, result

num1 = 0
num2 = 0
result = 0
op = ''

# colocar num loop while

while True:
    # o float ´q retorna string e nao da pra fazer op mat
    num1 = float(input('digite o primeiro numero: ')) 
    # ler o primeiro numero em float
    op = input('digite a operação matermatica a ser efetuada: ')
    num2 = float(input('digite o segundo numero: '))

    # condicionais
    if  op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print('operação não reconhecida')

    print('{} {} {} = {}'.format(num1, op, num2, result))