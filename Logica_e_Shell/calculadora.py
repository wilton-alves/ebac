# Calculadora que exibe o devido retorno para cada uma das quatro operações
# básicas da matemática a partir da entra de dois números pelo usuário

print('Olá! Informe dois números que eu irei realizar as quatro operações básicas da matemática para você.\n')


# laço de repetição onde o processo será executado até que o usuário encerre digitando 0 (zero)

opt = 1
while opt != 0:

  # recebe os números para efetuar as operações matemáticas e converte para float
  num1 = float(input('Digite o primeiro número: '))
  num2 = float(input('Digite o segundo número: '))

  # realiza as quatro operações
  print(f'\nA soma de {num1} + {num2} é igual a {num1 + num2}')
  print(f'A subtração de {num1} - {num2} é igual a {num1 - num2}')
  print(f'A multiplicação de {num1} * {num2} é igual a {num1 * num2}')

  # para a divisão é necessário um condicional pois não é possível dividir por zero
  if num2 == 0:
    print('Não é possível dividir por zero')
  else:
    print(f'A divisão de {num1} / {num2} é igual a {num1 / num2}')

  opt = int(input('\nDeseja realizar um novo cálculo?\n1 para Sim\n0 para Não\n'))

print('Obrigado, tenha um bom dia!')
