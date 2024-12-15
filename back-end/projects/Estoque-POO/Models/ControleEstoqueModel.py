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

        produto = {
            'table': 'produto',
            'collumns': {
                'nome': nome, 
                'quantidade': quantidade,
                'preco': preco
            }
        }

        return self.insert_values(produto['table'], produto['collumns'])

    def alterar_produto(self, id, nome, quantidade, preco):

        produto = {
            'table': 'produto',
            'collumns': {
                'nome': nome, 
                'quantidade': quantidade,
                'preco': preco 
            },            
            'condition': {
                'where': f'id = {id}'
            }
        }

        return self.update_values(produto['table'], produto['collumns'], produto['condition'])

    def excluir_produto(self, id):
        
        condition = {
            'where': f'id = {id}'
        }

        return self.delete_values('produto', condition)

    def listar_produtos(self):

        return self.get_all('produto')

    def buscar_produto(self, condition):

        return self.get_conditional_list('produto', condition)
    
    def busca_produto_id(self, id):

        return self.get_value_id('produto', id)

    def total_produtos(self, sum):

        return self.get_sum('produto', sum)
