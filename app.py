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

def finalizar_app():
    os.system('clear')
    print('Finalizando programa\n')

def opcao_invalida():
    print('Escolha uma opção válida!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastro_rest():
    os.system('clear')
    print('Cadastro de restaurantes\n')
    nome_rest = input('Insira o nome do restaurante a ser cadastrado:')
    print('Nome registrado!')
    categoria = input('Insira a categoria do restaurante:')
    dados_rest = {'nome':nome_rest, 'categoria':categoria, "ativo":False}
    rest.append(dados_rest)
    print('Restaurante registrado!')
    retorno_cad()
    
def retorno_cad():
    retorno = input('Deseja cadastrar um novo restaurante? [Sim/Nao]')

    if retorno == 'Sim':
        cadastro_rest()
    elif retorno == 'Nao':
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
    os.system('clear')
    print('Lista de restaurantes cadastrados')
    
    for restaurante in rest:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_restaurante} | {categoria} | {ativo}')
    
    input('\nDigite uma tecla para continuar: ')
    main()

def escolha_user():
    try:
        escolha_user =  int(input('Escolha uma opção: '))
        if escolha_user == 1:
            cadastro_rest()
        elif escolha_user == 2:
            listar_rest()
        elif escolha_user == 3:
            print('Ativar Restaurante')
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