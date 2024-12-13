from Models.ControleEstoqueModel import ControleEstoque
from Models.ProdutoModel import Produto
import lib.screen as screen
import lib.string_functions as strings
import lib.validations as validations
import time

estoque = ControleEstoque('Banco/estoque.db')


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


def data_entry(optionNumber, fieldsLabels, fieldsTypes):

    executeInput = True

    title = ''

    id = 0

    if optionNumber == 1:

        title = 'CADASTRO DE PRODUTO'

    elif optionNumber == 2:

        title = 'ALTERAÇÃO DE PRODUTO'

    print_title(title, 100)

    if optionNumber == 2:

        recordsNumber = 0

        searchContent = search_input()

        SQLStatement = 'SELECT id, nome, quantidade, preco FROM produtos WHERE '

        if validations.is_number(searchContent):

            SQLStatement += 'id = ' + searchContent.strip()

        else:

            SQLStatement += 'nome LIKE "%' + searchContent.strip() + '%"'

            screen.pause_screen()

    fieldsContent = []

    if executeInput:

        index = 0

        for field in fieldsLabels:

            fieldsContent.append(input(field + ': '))

        if optionNumber == 2:

            fieldsContent.append(id)

    return fieldsContent


def insertOption(fieldsLabels, fieldsTypes, fieldsContent):

    fieldsContent = data_entry(1, fieldsLabels, fieldsTypes)

    if len(fieldsContent) >= 3:

        fieldsValues = delimiter = ''

        for field in fieldsLabels:

            fieldIndex = fieldsLabels.index(field)

            fieldsValues += delimiter + \
                strings.quoted(fieldsContent[fieldIndex])

            delimiter = ', '

# Altera produto


def updateOption(fieldsLabels, fieldsNames, fieldsTypes, fieldsContent):

    fieldsContent = data_entry(2, fieldsLabels, fieldsTypes)

    if len(fieldsContent) >= 3:

        fieldsValues = delimiter = where = ''

        for field in fieldsLabels:

            fieldIndex = fieldsLabels.index(field)

            fieldType = fieldsTypes[fieldIndex]

            if fieldType == 'TEXT':

                fieldsValues += delimiter + \
                    fieldsNames[fieldIndex] + '=' + \
                    strings.quoted(fieldsContent[fieldIndex])

            else:

                fieldsValues += delimiter + \
                    fieldsNames[fieldIndex] + '=' + \
                    str(fieldsContent[fieldIndex])

            delimiter = ', '

        # where = ' WHERE id = ' + str(fieldsContent.pop())

        # SQLStatement = f'UPDATE produtos SET {fieldsValues} {where}'

        # if cursor.execute(SQLStatement):

        #     print('Produto alterado.')

        # else:

        #     print('Erro ao tentar alterar produto.')

        screen.pause_screen()

# Pesquisa e exibe produto


def selectOption(option, title, pause=True):

    SQLStatement = ''

    match(option):

        case 1:

            print_title(title, 100)

            if SQLStatement.strip() == '':

                SQLStatement = '''
                    SELECT id, nome, quantidade, preco
                    FROM produtos                
                '''

        case 2:

            print_title('BUSCA DE PRODUTOS', 100)

            recordsNumber = 0

            searchContent = search_input()

            SQLStatement = 'SELECT id, nome, quantidade, preco FROM produtos WHERE '

            if validations.is_number(searchContent):

                SQLStatement += 'id = ' + searchContent.strip()

            else:

                SQLStatement += 'nome LIKE "%' + searchContent.strip() + '%"'

    # if cursor.execute(SQLStatement):

    #     recordsList = cursor.fetchall()

    #     recordsNumber = len(recordsList)

    #     if len(recordsList) <= 0:

    #         print('Nenhum produto encontrado.')

    #         lib.screen.pause_screen()

    #     else:

    #         list_records(recordsList)

    # else:

    #     print("Erro ao tentar listar os produtos.")

    if pause:

        screen.pause_screen()

# Exclui produto


def deleteOption():

    id = id_entry()
