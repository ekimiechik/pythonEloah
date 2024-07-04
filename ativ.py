# #atividade 01
# nome = input("Digite seu nome")
# print("Nome próprio:" + nome)

# apelido = input("Digite seu apelido")
# print("apelido:" + apelido)

# endereço = input("Digite seu endereço")
# print("endereço:" + endereço)

# cdd = input("Digite sua cidade e código postal")
# print("cidade e código postal:" + cdd)

# print(endereço + cdd) 


# #atividade 02
# nome2 = input("por favor digite um nome:")
# print(nome2)

# ano = input("por favor digite um ano:")
# print(ano)

# #atividade 03
# sp = "Rio de Janeiro"
# print(sp)
# sp = "São Paulo"
# print(sp)

# #atividade04
# letra = "E"
# print(letra)
# nmr = 45
# print(nmr)
# float = ('54')
# print(float)

# #atividade05
# nome3 = ("A eloah")
# nome4 = (" é linda")
# print(nome3 + nome4)

# #atividade06
# usuário = int(input("Coloque seu nmr aqui: "))
# print(f"o resultado é {usuário * 5}")

# #if e else

# idade = 16
# if idade >=18:
#     print("Você é maior de idade")

#ativ07
# nome = input("qual o seu nome? ")
# ano = input("que ano vc nasceu?")
# print(f"oça {nome}, voce fará {2024 - ano} anos esse ano!")

#ativ08
# precinho = flat(input("dgt o preço do produto: "))
# desconto = int(input("qual a porcentagem do decontinho? "))
# precoDescontinho = precinho*desconto
# valorfinal = precoDescontinho / 100
# print(f"o valor é: ")


# #02

# numero = int(input("entre com um numero: "))
# if numero > 0:
#     print("esse numero é positivo")
# if numero ==  0:
#     print("esse numero é 0" )

#     #03


# #ativ16
# nmr1 = int(input("escreva um numero: "))
# if nmr1 < 0:
#     calculo = nmr * -1
#     print(calculo)

# #ativ17
# nm = input("digite your nombre:")
# porcaozinha = int(input("que quantidade o senhore irá querer?  "))
# preco_porcaozinha = 5,90
# if nm != "jerry":
#     print (preco_porcaozinha * porcaozinha)

#ativ18
# numero = int(input("dgt um numero: "))
# if numero < 1000:
#   print("esse numero é menor que 1000")
# if numero > 1000:
#   print("obg")
# if numero < 10 <100 < 1000:
#   print("esse numero é menor que 1000, menor que 100e menor 10!!!!!!")

# #ativ19
# nm2 = "pedro" 
# cdd = "curitiba"
# estado = "parana"
# cep = "81064598"

# nominho = input ("digite seu nome: ")

# if nominho == nm2:
#    print(f"nome: {nm2}")
#    print(f"cidade: {cdd}")
#    print(f"estado: {estado}")
#    print(f"cep: {cep}")

#ex1
# c1 = 9 == 5
# c2 = 9 > 5
# c3 = 9 < 5

# #ex2
# a = 3
# condicao = a < 5
# print(condicao)
# if condicao:
#     print("a é menor que 5")

# #ativ20
# nmr1 = float(input(12))
# nmr2 = float(input(21))

# if operacaozinha == "add":
# resultado = nmr1 + nmr2
# print(f"resultado:(resultado)")

# if

#ativ22
# salariohora = float(input("qual o seu salario /h: "))
# day = (input("escolha um dia da smana: "))
# horas = float(input("qnts horas trabalhei: "))

# dindin = salariohora * horas
# folga = "domingo"

# if day == folga:
#     print("seu salário trabalhado no mês: ", dindin * 2)
#     print("salário dos dias trabalhados durante a semana: " , dindin)

#ativ23
# pts = int(input("dgt a qntd de pontos no cartão: "))
# if pts < 100:
#     taxa_de_bonus = 0.10
# if pts < 100:
#     taxa_de_bonus = 0.15
# bonus = pts * taxa_de_bonus
# print(f"o bonus é: {bonus:.2f} pts")


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
 