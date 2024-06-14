agenda = []

def criar_contato(agenda, nome, telefone):
    contato = {'nome': nome, 'telefone': telefone}
    agenda.append(contato)
    print('Seu contato foi criado com sucesso!')

def excluir_contato(agenda, nome_contato):
    for contato in agenda:
        if contato['nome'] == nome_contato:
            agenda.remove(contato)
            print(f'O contato {nome_contato} foi removido com sucesso.')
            return
    print(f'O contato {nome_contato} não foi encontrado na agenda.')


def listar_contatos():
    if not agenda:
        print('A agenda está vazia.')
    else:
        for contato in agenda:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def alterar_contato(agenda, nome_contato):
    for contato in agenda:
        if contato['nome'] == nome_contato:
            print(f'Contato encontrado: {contato["nome"]}, Telefone: {contato["telefone"]}')
            opcao_alteracao = input("O que você deseja alterar? (nome/telefone): ")
            if opcao_alteracao == 'nome':
                novo_nome = input('Digite o novo nome: ')
                contato['nome'] = novo_nome
                print('Nome do contato atualizado com sucesso!')
            elif opcao_alteracao == 'telefone':
                novo_telefone = input('Digite o novo número de telefone: ')
                contato['telefone'] = novo_telefone
                print('Telefone do contato atualizado com sucesso!')
            else:
                print('Opção inválida.')
            return
    print(f'O contato {nome_contato} não foi encontrado na agenda.')


def principal():
    while True:
        print('====== AGENDA TELEFÔNICA ======')
        print(' 1 - Criar Contato')
        print(' 2 - Excluir Contato')
        print(' 3 - Listar Contatos')
        print(' 4 - Alterar Contato')
        print(' 5 - Sair da Agenda')
        opcao = input('Qual será a opção escolhida? ')

        if opcao == '1':
            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o número do seu contato: ')
            criar_contato(agenda, nome, telefone)

        elif opcao == '2':
            nome_contato = input('Digite o nome do contato a ser removido: ')
            excluir_contato(agenda, nome_contato)

        elif opcao == '3':
            listar_contatos()
        
        elif opcao == '4':
            nome_contato = input('Digite o nome do contato a ser alterado: ')
            alterar_contato(agenda, nome_contato)
        
        elif opcao == '5':
            print('Saindo da sua agenda')
            break
principal()