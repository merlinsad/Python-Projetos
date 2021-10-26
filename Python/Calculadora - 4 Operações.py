num = int(input('Escolha a opção: \n1- Soma de 2 números\n2- Diferença entre dois números ( o menor pelo maior )\n3- Produto entre 2 números.\n4- Divisão entre 2 números ( o denominador não pode ser zero)\nEscolha a opção:  '))

if num > 5:
  print('Opção inválida.')

if num == 1:
  num1 = int(input('Escolha o primeiro valor a ser somado: '))
  num2 = int(input('Escolha o segundo valor a ser somado: '))
  num3 = num1 + num2
  print(f'O resultado é: {num3}.')
if num == 2:
  num1 = int(input('Escolha o primeiro valor a ser feito a diferença: '))
  num2 = int(input('Escolha o segundo valor a ser feito a diferença: '))
  num3 = num1 - num2
  print(f'O resultado é: {num3}.')
if num == 3:
  num1 = int(input('Escolha o primeiro valor a ser multiplicado: '))
  num2 = int(input('Escolha o segundo valor a ser multiplicado: '))
  num3 = num1 * num2
  print(f'O resultado é: {num3}.')
if num == 4:
  num1 = int(input('Escolha o primeiro valor a ser dividido: '))
  num2 = int(input('Escolha o segundo valor a ser dividido: '))
  num3 = num1 / num2
  print(f'O resultado é: {num3}.')
