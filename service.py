def listaProdutos(produtos):
    print("Produtos Disponiveis: ")
    for pr in produtos:
        dados = "Código: {0} , Nome: {1}, Descrição: {2}, Valor: {3}"
        print(dados.format(pr[0], pr[1], pr[2], pr[3]))
    print(" ")

def insert():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    valor = float(input("valor: "))

    produto = (nome, descricao, valor)
    return produto

def findByID(produto):
    listaProdutos(produto)
    id = int(input("Informe o código do produto: "))
    produto(id)

def updata(produtos):
    listaProdutos(produtos)
    test = False
    id = int(input("Informe o código do produto: "))
    for prod in produtos:
        if prod[0] == id:
            test = True
            break
    if test:
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        valor = float(input("valor: "))
        produto = (id, nome, descricao, valor)
        return produto

def delete(produtos):
    listaProdutos(produtos)
    id = input("Id: ")
    return id;