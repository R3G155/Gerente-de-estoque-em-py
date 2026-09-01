print('--- CALCULADORA ---')

# Recebe os números convertendo para inteiro
valor = int(input('Digite o primeiro número: '))
print('Escolha a operação:\n1 para Somar\n2 para Subtrair')
operacao = int(input('Digite uma opção: '))
valor1 = int(input('Digite o segundo número: '))

# Executa as condições baseadas na opção escolhida
if operacao == 1:
    soma = valor + valor1
    print(f'Resultado da soma: {soma}')
elif operacao == 2:
    subtracao = valor - valor1
    print(f'Resultado da subtração: {subtracao}')
else:
    print('Opção inválida!')

print('final')
