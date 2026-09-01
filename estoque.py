# Grente inteligente, sistema de teste reciclado
# Regivan; RU 5340594

# Produtos já cadrastrados
produtos = {
    "1": {"nome": "Caderno de capa dura ", "quantidade": 11},
    "2": {"nome": "Caixa de caneta azul", "quantidade": 67},
    "3": {"nome": "Tinta para impressora", "quantidade": 0},
    "4": {"nome": "Pacote de lapís", "quantidade": 0},
    "5": {"nome": "Pacote de papel A4", "quantidade": 9},
    "6": {"nome": "Placa de video de Pc ", "quantidade": 2}
}

# Lista para guardar o histórico de movimentações de entradas e saídas
historico_movimentacoes = []


def exibir_estoque():
    """Mostra os produtos disponíveis e seus saldos."""
    print("\n--- ESTOQUE ATUAL ---")
    for codigo, info in produtos.items():
        print(f"[{codigo}] Produto: {info['nome']} | Saldo: {info['quantidade']} unidades")
    print("       ")


def registrar_entrada():
    """Registra a entrada de produtos e atualiza o saldo."""
    exibir_estoque()
    codigo = input("Digite o código do produto para a ENTRADA: ")

    if codigo in produtos:
        try:
            qtd = int(input("Informe a quantidade recebida: "))
            if qtd <= 0:
                print(" A quantidade deve ser maior que zero, viu !")
                return

            data = input("Informe a data da entrada (ex: DD/MM/AAAA): ")

            # Critério: O estoque do produto deve ser atualizado automaticamente
            produtos[codigo]["quantidade"] += qtd

            # Registrando no histórico
            registro = f" ENTRADA | Data: {data} | Produto: {produtos[codigo]['nome']} | Qtd: {qtd}"
            historico_movimentacoes.append(registro)

            print(f"\n Sucesso! O estoque de {produtos[codigo]['nome']} subiu para {produtos[codigo]['quantidade']}.")
        except ValueError:
            print("Erro: Digite um número inteiro válido para a quantidade.")
    else:
        print("Produto não encontrado!")


def registrar_saida():
    """Registra a saída de produtos, validando o saldo."""
    exibir_estoque()
    codigo = input("Digite o código do produto para SAÍDA: ")

    if codigo in produtos:
        try:
            qtd = int(input("Informe a quantidade retirada: "))
            if qtd <= 0:
                print("A quantidade deve ser maior que zero!")
                return

            # Critério: Deve validar se há quantidade suficiente no estoque
            if qtd > produtos[codigo]["quantidade"]:
                print(f"Erro de Validação: Saldo insuficiente! Só há {produtos[codigo]['quantidade']} unidades.")
            else:
                data = input("Informe a data da retirada (ex: DD/MM/AAAA): ")
                responsavel = input("Informe o nome do responsável pela retirada: ")

                # Atualiza o estoque
                produtos[codigo]["quantidade"] -= qtd

                # Critério: O sistema deve registrar a movimentação com data e responsável
                registro = f"SAÍDA   | Data: {data} | Produto: {produtos[codigo]['nome']} | Qtd: {qtd} | Responsável: {responsavel}"
                historico_movimentacoes.append(registro)

                print(
                    f"\n Sucesso! Saída registrada. Novo saldo de {produtos[codigo]['nome']}: {produtos[codigo]['quantidade']}.")
        except ValueError:
            print(" Erro: Digite um número inteiro válido para a quantidade.")
    else:
        print(" Produto não encontrado!")


def exibir_historico():
    """Mostra os log de todas as movimentações feitas."""
    print("\n---- HISTÓRICO DAS MOVIMENTAÇÕES ---")
    if len(historico_movimentacoes) == 0:
        print("Nenhuma movimentação registrada ainda.")
    else:
        for linha in historico_movimentacoes:
            print(linha)
    print("---------------------")


def menu_principal():
    """Controla o loop do menu principal do sistema."""
    while True:
        print("\n" + "=" * 40)
        print(" OI, ESSE É O GERENTE INTELIGENTE - MENU PRINCIPAL  ")
        print("=" * 40)
        print("1. Registrar entrada de produto")
        print("2. Registrar saída de produto")
        print("3. Consultar estoque")
        print("4. Consultar histórico de movimentações")
        print("5. Sair do sistema")

        opcao = input("Escolha uma das opção (1-5): ")

        if opcao == '1':
            registrar_entrada()
        elif opcao == '2':
            registrar_saida()
        elif opcao == '3':
            exibir_estoque()
        elif opcao == '4':
            exibir_historico()
        elif opcao == '5':
            print("Encerrando o sistema. Valeu prof 8) !")
            break
        else:
            print("Opção inválida. Tente novamente .")

# Ponto de partida do programa
if __name__ == "__main__":
    menu_principal()
