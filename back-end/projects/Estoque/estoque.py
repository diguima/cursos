import os
import sqlite3
import lib.validations
import lib.string_functions
import time

def pause_screen():

    print('')

    response = input('Pressione qualquert tecla para continuar...\n')

# Imprime um título na tela

def print_title(title, size):

    print('')

    print(size * '=')
    print(lib.string_functions.fill_string(title, ' ', size))
    print(size * '=')


def list_records(list):

    item0 = item1 = item2 = item3 = ''   

    item0 = lib.string_functions.fill_string('Id', ' ', 10, 'left')
    item1 = lib.string_functions.fill_string('Nome', ' ', 30, 'right')
    item2 = lib.string_functions.fill_string('Quantidade', ' ', 15, 'left')
    item3 = lib.string_functions.fill_string('Preço', ' ', 10, 'left')
    
    print(100 * "=")
    print(item0, item1, item2, item3)
    print(100 * "=")

    for item in list:

        item0 = lib.string_functions.fill_string(str(item[0]), ' ', 10, 'left')
        item1 = lib.string_functions.fill_string(item[1], ' ', 30, 'right')
        item2 = lib.string_functions.fill_string(str(item[2]), ' ', 15, 'left')
        item3 = lib.string_functions.fill_string('R$ {:,.2f}'.format(item[3]), ' ', 10, 'left')

        print(item0, item1, item2, item3)

# Mostra opções

def show_options(optionsLables, inputMessage):    

    choiceStr = chosenNumber = 0

    validNumber = False

    while not validNumber:

        os.system("cls")

        systemTitle = lib.string_functions.fill_string(' CONTROLE DE ESTOQUE ', '*', 100)
        
        print(systemTitle + '\n')

        print("Menu:\n")

        optionsMaxNumber = 0

        for option in optionsLables:

            optionsMaxNumber += 1

            print(option)

        print('')
        
        choiceStr = input(inputMessage)

        validNumber = lib.validations.is_number(choiceStr)

        if validNumber:

            chosenNumber = int(choiceStr.strip())

            if chosenNumber == 0 or chosenNumber > optionsMaxNumber:

                validNumber = False

        if not validNumber:
    
            print('')
            print('Informe uma opção válida.')
            
            pause_screen()

    return chosenNumber

# Entrada de um Id

def id_entry():

    idNumber = 0

    while idNumber <= 0:

        id = input("Informe um Id: ")

        if not lib.validations.is_number(id):

            print("Informe um id válido.")

            time.sleep(2)

        else:

            idNumber = int(id.strip())

    return idNumber

# Entrada de algum valor para pesquisa

def search_input():

    searchContent = ''

    while searchContent.strip() == '':

        searchContent = input("Informe um Id, um nome ou parte do nome: ")

    return searchContent

# Entrada de dados

def data_entry(optionNumber, fieldsLabels, fieldsTypes, cursor):

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

        if lib.validations.is_number(searchContent):

            SQLStatement += 'id = ' + searchContent.strip()

        else:

            SQLStatement += 'nome LIKE "%' + searchContent.strip() + '%"'

        if cursor.execute(SQLStatement):

            recordsList = cursor.fetchall()

            recordsNumber = len(recordsList)

            if recordsNumber == 0:

                print('Nenhum produto encontrado.')
                
                executeInput = False

                pause_screen()

            else:

                if recordsNumber > 1:

                    print('Quantidade de produtos encontrados: ' + str(recordsNumber) + '\n')
                    print(recordsList)
                    print('')

                    id = id_entry()
        else:
        
            print("Não foi pesquisar na tabela de produto.")

            pause_screen()


    fieldsContent = []

    if executeInput:
        
        index = 0

        for field in fieldsLabels:            
            
            fieldsContent.append(input(field + ': '))

        if optionNumber == 2:

            fieldsContent.append(id)
        
    return fieldsContent
    
# Opção de inclusão de produto

def insertOption(cursor, fieldsLabels, fieldsTypes, fieldsContent):

    fieldsContent = data_entry(1, fieldsLabels, fieldsTypes, cursor)

    if len(fieldsContent) >= 3:
    
        fieldsValues = delimiter = ''

        for field in fieldsLabels:

            fieldIndex = fieldsLabels.index(field)

            fieldsValues += delimiter + lib.string_functions.quoted(fieldsContent[fieldIndex])
            
            delimiter = ', '        
        
        SQLStatement = f'INSERT INTO produtos (nome, quantidade, preco) VALUES ({fieldsValues})'

        if cursor.execute(SQLStatement):        

            print('Produto cadastrado.')

        else:

            print('Erro ao tentar cadastrar produto.')

        pause_screen()

# Opção de alteração de produto

def updateOption(cursor, fieldsLabels, fieldsNames, fieldsTypes, fieldsContent):

    fieldsContent = data_entry(2, fieldsLabels, fieldsTypes, cursor)

    if len(fieldsContent) >= 3:
    
        fieldsValues = delimiter = where = ''

        for field in fieldsLabels:

            fieldIndex = fieldsLabels.index(field)

            fieldType = fieldsTypes[fieldIndex]

            if fieldType == 'TEXT':

                fieldsValues += delimiter + fieldsNames[fieldIndex] + '=' + lib.string_functions.quoted(fieldsContent[fieldIndex])

            else:

                fieldsValues += delimiter + fieldsNames[fieldIndex] + '=' + str(fieldsContent[fieldIndex])
            
            delimiter = ', '

        where = ' WHERE id = ' + str(fieldsContent.pop())
        
        SQLStatement = f'UPDATE produtos SET {fieldsValues} {where}'

        if cursor.execute(SQLStatement):        

            print('Produto alterado.')

        else:

            print('Erro ao tentar alterar produto.')

        pause_screen()

# Opção de pesquisa e exibição de produto

def selectOption(option, cursor, title, pause=True):

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

            if lib.validations.is_number(searchContent):

                SQLStatement += 'id = ' + searchContent.strip()

            else:

                SQLStatement += 'nome LIKE "%' + searchContent.strip() + '%"'            

    if cursor.execute(SQLStatement):

        recordsList = cursor.fetchall()

        recordsNumber = len(recordsList)

        if len(recordsList) <= 0:

            print('Nenhum produto encontrado.')

            pause_screen() 

        else:

            list_records(recordsList)

    else:

        print("Erro ao tentar listar os produtos.")

    if pause:

        pause_screen()


def deleteOption(cursor):

    id = id_entry()

    SQLStatement = 'SELECT id, nome, quantidade, preco FROM produtos WHERE id = ' + str(id)

    if cursor.execute(SQLStatement):

        recordsList = cursor.fetchall()

        recordsNumber = len(recordsList)

        if len(recordsList) <= 0:

            print('Não existe produto com o Id informado.')
    
            pause_screen()

        else:

            SQLStatement = 'DELETE FROM produtos WHERE id = ' + str(id)

            if cursor.execute(SQLStatement):

                print('Produto excluído.')

            else:

                print('Não foi possívelm excluir o produto.')

            pause_screen()


def main():

    conn = sqlite3.connect('estoque.db')

    cursor = conn.cursor()

    SQLStatement = '''CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
        )
    '''

    if cursor.execute(SQLStatement):

        print('Banco criado.')

    else:

        print('Erro ao tentar criar banco estoque.db.')

    conn.commit()

    menuOptions = ('1 - Adicionar produto', '2 - Atualizar produto', '3 - Remover produto', '4 - Listar produtos', '5 - Buscar produto', '6 - Total em estoque', '7 - Sair')

    inputMessage = 'Escolha uma das opções acima: '

    fieldsLabels = ['Nome', 'Quantidade', 'Preço']
    fieldsNames = ['nome', 'quantidade', 'preco' ]
    fieldsTypes = ['TEXT', 'INTEGER', 'REAL']
    fieldsContent = []

    while True:

        chosenNumber = show_options(menuOptions, inputMessage)

        match(chosenNumber):
            case 1:

                insertOption(cursor, fieldsLabels, fieldsTypes, fieldsContent)

            case 2:

                updateOption(cursor, fieldsLabels, fieldsNames, fieldsTypes, fieldsContent)

            case 3:

                deleteOption(cursor)

            case 4:

                selectOption(1, cursor, 'LISTA DE PRODUTOS CADASTRADOS')

            case 5:

                selectOption(2, cursor, "BUSCA DE PRODUTO")

            case 6:

                selectOption(1, cursor, 'PRODUTOS EM ESTOQUE', False)

                print('')
                
                if cursor.execute(SQLStatement):

                    SQLStatement = '''
                        SELECT SUM(quantidade)
                        FROM produtos      
                    '''

                    if cursor.execute(SQLStatement):

                        recordsList = cursor.fetchall()

                        quantidadeTotal = recordsList[0]

                    print('QUANTIDADE TOTAL:', quantidadeTotal[0])

                    SQLStatement = '''
                        SELECT SUM(quantidade * preco)
                        FROM produtos      
                    '''

                    if cursor.execute(SQLStatement):

                        recordsList = cursor.fetchall()

                        valorTotal = recordsList[0]

                    print('VALOR TOTAL:', 'R$ {:,.2f}'.format(valorTotal[0]))

                    pause_screen()

            case 7:

                break

    conn.commit()

    conn.close()

    os.system("cls")

if __name__ == '__main__':

    main()
