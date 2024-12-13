def fill_string(string, char, totalSize, position="center"):
    
    stringSize = len(string)

    fillSize = totalSize - stringSize
    fillString = (char * fillSize)

    stringResult = ""

    if position.lower() == "left":

        stringResult = fillString + string 

    elif position.lower() == "right":

        stringResult = string + fillString

    else:

        leftFillSize = int(fillSize / 2)
        rightFillSize = int(fillSize / 2)

        if leftFillSize + rightFillSize + stringSize != totalSize:

            rightFillSize += 1

        stringResult = (leftFillSize * char) + string + (rightFillSize * char)
    
    return stringResult

def quoted(string):

    return '\"' + string + '\"'