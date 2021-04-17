#vetores
nome = []
sexo = []
sex = ""
cm = 0
cf = 0

#introdução
print("============== Registro com nomes e sexo ===================")

#inserção de dados
for c in range (0,10):
  print("Qual o nome da",c+1,"° pessoa?")
  nome.append(input())
  print("Qual o sexo de",nome[c],"? M ou F")
  sexo.append(input())
  sex = "".join(sexo)
  sex.lower

  if sexo[c] in ("m","masculino","M","Masculino","MASCULINO"):
    cm = cm + 1
  elif sexo[c] in ("f","feminino","F","Feminino","FEMININO"):
    cf = cf + 1
  else:
   print("Sexo inválido")
  print("_________________________________________")
  print(cf,cm)




#retorno dos dados inseridos
print("================= Os dados inseridos foram ==================")
for c in range (0,10):
  print(nome[c],"possui o sexo",sexo[c])
print("____________________________________________________________")
print("A quantidade de sexos definidos foi de",len(sexo) ,"onde",cm,"são do sexo masculino e",cf,"são do sexo feminino")