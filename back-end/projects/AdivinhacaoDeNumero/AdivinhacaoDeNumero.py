import random
import os

def is_number(numberStr):

    numbers = "0123456789"

    isOnlyNumbers = True

    if numberStr.strip() == "":
        
        isOnlyNumbers = False

    else:
           
        for char in numberStr:        

            if char not in numbers:

                isOnlyNumbers = False
                break

    return isOnlyNumbers

def main():

    os.system("cls")
    
    print("*" * 100)
    print(("*" * 40) + " ADIVINHE O NÚMERO " + ("*" * 41))
    print("*" * 100 + "\n")

    isValidRound = False

    maxRounds = 1
    
    while not isValidRound:

        roundsStr = input("Informe o número de rodadas que deseja jogar: ")

        roundsStr = roundsStr.strip()

        try:
        
            roundsNumber = int(roundsStr)

        except:

            roundsNumber = 0

        if not is_number(roundsStr):

            print("Informe somente números.\n")

            continue

        elif roundsStr == "" or roundsNumber <= 0:

            print("Informe um número.\n")

            continue

        else:

            isValidRound = True

    if roundsNumber <= 0:      

        roundsNumber = 1

    print("")
    print("Escolha um nível de dificuldade:\n")
    print("1 - Fácil")
    print("2 - Normal")
    print("3 - Difícil\n")

    isValidLevel = False

    while not isValidLevel:

        levelNumberStr = input("Nível: ")

        if levelNumberStr.strip() != "" and levelNumberStr.isdigit():

            number = int(levelNumberStr)

            if number < 1 or number > 3:

                print("Nível inválido.")

            else:

                isValidLevel = True

        else:
        
            print("Nível inválido.")

    levelNumber = int(levelNumberStr)

    if levelNumber == 1:
    
        maxTrys = 15
    
    elif levelNumber == 2:
        
        maxTrys = 10
    
    elif levelNumber == 3:

        maxTrys = 5

    round = 0

    while round < roundsNumber:

        round += 1

        print("")
        print(("*" * 45) + " RODADA " + str(round) + ("*" * 45) + " \n")

        print("Você tem " + str(maxTrys) + " tentativas!\n")
        
        randomNumber = random.randint(1, 100)

        counter = 0

        correctNumber = False    

        while counter < maxTrys:

            numberStr = input("Informe um número entre 1 e 100: \n")

            if not is_number(numberStr):

                print("Informe somente números.")

                continue
        
            counter += 1

            number = int(numberStr)

            if counter < maxTrys:

                if number < randomNumber:

                    print("O número informado é menor que o número a ser adivinhado.\n")

                elif number > randomNumber:

                    print("O número informado é maior que o número a ser adivinhado.\n")

                else:

                    correctNumber = True
                    break
        
        if correctNumber:

            print("")
            print("VOCÊ ACERTOU!")

        else:
        
            print("")
            print("Você não conseguiu adivinhar, o número era " + str(randomNumber) + ".\n")

        
            

if __name__ == '__main__':

    main()
