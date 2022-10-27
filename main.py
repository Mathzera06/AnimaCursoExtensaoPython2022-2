nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))
if nota == 10:
  print(f"{nome}, voce é o bichão mesmo")
elif (nota >= 6 and nota <= 9.99):
  print(f"{nome}, voce é mediano")
else:
  print("Não tirou dez")