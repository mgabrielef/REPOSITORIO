altura = float(input('Qual a sua altura?'))
peso = float(input('Qual o seu peso? '))
IMC = peso/(altura * altura)

if IMC < 18.5:
  print(f'Seu IMC é igual a {IMC:.2f}kg/m².')
  print(f'Você se encontra na categoria MAGREZA.')
elif IMC <= 24.9:
  print(f'Seu IMC é igual a {IMC:.2f}kg/m².')
  print(f'Você se encontra na categoria PESO IDEAL.')
elif IMC <= 29.9:
  print(f'Seu IMC é igual a {IMC:.2f}kg/m².')
  print(f'Você se encontra na categoria SOBREPESO.')
elif IMC <= 39.9:
  print(f'Seu IMC é igual a {IMC:.2f}kg/m².')
  print(f'Você se encontra na categoria OBESIDADE.')
else:
  print(f'Seu IMC é igual a {IMC:.2f}kg/m².')
  print(f'Você se encontra na categoria OBESIDADE GRAVE.')