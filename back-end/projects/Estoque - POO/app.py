from Models.DBModel import DB
from Models.ProdutoModel import Produto
import Controllers.ProdutoController as ProdutoController
import lib.validations
import lib.string_functions
import lib.screen as screen
import os
import sqlite3
import time


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
        item3 = lib.string_functions.fill_string(
            'R$ {:,.2f}'.format(item[3]), ' ', 10, 'left')

        print(item0, item1, item2, item3)

# Mostra opções


def show_options(optionsLables, inputMessage):

    choiceStr = chosenNumber = 0

    validNumber = False

    while not validNumber:

        os.system("cls")

        # systemTitle = lib.string_functions.fill_string(
        #     ' CONTROLE DE ESTOQUE ', '*', 100)

        # print(systemTitle + '\n')

        print('''\033[32m
        ####################################################################################
        #           ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗   ██╗███████╗           #
        #           ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║   ██║██╔════╝           #
        #           █████╗  ███████╗   ██║   ██║   ██║██║   ██║██║   ██║█████╗             #
        #           ██╔══╝  ╚════██║   ██║   ██║   ██║██║▄▄ ██║██║   ██║██╔══╝             #
        #           ███████╗███████║   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝███████╗           #
        #           ╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝           #
        #################################################################################### 
        \033[0m''')

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

            if chosenNumber > optionsMaxNumber:

                validNumber = False

        if not validNumber:

            print('')
            print('Informe uma opção válida.')

            lib.screen.pause_screen()

    return chosenNumber


def main():

    menuOptions = ('1 - Adicionar produto', '2 - Atualizar produto', '3 - Remover produto',
                   '4 - Listar produtos', '5 - Buscar produto', '6 - Total em estoque', '0 - Sair')

    inputMessage = 'Escolha uma das opções acima: '

    fieldsLabels = ['Nome', 'Quantidade', 'Preço']
    fieldsNames = ['nome', 'quantidade', 'preco']
    fieldsTypes = ['TEXT', 'INTEGER', 'REAL']
    fieldsContent = []

    while True:

        chosenNumber = show_options(menuOptions, inputMessage)

        match(chosenNumber):
            case 1:

                ProdutoController.insertOption(
                    fieldsLabels, fieldsTypes, fieldsContent)

            case 2:

                ProdutoController.updateOption(
                    fieldsLabels, fieldsNames, fieldsTypes, fieldsContent)

            case 3:

                ProdutoController.deleteOption()

            case 4:

                ProdutoController.selectOption(
                    1, 'LISTA DE PRODUTOS CADASTRADOS')

            case 5:

                ProdutoController.selectOption(2, "BUSCA DE PRODUTO")

            case 6:

                ProdutoController.selectOption(1, 'PRODUTOS EM ESTOQUE', False)

                print('')

                # if cursor.execute(SQLStatement):

                #     SQLStatement = '''
                #         SELECT SUM(quantidade)
                #         FROM produtos
                #     '''

                #     if cursor.execute(SQLStatement):

                #         recordsList = cursor.fetchall()

                #         quantidadeTotal = recordsList[0]

                #     print('QUANTIDADE TOTAL:', quantidadeTotal[0])

                #     SQLStatement = '''
                #         SELECT SUM(quantidade * preco)
                #         FROM produtos
                #     '''

                #     if cursor.execute(SQLStatement):

                #         recordsList = cursor.fetchall()

                #         valorTotal = recordsList[0]

                #     print('VALOR TOTAL:', 'R$ {:,.2f}'.format(valorTotal[0]))

                #     lib.screen.pause_screen()

            case 0:

                break

    # conn.commit()

    # conn.close()

    os.system("cls")


if __name__ == '__main__':

    main()
