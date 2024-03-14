from modelos.restaurante  import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de Uva', 5.0, 'pequeno')
prato = Prato('Pao na chapa', 10.0, 'Pao na chapa na hora!!!')
restaurante.adicionar_no_cardapio(bebida_suco)
restaurante.adicionar_no_cardapio(prato)

def main():
    restaurante.exibir_cardapio

if __name__ == '__main__':
    main() 