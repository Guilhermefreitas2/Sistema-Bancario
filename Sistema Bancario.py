limite_saque = 3
valor_extrato = []
contador_saque = 0 
saldo = 0

def deposito(saldo):
    valor_deposito = int(input("Digite o valor do depósito: R$"))

    while valor_deposito <= 0:
        print("\nDigite um valor acima de 1")
        valor_deposito = int(input("Digite o valor do depósito: R$"))
    
    valor_extrato.append(valor_deposito)
    saldo += valor_deposito
    print(f"Saldo atual: R${saldo:.2f}")
    print("Valor adicionado com sucesso")
    print("Extrato atual:", valor_extrato)
    return saldo

def saque(saldo, contador_saque, limite_saque):
    if contador_saque >= limite_saque:
        print("Limite de saques atingido.")
        return saldo, contador_saque
    
    valor_saque = int(input("Digite o valor do saque R$"))
    while valor_saque <= 0:
        print("\nDigite um valor acima de 1.")
        valor_saque = int(input("Digite o valor do saque: R$"))

    if valor_saque > saldo:
        print("Saldo insuficiente para este saque.")
        return saldo, contador_saque 

    valor_extrato.append(-valor_saque)
    saldo -= valor_saque
    contador_saque += 1  
    print(f"Saque realizado com sucesso. Saldo atual: R${saldo:.2f}")
    print("Extrato atual:", valor_extrato)
    return saldo, contador_saque  
def extrato():
    print("Extrato de transações:")
    

##############################################################################################
while True:
    print("\n[1] - Depósito\n[2] - Saque\n[3] - Extrato\n[0] - Sair")
    menu = int(input("\nDigite a operação que deseja: "))

    if menu == 1:
        saldo = deposito(saldo)

    elif menu == 2:
        saldo, contador_saque = saque(saldo, contador_saque, limite_saque)  

    elif menu == 3:
        extrato()

    elif menu == 0:
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Valor não aceito. Tente novamente.")
