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