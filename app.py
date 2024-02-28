import os
import time

rest = []

def menu():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def finalizar_app():
    os.system('clear')
    print('Finalizando programa\n')

def opcao_invalida():
    print('Escolha uma opção válida!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastro_rest():
    subtitulo('Cadastrar restaurantes')
    nome_rest = input('Insira o nome do restaurante a ser cadastrado:')
    print('Nome registrado!')
    categoria = input('Insira a categoria do restaurante:')
    dados_rest = {'nome':nome_rest, 'categoria':categoria, "ativo":False}
    rest.append(dados_rest)
    print('Restaurante registrado!')
    retorno_cad()
    
def retorno_cad():
    retorno_c = input('Deseja cadastrar um novo restaurante? [Sim/Nao]')
    upper_retorno_c = retorno_c.upper()

    if upper_retorno_c == 'SIM':
        cadastro_rest()
    elif upper_retorno_c == 'NAO':
        time.sleep(1)
        os.system('clear')
        print('Voltando ao menu')
        menu()
        exibir_opcoes()
        escolha_user()
    else:
        print('Insira uma opção válida')
        retorno_cad()

def listar_rest():
    subtitulo('Lista de restaurantes cadastrados')
    
    for restaurante in rest:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante} | {categoria} | {ativo} ')
    
    input('\nDigite uma tecla para continuar: ')
    main()

def alternar_estado_restaurante():
    subtitulo('Ativacao de restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in rest:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            retorno_ativacao()

    if not restaurante_encontrado:
        print('Digite um restaurante válido!')
        time.sleep(1)
        alternar_estado_restaurante()
    
    main()

def retorno_ativacao():
    retorno_l = input('Deseja ativar um novo restaurante? [Sim/Nao]')
    upper_retorno_l = retorno_l.upper()

    if upper_retorno_l == 'SIM':
        alternar_estado_restaurante()
    elif upper_retorno_l == 'NAO':
        time.sleep(1)
        os.system('clear')
        print('Voltando ao menu')
        menu()
        exibir_opcoes()
        escolha_user()
    else:
        print('Insira uma opção válida')
        retorno_ativacao()

def escolha_user():
    try:
        escolha_user =  int(input('Escolha uma opção: '))
        if escolha_user == 1:
            cadastro_rest()
        elif escolha_user == 2:
            listar_rest()
        elif escolha_user == 3:
            alternar_estado_restaurante()
        elif escolha_user == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    os.system('clear')
    menu()
    exibir_opcoes()
    escolha_user()

if __name__ == '__main__':
    main()





