from dao import Dao
import service

def menuPrincipal():
    continuar = True
    while(continuar != False):
        print("####### BARRA DE MENU ######")
        print("1 - Listagem de Produtos")
        print("2 - Inserir Produto")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair \n")

        numero = int(input("Selecione uma opção: "))
        print(" ")
        if numero < 1 or numero > 5:
            print("Opção invalida, tente novamente! \n")
        elif(numero == 5):
            continuar = False
            print("Sessão encerrada!")
            break
        else:
            chamadaOpcao(numero)

def chamadaOpcao(numero):
    dao = Dao()

    if(numero == 1):
        produtos = dao.product_All()
        if(len(produtos) > 0):
             service.listaProdutos(produtos)
        else:
            print("Não foi encontrado nenhum produto \n")

    elif(numero == 2):
        produto = service.insert()
        dao.insert(produto)
        print(" ")

    elif(numero == 3):
       produtos = dao.product_All()
       if(len(produtos) > 0):
            produto = service.updata(produtos)
            if produto:
                dao.update(produto)
            else:
                print("Produto não encontrado")
            print(" ")

    elif(numero == 4):
        produtos = dao.product_All()
        if (len(produtos) > 0):
            produto = service.delete(produtos)
            dao.delete(produto)
            print(" ")
        else:
            print("Não foi encontrado nenhum produto \n")

menuPrincipal()
