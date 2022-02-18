
try:
    inteiro = int(input("Digite um número inteiro: "))
    if inteiro%2 == 1:
      print("O número digitado é ímpar.")
    else:
        print("O número digitado é par.")
except:
    print("Você não digitou um número inteiro")
