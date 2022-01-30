nome = input("Qual é o seu nome: ")
idade = int(input("Qual é a sua idade? "))
peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso / (altura**2) #Não precisava do parentesis pois a exponenciação tem a maior precedência aqui

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)
