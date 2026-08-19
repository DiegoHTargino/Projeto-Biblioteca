import json


print("===============================\nBEM VINDO À BIBLIOTECA: \n===============================")

print("1- Adicionar livro\n2 - Listar livros\n3 - Buscar livro\n4 - Emprestar livro\n5 - Devolver livro\n6 - Remover livro\n7 - Estatísticas\n0 - Sair")  # Menu para o usuário escolher opções

opcao = int(input("Escolha uma opção: "))

match opcao: 
    case 1:
        print("===============================\nInforme os dados do livro.\n")
        titulolivro = input("Titulo: ")
        autorlivro = input("Autor: ")
        generolivro = input("Gênero: ")
        numeropaginas = int(input("Numero de páginas: "))
        anopublicacao = int(input("Ano de publicação: "))
        isbnlivro = input("ISBN: ")
        print("Livro cadastrado com sucesso!\n===============================")



                    