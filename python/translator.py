import sys

def getInput():
    return sys.argv[1:]

def isBraille(param):
    for c in param:
        if c != '.' or c != 'O':
            return False
    return True

def tokenizeBraille(param):
    tokens = []
    step = 6
    start = 0
    stop = start + step
    while stop < len(param):
        tokens.append(param[start:stop])
        start += step
        stop += step
    return tokens

def mapAsciiToBraille(param):
    result = ''
    match param.lower():
        case 'a' | '1':
            result += 'O.....'
        case 'b' | '2':
            result += 'O.O...'
        case 'c' | '3':
            result += 'OO....'
        case 'd' | '4':
            result += 'OO.O..'
        case 'e' | '5':
            result += 'O..O..'
        case 'f' | '6':
            result += 'OOO...'
        case 'g' | '7':
            result += 'OOOO..'
        case 'h' | '8':
            result += 'O.OO..'
        case 'i' | '9':
            result += '.OO...'
        case 'j' | '0':
            result += '.OOO..'
        case 'k':
            result += 'O...O.'
        case 'l':
            result += 'O.O.O.'
        case 'm':
            result += 'OO..O.'
        case 'n':
            result += 'OO.OO.'
        case 'o':
            result += 'O..OO.'
        case 'p':
            result += 'OOO.O.'
        case 'q':
            result += 'OOOOO.'
        case 'r':
            result += 'O.OOO.'
        case 's':
            result += '.OO.O.'
        case 't':
            result += '.OOOO.'
        case 'u':
            result += 'O...OO'
        case 'v':
            result += 'O.O.OO'
        case 'w':
            result += '.OOO.O'
        case 'x':
            result += 'OO..OO'
        case 'y':
            result += 'OO.OOO'
        case 'z':
            result += 'O..OOO'
        case '.':
            result += '..OO.O'
        case ',':
            result += '..O...'
        case '?':
            result += '..O.OO'
        case '!':
            result += '..OOO.'
        case ':':
            result += '..OO..'
        case ';':
            result += '..O.O.'
        case '-':
            result += '....OO'
        case '/':
            result += '.O..O.'
        case '<':
            result += '.OO..O'
        case '>':
            result += 'O..OO.'
        case '(':
            result += 'O.O..O'
        case ')':
            result += '.O.OO.'
        case ' ':
            result += '......'
        case 'cap-follow':
            result += '.....O'
        case 'dec-follow':
            result += '.O...O'
        case 'num-follow':
            result += '.O.OOO'
        case _:
            result = ''
    return result

def asciiToBraille(param):
    result = ''
    inSentence = False
    inNumber = False
    for c in param:
        if c.isalpha() and not inSentence:
            result += mapAsciiToBraille('cap-follow')
            inSentence = True
            inNumber = False
        elif c.isnumeric() and not inNumber:
            result += mapAsciiToBraille('num-follow')
            inSentence = False
            inNumber = True
        elif c == '.' and inSentence:
            inSentence = False
        elif c == '.' and inNumber:
            result += mapAsciiToBraille('dec-follow')
        elif c == ' ' and inNumber:
            inNumber = False
        result += mapAsciiToBraille(c)
    return result

def brailleToAscii(param):
    tokens = tokenizeBraille(param)

def translate():
    params = getInput()
    result = ''
    for param in params:
        if isBraille(param):
            result += brailleToAscii(param)
        else:
            result += asciiToBraille(param)
    print(result)

translate()