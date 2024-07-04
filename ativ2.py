# #ativ37
# ano = int(input("dgt um ano: "))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
# print (f"{ano} e um, ano bi")

# else:
# print (f"{ano}não e um ano bi")

#exemplo
# while True:
#     numero =  int(input("entre com um numero: ou digite  -1 para parar:"))
#     if numero == -1:
#         break
#     print(numero ** 2)

# print("programa encerrado, obrigada!")

# while True:
#     codigo = input("por favor, insira o PIN: ")
#     if codigo == "1234" :
#         break
#     print("encerado!... tente de novo")
# print("PIN correto! obrigada!")

#atividade38

# while True:
#     pergunta = input("ola! você quer continuar?")
#     if pergunta == "não" :
#      break
#     print("não aceitamos essa resposta")
# print("okay! ate a proxima!")

#ativ39
 
# from math import sqrt
# while True:
#    nmr = int(input("dgt um numero inteiro: "))
#    raiz = sqrt(nmr)
#    print(f"raiz de {nmr} é {raiz:.2f}")
#    if nmr == 0 :
#     break

#ativ40
# numero = 5
# print("contagem regressiva!")
# while True:
#     print(numero)
#     numero = numero - 1
#     if numero == 0:
#         break
# print("foiii!")
    
#ativ41
# while True:
#   nmr = int(input("Digite a sua senha: "))
#   nmr2 = int(input("confirme a senha: "))
#   if nmr == nmr2:
#     break
#   print(int(input("digite novamente: ")))
#   print("senha confirmada!")
  
#exemplo:
# tentativas = 0
# while True:
#   codigo = input("por favor, digite seu PIN: ")
#   tentativas += 1
#   if codigo == "1234" :
#     sucesso = True
#     break
#   if tentativas == 3:
#     sucesso = False
#     break
#   print("incorreto... tente novamente")
# if sucesso:
#     print("PIN correto inserido!")
# else:
#    print("muitas tentativas...")

   #ativ42
# tentativas = 0
# while True:
#   codigo = input("por favor, digite seu PIN: ")
#   tentativas += 1
#   if codigo == "4321" :
#     sucesso = True
#    0, break
#   if tentativas == 3:
#     sucesso = False
#     break
#   print("incorreto... tente novamente")
# if sucesso:
#     print("PIN correto inserido!")
# else:
#    print("muitas tentativas...")

#ativ43

#exemplo2
# numero = int(input("por favor, digite um numero: "))

# while numero < 10:
#     print(numero)
#     numero += 1
#     print("execução finalizada.")

#ativ44

#exemplo03
# import re
# print(re.sezrch("A-Z", "Senha"))
# print(re.search("a-Z", "Senha"))
# print(re.search("0-9", "Senha"))

# import random
# numero_secreto = random.randint(1, 100)
# print(numero_secreto)

#ativ50
 # import