#comando input(): quero permitir que o usuário digite algo...
nome = input("Digite seu nome:")
print(nome)

idade = int(input("Digite sua idade:"))
print(idade)

dobro = (idade * 2)
print("o dobro da idade informada é  {}".format(dobro))

genero = input("Informe o seu genero M= Masculino, F=Feminino, O=Outros: ")
if idade >= 18 and genero == "M":
  print("... e voce tambem precisa/precisou prestar o serviço militar")
  
# IF 
# Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir" 



if idade >= 18: 
  print("Você é maior de idade")
else:
  print("Você não é maior de idade")

  