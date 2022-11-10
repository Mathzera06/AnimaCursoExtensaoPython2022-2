preco = 19.90
imposto = preco * 0.05
print(imposto)

preco2 = 500
imposto2 = preco2 * 0.05
print(imposto2)

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

preco = 299
calcular_imposto(preco)
print(imposto)