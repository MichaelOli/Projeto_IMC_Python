# Entrada de dados IMC = peso / (altura x altura)

nome = input('Informe seu nome, meu mano: ')

# Loop para garantir que o usuário insira um número válido para peso
while True:
    try:
        peso = float(input('Informe seu peso: ').replace(',', '.'))
        break
    except ValueError:
        print('Mano, informe um número válido para o peso, por gentileza...')

# Loop para garantir que o usuário insira um número válido para altura
while True:
    try:
        altura = float(input('Informe sua altura: ').replace(',', '.'))
        break
    except ValueError:
        print('Mano, informe um número válido para a altura, por gentileza...')

# Calculo do IMC = peso / (altura x altura)
resultado = peso / (altura ** 2)
resultado = round(resultado, 2)

# Condicional para exibição do resultado
if resultado < 18.5:
    print(f'O resultado do seu IMC: {resultado}. MAGREZA demais cê é louco {
          nome}, bora ir atrás de uns hipercalórico, mano vei...')
elif 18.5 <= resultado <= 24.9:
    print(f'{nome}. Seu peso é Normal, mas ainda é frango, se liga no resultado: {
          resultado}')
elif 25.0 <= resultado <= 29.9:
    print(f'Mano, você tá com SOBREPESO, olha isso {
          resultado}, ainda dá tempo de cuidar')
elif 30 <= resultado <= 39.9:
    print(f'{resultado}, Cê é louco tio, OBESIDADE II, bora se cuidar né, {nome}')
else:  # resultado > 40
    print(f'{resultado}. OBESIDADE GRAVE de grau III, {
          nome}, cancela sua conta do iFood')
