menu = """
[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else: 
            print("Operação falhou. O valor inserido é inválido!")      

    elif opcao =="S":  
        valor = float(input("Insira o valor do saque: "))     

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo excedido!") 
        elif excedeu_limite:
            print("Limite excedido!")
        elif excedeu_saques:
            print("Limit de saques!") 

        elif valor > 0:
            saldo -= valor
            extrato +=  f"Saque: R$ {valor:.2f}\n"  
            numero_saques += 1

        else: 
            print("Operação inválida! O valor informado é inválido!")

    elif opcao == "E":
        print("\n ########################### Extrato #############################")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print("##############################################")

    
    elif opcao == "Q":
        break        

    else:
        print("Operação inválida! Por favor selecione a opção desejada!")   