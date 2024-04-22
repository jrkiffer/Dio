menu = """

Sistema Bancário ficticio da DIO

Selecione uma das opções abaixo:

[ 1 ] Depósito
[ 2 ] Saque
[ 3 ] Extrato
[ 0 ] Sair

Digite a opção: 
"""

saldo = 0
limite = 1000 # Limite diário será de R$ 1000
extrato = ""
numero_saques = 0
limite_diario_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Seu novo saldo é de R${saldo:.2f}")
        else:
            print("Operação falhou. O valor informado para depósito é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_diario_saques

        if excedeu_saldo:
            print(f"Você excedeu o limite para saque. Você está tentando sacar R${valor:.2f}, mas o seu saldo é de R${saldo:.2f}")

        elif excedeu_limite:
            print(f"O valor informado é maior que o limite para saque. O valor máximo para saque é de R$ 1000")

        elif excedeu_saques:
            print(f"Você excedeu o limite diário de saques que é de {limite_diario_saques}.")

        elif valor > 0:
            saldo = saldo - valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques = numero_saques + 1
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso. Seu novo saldo é de {saldo:.2f}")
        else:
            print(f"Operação falhou. O valor informado é inválido.")

    elif opcao == "3":
        print(f"#####EXTRATO#####")
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"################")

    elif opcao == "0":
        break

    else:
        print(f"Operação inválida, por favor selecione outra opção.")