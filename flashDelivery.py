import os

entregas = []

def calcularFrete(distancia, pesoPacote):
    taxaBase = 10.00
    adicionalKm = distancia * 1.50
    
    if pesoPacote > 5:
        taxaPeso = 15.00
    else:
        taxaPeso = 0.00
    
    valorTotal = taxaBase + adicionalKm + taxaPeso
    return valorTotal

def cadastroEntrega():
    print("\n===== CADASTRAR ENTREGA =====")
    idPedido = int(input('ID: '))
    nomeCliente = input('Nome: ').capitalize()
    distancia = float(input('Distância (km): '))
    pesoPacote = float(input('Peso do Pacote (kg): '))
    status = 'Pendente'
    
    valorFrete = calcularFrete(distancia, pesoPacote)

    novaEntrega = {
        'id': idPedido,
        'cliente': nomeCliente,
        'distancia': distancia,
        'peso': pesoPacote,
        'status': status,
        'frete': valorFrete  
    }

    entregas.append(novaEntrega)
    print(f'\nEntrega ID:{idPedido} cadastrada com sucesso!')
    print(f'Valor do frete: R$ {valorFrete:.2f}')  

def listarEntrega ():
    print("\n===== ENTREGAS CADASTRADAS =====")

    for entrega in entregas:
        print(f"\nID: {entrega['id']}")
        print(f"Nome do Cliente: {entrega['cliente']}")
        print(f"Distância em km: {entrega['distancia']}")
        print(f"Peso do Pacote: {entrega['peso']}")
        print(f"Status: {entrega['status']}")
        print(f"Frete: R${entrega['frete']}")

while True:
    print('\n======== FLASH DELIVERY ========')
    print('')
    print('1. Cadastrar nova entrega')
    print('2. Calcular valor do frete')
    print('3. Listar todas as entregas')
    print('4. Alterar status')
    print('5. Sair')
    print('--------------------------------')
    opcaoDoMenu = int(input('Digite a sua opção: '))

    if opcaoDoMenu == 1:
        os.system('cls')
        cadastroEntrega()
        input("\nPressione Enter para continuar...")
        os.system('cls')

    elif opcaoDoMenu == 2:
        os.system('cls')
        print("\n===== CALCULADORA DE FRETE =====")
        distancia = float(input("Distância (Km): "))
        peso = float(input("Peso do pacote (Kg): "))
        resultado = calcularFrete(distancia, peso)
        print(f"\nDistância: {distancia} Km")
        print(f"Peso: {peso} Kg")
        print(f"Valor do frete: R${resultado:.2f}")
        input("\nPressione Enter para continuar...")
        os.system('cls')

    elif opcaoDoMenu == 3:
        os.system('cls')
        listarEntrega ()
        input("\nPressione Enter para continuar...")
        os.system('cls')
      
    elif opcaoDoMenu == 4:
        os.system('cls')
        print("\n===== ALTERAR STATUS =====")
        idBusca = int(input("ID do pedido: "))    
            
        for entrega in entregas:
            if entrega['id'] == idBusca:
                print(f"\nEntrega encontrada:")
                print(f"Cliente: {entrega['cliente']}")
                print(f"Distância: {entrega['distancia']} Km")
                print(f"Peso: {entrega['peso']} Kg")
                print(f"Status atual: {entrega['status']}")
                
                opcaoEntrega = input("\nConfirmar entrega? (s/n): ").lower()
                if opcaoEntrega == 's':
                    entrega['status'] = 'Entregue'
                    print("Entrega confirmada!")
                else:                        
                    print("Pendente")
                    break  
            else:
                print(f"Pedido ID:{idBusca} não encontrado.")
        
        input("\nPressione Enter para continuar...")
        os.system('cls')

    elif opcaoDoMenu == 5:
        os.system('cls')
        print('\n-----------------------------')
        print('     Saindo do Sistema...')
        print('')
        break

    else:
        os.system('cls')
        print('\n-----------------------------')
        print('Digite um número entre 1 - 5')
        input("\nPressione Enter para continuar...")
        os.system('cls')