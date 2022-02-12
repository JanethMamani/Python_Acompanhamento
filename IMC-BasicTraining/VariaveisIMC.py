nome = input("Qual é o seu nome: ")
idade = int(input("Qual é a sua idade? "))
peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso / (altura**2) #Não precisava do parentesis pois a exponenciação tem a maior precedência aqui

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {2:.2f} de imc e {0} tem {1} de idade'.format(nome, idade, imc))
print('{n} tem {im:.2f} de imc e {n} tem {i} de idade'.format(n=nome, i=idade, im=imc))