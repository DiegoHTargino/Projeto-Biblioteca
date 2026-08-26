import json


print("===============================\n~ BEM  VINDO À BIBLIOTECA ~ \n===============================")

print("1 - Adicionar livro\n2 - Listar livros\n3 - Buscar livro\n4 - Emprestar livro\n5 - Devolver livro\n6 - Remover livro\n7 - Estatísticas\n0 - Sair")  # Menu para o usuário escolher opções

opcao = int(input("Escolha uma opção: "))

match opcao: 
    case 1:
        print("\n===============================\n~ CADASTRO DE LIVROS ~ \n===============================")
        print("Informe os dados do livro.\n") 

        titulolivro = input("Titulo: ")           #cadastro do livro
        autorlivro = input("Autor: ")
        generolivro = input("Gênero: ")
        numeropaginas = int(input("Numero de páginas: "))
        anopublicacao = int(input("Ano de publicação: "))
        isbnlivro = input("ISBN: ")
        statuslivro = input("Status: ")

        novo_livro = {
            "Titulo": titulolivro,           # dicionário python dos livros
            "Autor": autorlivro,
            "Gênero": generolivro,
            "Numero de páginas": numeropaginas,
            "Ano de publicação": anopublicacao,
            "ISBN": isbnlivro,
            "Status": statuslivro
        }

        try:
            with open("livros.json","r",encoding="utf-8") as arquivo:   # carrega os dados
                livros = json.load(arquivo)                             # dos livros existentes

        except FileNotFoundError:
            livros = []

        livros.append(novo_livro)              #adiciona mais livros cadastrados no arquivo json


        with open("livros.json", "w", encoding="utf-8") as arquivo:
            json.dump(livros, arquivo, indent=4, ensure_ascii=False)
            
        print("\nLivro cadastrado com sucesso!\n===============================")

    case 2:
            print("\n===============================\n~ LISTA DE LIVROS ~ \n===============================")

            with open("livros.json","r",encoding="utf-8") as arquivo:   
                livros = json.load(arquivo)

            print("Os livros cadastrados são:\n")
            for livro in livros:
                print('- ' + livro['Titulo'] + ' - (' + livro['Autor'] + ').') 
            print("===============================")
                  

    case 3:
        print("\n===============================\n~ BUSCA DE LIVROS ~ \n===============================")
        print("\n1- Titulo\n2- ISBN")   # adiciona a opção de procura para o
        opcaoprocura = int(input("\nComo deseja procurar seu livro? "))

        match opcaoprocura:
            case 1:     
                titlesearch = input("Insira o titulo do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                encontrado = False 

                for livro in livros:
                    if livro["Titulo"] == titlesearch:                
                        print("===============================\n") 
                        print("===============================\n~ INFORMAÇÕES DO LIVRO ~ \n===============================")   
                        print("Nome: " + livro['Titulo'] + "\n"  + "Autor:" + livro['Autor'])
                        print("Gênero: " + livro['Gênero'] + "\n" + "Número de páginas: " + str(livro['Numero de páginas']))
                        print("ISBN: " + livro['ISBN'])
                        print("Status: " + livro['Status']) 
                        encontrado = True
                        break
                
                if encontrado == True:
                    with open("livros.json", "w", encoding="utf-8") as arquivo:
                        json.dump(livros, arquivo, indent=4, ensure_ascii=False)
                
                    print("\nLivro achado com sucesso!\n===============================")
                else:
                    print("\nEste título não está na biblioteca.\n===============================")
            case 2:     
                isbnsearch = input("Insira o ISBN do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                encontrado = False 

                for livro in livros:
                    if livro["ISBN"] == isbnsearch:                
                        print("===============================\n")        
                        print("Nome: " + livro['Titulo'] + "\n"  + "Autor:" + livro['Autor'])
                        print("Gênero: " + livro['Gênero'] + "\n" + "Número de páginas: " + str(livro['Numero de páginas']))
                        print("ISBN: " + livro['ISBN'])
                        encontrado = True
                        break
                
                if encontrado == True:
                    with open("livros.json", "w", encoding="utf-8") as arquivo:
                        json.dump(livros, arquivo, indent=4, ensure_ascii=False)
                
                    print("\nLivro achado com sucesso!\n===============================")
                else:
                    print("\nEste título não está na biblioteca.\n===============================")   

            case _:
                    print("\nOpção inválida.")   
    case 4:
        print("\n===============================\n~ EMPRÉSTIMO DE LIVROS ~ \n===============================\n")
        print("1- Titulo\n2- ISBN\n")
        opcaoaluguel = int(input("Digite como quer alugar seu livro: "))

        match opcaoaluguel:
            case 1: 
                opcaoaluguelT = input("Digite o titulo do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                encontrado = False

                for livro in livros:
                    if livro['Titulo'] == opcaoaluguelT:
                        encontrado = True
                        if livro['Status'] == "Disponível":
                            livro['Status'] = "Alugado"

                            with open("livros.json", "w", encoding="utf-8") as arquivo:
                                json.dump(livros, arquivo, indent=4, ensure_ascii=False)

                                print("\nLivro alugado com sucesso!\n===============================")
                        else:
                            print("\nEste livro já está alugado.\n===============================")

                        break

                if encontrado == False:
                    print("Este livro não foi encontrado.\n===============================")
            case 2:
                opcaoaluguelISBN = input("Digite o ISBN do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                encontrado = False

                for livro in livros:
                    if livro['ISBN'] == opcaoaluguelISBN:
                        encontrado = True
                        if livro['Status'] == "Disponível":
                            livro['Status'] = "Alugado"

                            with open("livros.json", "w", encoding="utf-8") as arquivo:
                                json.dump(livros, arquivo, indent=4, ensure_ascii=False)

                                print("\nLivro alugado com sucesso!\n===============================")
                        else:
                            print("\nEste livro já está alugado.\n===============================")

                        break

                if encontrado == False:
                    print("\nEste livro não foi encontrado.\n===============================")
            case _:
                print("\nOpção inválida.")

    case 5:
        print("\n===============================\n~ DEVOLUÇÃO DE LIVROS ~ \n===============================\n")
        print("1- Titulo\n2- ISBN\n")
        opcaodevolucao = int(input("Como deseja procurar seu livro para devolve-lo? "))

        match opcaodevolucao:
            case 1: 
                opcaodevolucaotitulo = input("Digite o titulo do livro: ")
        
                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)
        
                encontrado = False
        
                for livro in livros:
                    if livro['Titulo'] == opcaodevolucaotitulo:
                        encontrado = True
                        if livro['Status'] == "Alugado":
                            livro['Status'] = "Disponível"
        
                            with open("livros.json", "w", encoding="utf-8") as arquivo:
                                json.dump(livros, arquivo, indent=4, ensure_ascii=False)
        
                            print("\nLivro devolvido com sucesso!\n===============================")
                        else:
                            print("\nEste livro já foi devolvido.\n===============================")
        
                            break
        
                        if encontrado == False:
                            print("Este livro não foi encontrado.")
            case 2:
                opcaodevolucaoisbn = input("Digite o ISBN do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                encontrado = False
        
                for livro in livros:
                    if livro['ISBN'] == opcaodevolucaoisbn:
                        encontrado = True
                        if livro['Status'] == "Alugado":
                            livro['Status'] = "Disponível"
        
                            with open("livros.json", "w", encoding="utf-8") as arquivo:
                                json.dump(livros, arquivo, indent=4, ensure_ascii=False)
        
                            print("\nLivro devolvido com sucesso!\n===============================")
                        else:
                            print("\nEste livro já foi devolvido.\n===============================")
        
                            break
        
                        if encontrado == False:
                            print("\nEste livro não foi encontrado.\n===============================")

            case _:
                print("\nOpção inválida.")
    case 6:
        print("\n===============================\n~ REMOÇÃO DE LIVROS ~ \n===============================")
        print("\n1- Titulo\n2- ISBN")   # adiciona a opção de procura para o
        opcaoremocao = int(input("\nComo deseja procurar seu livro para remove-lo? "))    # usuário

        match opcaoremocao:
            case 1:
                titleremove = input("Insira o titulo do livro: ")         # podendo escolher entre remover po
                                                                          # titulo ou ISBN
                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                encontrado = False

                for livro in livros:
                    if livro["Titulo"] == titleremove:
                        livros.remove(livro)
                        encontrado = True
                        break

                if encontrado == True:
                    with open("livros.json", "w", encoding="utf-8") as arquivo:
                        json.dump(livros, arquivo, indent=4, ensure_ascii=False)

                    print("\nLivro removido com sucesso!\n===============================")
                else:
                    print("\nEste título não está na biblioteca.\n===============================")
            case 2:
                isbnremove = input("Insira o ISBN do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)
                
                encontrado = False
                
                for livro in livros:
                    if livro["ISBN"] == isbnremove:
                        livros.remove(livro)
                        encontrado = True
                        break

                if encontrado == True:
                    with open("livros.json", "w", encoding="utf-8") as arquivo:
                        json.dump(livros, arquivo, indent=4, ensure_ascii=False)
                
                    print("\nLivro removido com sucesso!\n===============================")
                else:
                    print("\nEste título não está na biblioteca.\n===============================")

            case _:
                print("\nOpção inválida.")

    case 7:
        print("===============================\n~ ESTATÍSTICAS ~ \n===============================")
        print("\n1- Livros cadastrados\n2- Livros disponíveis\n3- Livros alugados\n")

        opcaoestatistica = int(input("Escolha uma opção: "))

        match opcaoestatistica:
            case 1:
                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                print("zn===============================\n~ LIVROS TOTAIS CADASTRADOS ~ \n===============================")

                print("Livros totais: ", len(livros))
        

            case 2:
                
                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                    print("\n===============================\n~ LIVROS DISPONÍVEIS ~ \n===============================")

                    disponivel = 0

                    for livro in livros:
                        if livro['Status'] == "Disponível":
                            print("- " + livro['Titulo'])
                            disponivel += 1

                    print("\nLIVROS DISPONÍVEIS: ", disponivel)
                    print("===============================")
            case 3: 

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                    print("\n===============================\n~ LIVROS ALUGADOS ~ \n===============================")

                    alugado = 0

                    for livro in livros:
                        if livro['Status'] == "Alugado":
                            print("- " + livro['Titulo'])
                            alugado += 1
                    print("\nLIVROS ALUGADOS: ", alugado)
                    print("===============================")
            case _:
                print("\nOpção inválida.")
    case _:
        print("\nOpção inválida.")