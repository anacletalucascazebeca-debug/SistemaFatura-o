clientes = []
fila_atendimento = []

#Func para Registar Clientes
def registar_cliente():
    print("\n--- Registo de novo cliente ---")
    nome = str(input("Nome do cliente: "))
    genero = str(input("Género (M/F): ")).upper()

    gravida = False
    if genero == "F":
        resposta = input("A cliente está grávida? (s/n): ").lower()
        if resposta == "s":
            gravida = True

    idade = int(input("Idade do cliente: "))
    idoso = idade >= 60

    resposta_def = input("O cliente tem deficiência? (s/n): ").lower()
    deficiencia = resposta_def == "s"

    prioritario = gravida or idoso or deficiencia

    # Compras feitas pelo cli
    qtde_itens = int(input("Quantos produtos o cliente vai registar? "))
    total_compras = 0

    for i in range(qtde_itens):
        print(f'\n=== Produto {i+1} de {qtde_itens}')
        produto = str(input("Produto: "))
        valor_item = float(input("Preço: "))
        total_compras = total_compras + valor_item

    if total_compras > 100000:
        bonus = total_compras * 0.10
    else:
        bonus = 0

    valor_a_pagar = total_compras - bonus

    # Guarda os dados do cli num dic
    cliente = {
        "nome": nome,
        "genero": genero,
        "total_compras": total_compras,
        "bonus": bonus,
        "valor_a_pagar": valor_a_pagar,
        "prioritario": prioritario,
        "gravida": gravida,
        "idoso": idoso,
        "deficiencia": deficiencia,
    }

    clientes.append(cliente)

    # Organiza a fila de atendimento
    if prioritario:
        fila_atendimento.insert(0, cliente)
    else:
        fila_atendimento.append(cliente)

    # imprimir Factura
    print("\n========= Fatura de Compra =========")
    print("Cliente:", nome)
    print(f"Total das compras: {total_compras} Kz")
    if bonus > 0:
        print(f"Bónus: -{bonus} Kz")
    else:
        print("Bónus: não aplicável (compra <= 100 000 Kz)")
    print(f"Valor a pagar: {valor_a_pagar}")

    if prioritario:
        print("Atendimento: Prioritário")
    else:
        print("Atendimento: Normal")


def listar_fila():
    print("\n==== Fila de atendimento (ordem de chamada) ====")
    if len(fila_atendimento) == 0:
        print("Não há clientes registados.")
        return

    posicao = 1
    for cliente in fila_atendimento:
        if cliente["prioritario"]:
            tipo = "Prioritário"
        else:
            tipo = "Normal"
        print(f"{posicao}º - {cliente['nome']} ({tipo})")
        posicao = posicao + 1


def listar_clientes():
    print("\n==== Todos os clientes registados ====")
    if len(clientes) == 0:
        print("Não há clientes registados.")
        return

    for cliente in clientes:
        print("-" * 30)
        print(f"Nome: {cliente['nome']}")
        print(f"Total compras: {cliente['total_compras']} Kz")
        print(f"Bónus: {cliente['bonus']}")
        print(f"Valor a pagar:{cliente['valor_a_pagar']} Kz")


# --- Menu principal ---
while True:
    print("\n******* SISTEMA DE FACTURAÇÂO  ********")
    print("1 - Registar novo cliente")
    print("2 - Ver fila de atendimento")
    print("3 - Ver lista de todos os clientes")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registar_cliente()
    elif opcao == "2":
        listar_fila()
    elif opcao == "3":
        listar_clientes()
    elif opcao == "4":
        print("A sair do sistema. Até breve!")
        break
    else:
        print("Opção inválida. Tente novamente.")
