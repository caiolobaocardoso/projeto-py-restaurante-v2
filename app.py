from modelos.restaurante  import Restaurante

nome_rest = input('Insira o nome do restaurante')
categoria_rest = input('Insira a categoria do restaurante')
Restaurante(nome_rest, categoria_rest)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()