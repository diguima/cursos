class Produto:

    def __init__(self):

        self.__nome = ''
        self.__quantidade = 0
        self.__preco = 0

    def set_product(self, nome, quantidade, preco):

        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco

    def get_id(self):

        return self.__id

    def get_nome(self):

        return self.__nome

    def get_quantidade(self):

        return self.__quantidade

    def get_preco(self):

        return self.__preco
    
    def get_collumns(self):
        
        collumns = {
            'nome': self.nome, 
            'quantidade': self.quantidade, 
            'preco': self.preco
        }

        return collumns

    def __str__(self):
        
        collumns = '{' + f"'id': {self.id}, 'nome': {self.nome}, 'quantidade': {self.quantidade}, 'preco': {self.preco}" + '}'
                
        return collumns
        