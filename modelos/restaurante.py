class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):  
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'


restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_pizza = Restaurante('pizza', 'Italiano')


Restaurante.listar_restaurantes()