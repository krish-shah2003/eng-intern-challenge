import sys

brailleToEng = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number"
}
engToBraille = {brailleToEng[key]: key for key in brailleToEng}

brailleToNum = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}
numToBraille = {brailleToNum[key]: key for key in brailleToNum}

def translateBraille(input_str):
    result = ""
    isCaps = False
    isNum = False
    isDec = False
    for i in range(0, len(input_str), 6):
        segment = input_str[i:i + 6]
        if segment not in brailleToEng:
            continue
        token = brailleToEng[segment]
        if token == "capital":
            isCaps = True
            isNum = isDec = False
        elif token == "number":
            isNum = True
            isCaps = isDec = False
        elif token == "decimal":
            isDec = True
            isCaps = isNum = False
        else:
            if isCaps and token.isalpha():
                result += token.upper()
            elif isNum:
                if segment in numToBraille:
                    result += numToBraille[segment]
                else:
                    result += token
                isNum = False
            elif isDec and token == ".":
                result += token
            else:
                result += token
            isCaps = False
    return result

def translateEnglish(input_str):
    result = ""
    isNum = False
    for letter in input_str:
        if letter.isnumeric():
            if not isNum:
                result += engToBraille["number"]
                isNum = True
            result += numToBraille[letter]
        else:
            isNum = False
            if letter.isupper():
                result += engToBraille["capital"]
            result += engToBraille[letter.lower()]
    return result

def translate(input_str):
    if len(input_str) % 6 == 0:
        return translateBraille(input_str)
    return translateEnglish(input_str)

if __name__ == "__main__":
    user_input = ' '.join(sys.argv[1:])
    print(translate(user_input), flush=True)
    ##

