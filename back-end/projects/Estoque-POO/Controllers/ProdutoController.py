from Models.ControleEstoqueModel import ControleEstoque
from Models.ProdutoModel import Produto
import lib.screen as screen
import lib.string_functions as strings
import lib.validations as validations
import time

estoque = ControleEstoque('Banco/estoque.db')

fieldsLabels = ['Nome', 'Quantidade', 'Preço']
fieldsNames = ['nome', 'quantidade', 'preco']
fieldsTypes = ['TEXT', 'INTEGER', 'REAL']

def list_records(list, pause=True):

    item0 = item1 = item2 = item3 = ''

    item0 = strings.fill_string('Id', ' ', 10, 'left')
    item1 = strings.fill_string('Nome', ' ', 30, 'right')
    item2 = strings.fill_string('Quantidade', ' ', 15, 'left')
    item3 = strings.fill_string('Preço', ' ', 10, 'left')

    print(100 * "=")
    print(item0, item1, item2, item3)
    print(100 * "=")

    for item in list:

        item0 = strings.fill_string(str(item[0]), ' ', 10, 'left')
        item1 = strings.fill_string(item[1], ' ', 30, 'right')
        item2 = strings.fill_string(str(item[2]), ' ', 15, 'left')
        item3 = strings.fill_string('R$ {:,.2f}'.format(item[3]), ' ', 10, 'left')

        print(item0, item1, item2, item3)

    if pause:

        screen.pause_screen()


def print_title(title, size):

    print('')

    print(size * '=')
    print(strings.fill_string(title, ' ', size))
    print(size * '=')

# Entrada de algum valor para pesquisa


def search_input():

    searchContent = ''

    while searchContent.strip() == '':

        searchContent = input("Informe um Id, um nome ou parte do nome: ")

    return searchContent


# Entrada de um Id


def id_entry():

    idNumber = 0

    while idNumber <= 0:

        id = input("Informe um Id: ")

        if not validations.is_number(id):

            print("Informe um id válido.")

            time.sleep(2)

        else:

            idNumber = int(id.strip())

    return idNumber


# Entrada de dados


def data_entry(optionNumber):

    executeInput = True

    title = ''

    id = 0
    
    fieldsContent = []

    if optionNumber == 1:

        title = 'CADASTRO DE PRODUTO'

    elif optionNumber == 2:

        title = 'ALTERAÇÃO DE PRODUTO'

    print_title(title, 100)

    if optionNumber == 2:

        recordsNumber = 0

        searchContent = search_input()
        
        if validations.is_number(searchContent):

            id = searchContent
                
            recordsList = estoque.busca_produto_id(id)

            if len(recordsList) <= 0:

                print('Id invalido.')

                time.sleep(2)                    

                executeInput = False

        else:
           
            condition = {
                'where': f'nome LIKE "%{searchContent}%"'
            }                
             
            recordsList = estoque.get_conditional_list('produto', condition)

            recordsNumber = len(recordsList)

            if recordsNumber == 0:

                print('Nenhum produto encontrado.')
                
                executeInput = False

                screen.pause_screen()

            else:

                list_records(recordsList, False)

                print('')

                id = id_entry()

                recordsList = estoque.busca_produto_id(id)

                if len(recordsList) <= 0:

                    print('Id invalido.')

                    time.sleep(2)                    

                    executeInput = False

    if executeInput:

        for field in fieldsLabels:

            fieldsType = fieldsTypes[fieldsLabels.index(field)]

            content = input(field + ': ')

            if fieldsType == 'REAL':

                content = content.replace(',', '.')

            fieldsContent.append(content)

        if optionNumber == 2:

            fieldsContent.append(id)

    return fieldsContent


def insertOption():

    fieldsContent = data_entry(1)

    if len(fieldsContent) >= 3:

        novoProduto = Produto()

        nome = fieldsContent[0]
        quantidade = fieldsContent[1]
        preco = fieldsContent[2]

        novoProduto.set_produto(nome, quantidade, preco)

    if estoque.adicionar_produto(novoProduto.get_nome(), novoProduto.get_quantidade(), novoProduto.get_preco()):

        print('Produto adicionado.')

    else:

        print('Erro ao adicionar produto.')

    screen.pause_screen()

# Altera produto

def updateOption():

    fieldsContent = data_entry(2)

    if len(fieldsContent) >= 3:

        alteraProduto = Produto()

        nome = fieldsContent[0]
        quantidade = fieldsContent[1]
        preco = fieldsContent[2]
        id = str(fieldsContent.pop())

        alteraProduto.set_produto(nome, quantidade, preco)

        if estoque.alterar_produto(id, alteraProduto.get_nome(), alteraProduto.get_quantidade(), alteraProduto.get_preco()):

            print('Produto alterado.')

        else:

            print('Erro ao tentar alterar produto.')

        screen.pause_screen()

# Pesquisa e exibe produto

def selectOption(option, title, pause=True):

    match(option):

        case 1:

            print_title(title, 100)

            recordsList = estoque.listar_produtos()

            recordsNumber = len(recordsList)

            if recordsNumber <= 0:

                print('Nenhum produto encontrado.')

                screen.pause_screen()

            else:

                list_records(recordsList)

        case 2:

            print_title('BUSCA DE PRODUTOS', 100)

            searchContent = search_input()

            if validations.is_number(searchContent):

                condition = {
                    'where': f'id = {searchContent}'
                }                

            else:

                searchContent = searchContent.strip()

                condition = {
                    'where': f'nome LIKE "%{searchContent}%"'
                }
                
            recordsList = estoque.buscar_produto(condition)

            recordsNumber = len(recordsList)

            if recordsNumber <= 0:

                print('Nenhum produto encontrado.')

                screen.pause_screen()

            else:

                list_records(recordsList)            

        case 3:

            print_title(title, 100)

            recordsList = estoque.listar_produtos()

            recordsNumber = len(recordsList)

            if recordsNumber <= 0:

                print('Nenhum produto encontrado.')

                screen.pause_screen()

            else:

                list_records(recordsList, False)

                print('')

                quantidadeTotal = estoque.total_produtos('quantidade')

                print('QUANTIDADE TOTAL:', quantidadeTotal)

                valorTotal = estoque.total_produtos('quantidade * preco')

                print('VALOR TOTAL:', 'R$ {:,.2f}'.format(valorTotal))

                screen.pause_screen()

# Exclui produto


def deleteOption():

    searchContent = search_input()

    deletaProduto = True
    
    if validations.is_number(searchContent):

        id = searchContent

        recordsList = estoque.busca_produto_id(id)

        if len(recordsList) <= 0:

            print('Id invalido.')

            time.sleep(2)                    

            deletaProduto = False        

    else:
        
        condition = {
            'where': f'nome LIKE "%{searchContent}%"'
        }                
            
        recordsList = estoque.get_conditional_list('produto', condition)

        recordsNumber = len(recordsList)

        if recordsNumber == 0:

            print('Nenhum produto encontrado.')
            
            deletaProduto = False

            screen.pause_screen()

        else:

            list_records(recordsList, False)

            print('')

            id = id_entry()

            recordsList = estoque.busca_produto_id(id)

            if len(recordsList) <= 0:

                print('Id invalido.')

                time.sleep(2)                    

                deletaProduto = False


    if deletaProduto:

        estoque.excluir_produto(id)

        print('Produto excluido.')

    else:

        print('Erro ao tentar excluir produto.')

    screen.pause_screen()