try:
    horas = int(input("Digite as horas no formato 'hh': "))
    if 0<=horas<=11:
        print("Bom dia!")
    elif 12<=horas<=17:
        print("Boa tarde!")
    elif 18<=horas<=23:
        print("Boa noite!")
    else:
        print("Essa hora não existe.")
except:
    print("Digite as hora no formato hh(número inteiro).")