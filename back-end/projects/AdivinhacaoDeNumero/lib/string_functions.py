def fill_string(string, char, totalSize, position="center"):
    
    stringSize = len(string)

    fillSize = totalSize - stringSize
    fillString = (char * fillSize)

    stringResult = ""

    if position.lower() == "left":

        stringResult == fillString + string 

    elif position.lower() == "right":

        stringResult == string + fillString

    else:

        leftFillSize = fillSize / 2
        rightFillSize = fillSize / 2

        if leftFillSize + rightFillSize + stringSize != totalSize:

            rightFillSize += 1

        stringResult = leftFillSize + string + rightFillSize

    return stringResult