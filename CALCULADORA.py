#CALCULADORA OPERAÇÕES MATEMÁTICAS SIMPLES

num1 = 0
num2 = 0
resultado = 0
operacao = ''

print('CALCULADORA SIMPLES \n+ para adição \n- para subtração \n* para multiplicação \n/ para divisão \nx para sair')


while True:
  try:
    operacao = input('Digite a operação ou código de saída: ')
    if operacao == 'x' or operacao == 'X':
      break
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
      
    if operacao == '+':
      resultado = num1 + num2
      print(str(num1), operacao, str(num2), ' = ', (resultado))
    elif operacao == '-':
      resultado = num1 - num2
      print(str(num1), operacao, str(num2), ' = ', (resultado))
    elif operacao == '*':
      resultado = num1 * num2
      print(str(num1), operacao, str(num2), ' = ', (resultado))
    elif operacao == '/':
      resultado = num1/num2
      print(str(num1), operacao, str(num2), ' = ', (resultado))
    else:
      print('OPERAÇÃO INVÁLIDA')
  except ValueError:
    print(f'ALGO DEU ERRADO. VERIFIQUE SE ESTÁ SEGUINDO OS COMANDOS CORRETOS.')





