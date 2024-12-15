from Models.DBModel import DB
from Models.ProdutoModel import Produto
import Controllers.ProdutoController as ProdutoController
import lib.validations
import lib.string_functions
import lib.screen as screen
import os
import sqlite3
import time

optionsLables = ('1 - Adicionar produto', '2 - Atualizar produto', '3 - Remover produto',
                '4 - Listar produtos', '5 - Buscar produto', '6 - Total em estoque', '0 - Sair')

# Mostra opções


def show_options():

    inputMessage = 'Escolha uma das opções acima: '

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

        optionsMaxNumber -= 1

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

    while True:

        chosenNumber = show_options()

        match(chosenNumber):
            case 1:

                ProdutoController.insertOption()

            case 2:

                ProdutoController.updateOption()

            case 3:

                ProdutoController.deleteOption()

            case 4:

                ProdutoController.selectOption(1, 'LISTA DE PRODUTOS CADASTRADOS')

            case 5:

                ProdutoController.selectOption(2, "BUSCA DE PRODUTO")

            case 6:

                ProdutoController.selectOption(3, 'PRODUTOS EM ESTOQUE', False)

            case 0:

                break

    # conn.commit()

    # conn.close()

    os.system("cls")


if __name__ == '__main__':

    main()
