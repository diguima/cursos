from Models.DBModel import DB

class ControleEstoque(DB):
    
    def __init__(self, bd):

        super().__init__(bd)

        self.__table = {
            'table': 'produto',
            'collumns': {
                'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                'nome': 'TEXT NOT NULL',
                'quantidade': 'INTEGER NOT NULL',
                'preco': 'REAL NOT NULL'
            }
        }      

        self.create_table(self.__table['table'], self.__table['collumns'])

    def adicionar_produto(self, nome, quantidade, preco):

        newProduct = {
            'table': 'produto',
            'collumns': {
                'nome': nome, 
                'quantidade': quantidade,
                'preco': preco
            }
        }

        return self.insert_values(newProduct['table'], newProduct['collumns'])

    def alterar_produto(self):

        pass

    def excluir_produto(self):

        pass

    def listar_produtos(self):

        pass

    def buscar_produto(self):

        pass
