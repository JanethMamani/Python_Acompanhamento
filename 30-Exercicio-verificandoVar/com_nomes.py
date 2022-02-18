nome_ex = len(input("Digite seu primeiro nome: "))
if 0<nome_ex<5:
    print("Seu nome é curto.")
elif 4<nome_ex<7:
    print("Seu nome é normal.")
elif nome_ex>6:
    print("Seu nome é muito grande.")
else:
    print("Não reconheço essa entrada")