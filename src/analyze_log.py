import csv


def top_receitas(dados, cliente):
    mais_pedidas = ""
    pedidos_clientes = {}

    for nome, pedido, dia in dados:
        if nome == cliente:
            if pedido not in pedidos_clientes:
                pedidos_clientes[pedido] = 1
            else:
                pedidos_clientes[pedido] += 1

            if (
                mais_pedidas not in pedidos_clientes
                or pedidos_clientes[pedido] > pedidos_clientes[mais_pedidas]
            ):
                mais_pedidas = pedido

    return mais_pedidas


def qtd_pedida(dados, cliente, receita):
    quantidade = 0

    for nome, pedido, dia in dados:
        if nome == cliente and pedido == receita:
            quantidade += 1

    return quantidade


def pega_receita_nunca_pedida(dados, cliente):
    receita_restaurante = set()
    receita_cliente = set()

    for nome, pedido, dia in dados:
        receita_restaurante.add(pedido)

        if nome == cliente:
            receita_cliente.add(pedido)
    return receita_restaurante.difference(receita_cliente)


def pega_dias_sem_ir(dados, cliente):
    dias_abertos = set()
    dias_comparecidos = set()

    for nome, pedido, dia in dados:
        dias_abertos.add(dia)
        if nome == cliente:
            dias_comparecidos.add(dia)
    return dias_abertos.difference(dias_comparecidos)


def analyse_log(path_to_file):
    with open(path_to_file, "r") as arquivo_de_pedidos:
        conteudo = csv.reader(arquivo_de_pedidos, delimiter=",")
        dados = [*conteudo]

        receita_mais_solicitada = top_receitas(dados, "Maria")
        qtd_receita_pedida = qtd_pedida(dados, "arnaldo", "hamburguer")
        receita_nunca_pedida = pega_receita_nunca_pedida(dados, "joao")
        dias_sem_ir = pega_dias_sem_ir(dados, "joao")

        with open("data/mkt_campaign.txt", "w") as arquivo_de_marketing:
            print(
                receita_mais_solicitada,
                qtd_receita_pedida,
                receita_nunca_pedida,
                dias_sem_ir,
                sep="\n",
                file=arquivo_de_marketing,
            )
