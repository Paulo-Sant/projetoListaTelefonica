

def salvar_contatos(lista):
    arquivo = open("contatos.txt", "w")

    for contato in lista:
        arquivo.write(f'{contato["nome"], contato["email"], contato["telefone"]}')

    arquivo.close()


def carregar_contato():
    lista = []

    try:
        arquivo = open('contatos.txt', 'r')

        for linha in arquivo.readlines():
            coluna = linha.strip().split('#')
            contato = {"email": coluna[1], "nome": coluna[0], "tel": coluna[2]}

            lista.append(contato)

        arquivo.close()
    except FileNotFoundError:
        pass
    return lista


def existe_contato(lista, email):
    if len(lista) > 0:
        for contato in lista:
            if contato['email'] == email:
                return True
    return False


def adicionar(lista):
    while True:
        email = input('Digite o e-mail do Contato: ')

        if not existe_contato(lista, email):
            break
        else:
            print('Este e-mail já está em uso.')
            print('Por favor utilize um e-mail diferente.')
    # Deste modo o identificador do contato inserido será unico

    contato = {'email': email, 'nome': input('Digite o nome: '), 'telefone': input('Digite o Telefone: ')}
    lista.append(contato)

    print(f"O contato {contato['nome']}, foi cadastrado com Sucesso! ")


def excluir(lista):
    print('=====EXCLUIR CONTATO=====')
    if len(lista) > 0:
        email = input('Digite o email do contato a ser excluído: ')
        if existe_contato(lista, email):
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print(f"Nome:{contato['nome']}")
                    print(f"Email:{contato['email']}")
                    print(f"Telefone:{contato['telefone']}")
                    print('========================\n')

                    del lista[i]

                    print('O contato foi exluído com sucesso!!')
                    break
        else:
            print('Não foram encontrados resultados com o email informado\n')
    else:
        print('Não Existe nenhum contato cadastrado no sistema. \n')


def editar(lista):
    print('=====ALTERAR CONTATO=====')
    if len(lista) > 0:
        email = input('Digite o email do contato a ser alterado: ')
        if existe_contato(lista, email):
            for contato in lista:
                if contato['email'] == email:
                    print(f"Nome:{contato['nome']}")
                    print(f"Email:{contato['email']}")
                    print(f"Telefone:{contato['telefone']}")
                    print('========================\n')

                    contato['nome'] = input('Digite um novo nome: ')
                    contato['telefone'] = input('Digite um novo número: ')

                    print(f'Dados do contato {contato["email"]} alterados com sucesso!')
                    break
        else:
            print('Não foram encontrados resultados com o email informado\n')
    else:
        print('Não Existe nenhum contato cadastrado no sistema. \n')


def listar(lista):
    print('=====LISTAR CONTATOS=====')
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            print(f'Contato {i+1}')
            print(f"\tNome:{contato['nome']}")
            print(f"\tEmail:{contato['email']}")
            print(f"\tTelefone:{contato['telefone']}")
            print('=================================')
        print(f"Total de Contatos {len(lista)} \n")

    else:
        print('Não Existe nenhum contato cadastrado no sistema. \n')


def buscar(lista):
    print('=====BUSCAR CONTATO=====')
    if len(lista) > 0:
        email = input('Digite o email do contato: ')
        if existe_contato(lista, email):
            for contato in lista:
                if contato['email'] == email:
                    print(f"Nome:{contato['nome']}")
                    print(f"Email:{contato['email']}")
                    print(f"Telefone:{contato['telefone']}")
                    print('========================\n')
                    break
        else:
            print('Não foram encontrados resultados com o email informado\n')
    else:
        print('Não Existe nenhum contato cadastrado no sistema. \n')


def principal():

    lista = carregar_contato()

    while True:
        print('=================')
        print('AGENDA TELEFÔNICA')
        print('=================')
        print('1 - Adicionar')
        print('2 - Excluir')
        print('3 - Editar')
        print('4 - Listar')
        print('5 - Buscar')
        print('6 - Sair')
        opcao = int(input('>>> '))

        if opcao == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opcao == 2:
            excluir(lista)
            salvar_contatos(lista)
        elif opcao == 3:
            editar(lista)
            salvar_contatos(lista)
        elif opcao == 4:
            listar(lista)
        elif opcao == 5:
            buscar(lista)
        elif opcao == 6:
            print('Saindo do Programa...')
            break
        else:
            print('Opção inválida, por favor insira uma opção de 1 a 6!')


principal()
