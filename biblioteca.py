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
            
        print("Livro cadastrado com sucesso!\n===============================")

    case 2:
            with open("livros.json","r",encoding="utf-8") as arquivo:   
                livros = json.load(arquivo)

            print("===============================\nOs livros cadastrados são:\n")
            for livro in livros:
                print('- ' + livro['Titulo'] + ' - (' + livro['Autor'] + ').')   

    case 3:
        print("===============================\n1- Titulo\n2- ISBN")   # adiciona a opção de procura para o
        opcaoprocura = int(input("Como deseja procurar seu livro? "))

        match opcaoprocura:
            case 1:     
                titlesearch = input("Insira o titulo do livro: ")

                with open("livros.json", "r", encoding="utf-8") as arquivo:
                    livros = json.load(arquivo)

                encontrado = False 

                for livro in livros:
                    if livro["Titulo"] == titlesearch:                
                        print("===============================\n")        
                        print("Nome: " + livro['Titulo'] + "\n"  + "Autor:" + livro['Autor'])
                        print("Gênero: " + livro['Gênero'] + "\n" + "Número de páginas: " + str(livro['Numero de páginas']))
                        print("ISBN: " + livro['ISBN'])
                        print("Status: " + livro['Status']) 
                        encontrado = True
                        break
                
                if encontrado == True:
                    with open("livros.json", "w", encoding="utf-8") as arquivo:
                        json.dump(livros, arquivo, indent=4, ensure_ascii=False)
                
                    print("\nLivro achado com sucesso!")
                else:
                    print("\nEste título não está na biblioteca.")
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
                
                    print("\nLivro achado com sucesso!")
                else:
                    print("\nEste título não está na biblioteca.")      
    case 4:
        print("===============================\n1- Titulo\n2- ISBN")
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

                                print("Livro alugado com sucesso!")
                        else:
                            print("Este livro já está alugado.")

                        break

                if encontrado == False:
                    print("Este livro não foi encontrado.")
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

                                print("Livro alugado com sucesso!")
                        else:
                            print("Este livro já está alugado.")

                        break

                if encontrado == False:
                    print("Este livro não foi encontrado.")
                    
    case 6:
        print("===============================\n1- Titulo\n2- ISBN")   # adiciona a opção de procura para o
        opcaoremocao = int(input("Como deseja procurar seu livro para remove-lo? "))    # usuário

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

                    print("Livro removido com sucesso!")
                else:
                    print("Este título não está na biblioteca.")
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
                
                    print("\nLivro removido com sucesso!")
                else:
                    print("\nEste título não está na biblioteca.")
                
                   



                    
