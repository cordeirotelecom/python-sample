imposto = float(input("Imposto: "))

if imposto < 10.:
    print("Baixo")

elif 10. <= imposto <= 27.:
    print("Médio")

elif 27. < imposto <= 100:
    print("Alto")

else:
    print("Imposto")

imposto2 = float(input("Imposto"))

if imposto2 < 50:
    print("Baixíssimo")

elif 40 <= imposto2 <= 35:
    print("Imposto está na média")

else:
    print("Parabéns seu imposto é ótimo")

