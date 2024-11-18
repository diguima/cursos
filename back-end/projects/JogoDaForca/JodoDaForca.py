import random
import os
import time

def show_wrong_letters(wrongLetters):    

    lettersToShow = ""  

    for letter in wrongLetters:

        if letter not in lettersToShow:

            lettersToShow += letter + " "

    print(lettersToShow + "\n")

def show_screen(wrongLetters, trysNumber, word):

    imagens_forca = [
        """
        -----
         |  |
            |
            |
            |
            |
        =======
        """,
        """
        -----
         |  |
         O  |
            |
            |
            |
        =======
        """,
        """
        -----
         |  |
         O  |
         |  |
            |
            |
        =======
        """,
        """
        -----
         |  |
         O  |
        /|  |
            |
            |
        =======
        """,
        """
        -----
         |  |
         O  |
        /|\ |
            |
            |
        =======
        """,
        """
        -----
         |  |
         O  |
        /|\ |
        /   |
            |
        =======
        """,
        """
        -----
         |  |
         O  |
        /|\ |
        / \ |
            |
        =======
        """
    ]    

    os.system("cls")
    
    print("*** JOGO DA FORCA ***\n")
    
    show_wrong_letters(wrongLetters)
    
    print(imagens_forca[trysNumber])
    print(word + "\n")

def main():
    
    words = ["python", "programacao", "desenvolvimento", "tecnologia"]

    secretWord = random.choice(words)

    errors = trysNumber = 0
    
    wrongLetters = lettersFounded = typedLetters = finalWord = ""

    maxTrys = 6

    wordHit = False
        
    secretWordLen = len(secretWord)        
    
    while trysNumber < maxTrys and not wordHit:

        show_screen(wrongLetters, trysNumber, finalWord)
    
        letter1 = input("Informe uma letra: ")

        letter1 = letter1.lower()

        if not letter1.isalpha():

            print("Informe somente letras.\n")

            time.sleep(3)

            continue

        if letter1 in typedLetters:

            print("A letra '" + letter1 + "' já foi informada.\n")

            time.sleep(3)

            continue

        finalWord = ""

        typedLetters += letter1
            
        letterFounded = False
        
        for letter2 in secretWord:

            if letter1 == letter2:

                lettersFounded += letter1

                finalWord += letter1
                
                letterFounded = True
            
            elif letter2 in lettersFounded:

                finalWord += letter2
        
            else:        

                finalWord += "_"                     


        if letterFounded == False:        

            trysNumber += 1            
            wrongLetters += letter1

        if finalWord == secretWord:

            finalWord = secretWord
            wordHit   = True            
                    
    if wordHit:        

        show_screen(wrongLetters, trysNumber, secretWord)

        print("VOCÊ ACERTOU!")

    else:

        print("Você não acertou. A palavra era '" + secretWord + "'.\n")

if __name__ == '__main__':

    main()