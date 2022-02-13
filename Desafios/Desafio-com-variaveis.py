nome = input("Qual é o seu nome? ")
idade = int(input("Qual idade você vai completar/completou esse ano? "))
altura = float(input("Qual é a sua altura? "))
peso = float(input("Qual é o seu peso? "))
ano_atual = int(input("Em que ano estamos? "))
imc = peso/altura**2

print(f"{nome} tem {idade} anos de idade.")
print(f"Seu IMC é {imc:.2f}.")
print(f"Ele nasceu no ano de {ano_atual - idade}.")
