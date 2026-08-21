import json


print("===============================\nBEM VINDO À BIBLIOTECA: \n===============================")

print("1- Adicionar livro\n2 - Listar livros\n3 - Buscar livro\n4 - Emprestar livro\n5 - Devolver livro\n6 - Remover livro\n7 - Estatísticas\n0 - Sair")  # Menu para o usuário escolher opções

opcao = int(input("Escolha uma opção: "))

match opcao: 
    case 1:
        print("===============================\nInforme os dados do livro.\n") 

        titulolivro = input("Titulo: ")           #cadastro do livro
        autorlivro = input("Autor: ")
        generolivro = input("Gênero: ")
        numeropaginas = int(input("Numero de páginas: "))
        anopublicacao = int(input("Ano de publicação: "))
        isbnlivro = input("ISBN: ")

        novo_livro = {
            "Titulo": titulolivro,           # dicionário python dos livros
            "Autor": autorlivro,
            "Gênero": generolivro,
            "Numero de páginas": numeropaginas,
            "Ano de publicação": anopublicacao,
            "ISBN": isbnlivro
        }

        try:
            with open("livros.json","r",encoding="utf-8") as arquivo:   # carrega os dados
                livros = json.load(arquivo)                             # dos livros existentes

        except FileNotFoundError:
            livros = []

        livros.append(novo_livro)              #adiciona mais livros cadastrados no arquivo json


        with open("livros.json", "w", encoding="utf-8") as arquivo:
            json.dump(livros, arquivo, indent=4, ensure_ascii=False)
            
        print("Livro cadastrado com sucesso!\n===============================")

    case 6:
        print("===============================\n1- Titulo\n2- ISBN")   # adiciona a opção de procura para o
        opcaoremocao = int(input("Como deseja procurar seu livro para remove-lo? "))    # usuário

        match opcaoremocao:
            case 1:
                titleremove = input("Insira o titulo do livro: ")         # podendo escolher entre remover po
                                                                          # titulo ou ISBN
                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                for livro in livros:
                    if livro["Titulo"] == titleremove:
                        livros.remove(livro)
                        print("Livro removido com sucesso!")
                        break
                    else:
                        print("Este titulo não está na biblioteca.")
                        break
                

                with open("livros.json", "w", encoding="utf-8") as arquivo:
                    json.dump(livros, arquivo, indent=4, ensure_ascii=False)

            case 2:
                isbnremove = input("Insira o ISBN do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                for livro in livros:
                    if livro["ISBN"] == isbnremove:
                        livros.remove(livro)
                        print("Livro removido com sucesso!")
                        break
                    else:
                        print("Este ISBN não está na biblioteca.")
                        break
                    

                with open("livros.json", "w", encoding="utf-8") as arquivo:
                    json.dump(livros, arquivo, indent=4, ensure_ascii=False)


