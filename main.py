# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class AnalizadorDeTexto:

    def __init__(self):
        self.letters = []
        self.text = self.__askingForLargeText()
        self.__askingFor3Letters()
        self.__countingLetters()
        self.__countingWords()
        self.__showsFirstAndLastWord()
        self.__reversingTextOrder()
        self.getPythonWord()

    def __askingForLargeText(self):
        text = input("Por favor ingresa un texto: ")
        return text

    def __askingFor3Letters(self):

        print("Please give me three different letters for me to process the information")
        for i in range(0, 3):
            letter = input("Could you please provide the letter {}: ".format((i+1)))
            self.letters.append(letter)

    def __countingLetters(self):

        for i in range(0, len(self.letters)):
            print("The letter '{}' appears {} times in this text".format(self.letters[i], self.text.upper().count(self.letters[i].upper())))

    def __countingWords(self):
        countingWords = len(self.text.split())
        print ("The text consists of {} word(s).".format(countingWords))

    def __showsFirstAndLastWord(self):
        first = self.text[0]
        last = self.text[-1]
        print("The first word is {} and the last one is {}".format(first, last))

    def __reversingTextOrder(self):
        text = self.text[::-1]
        print("The reverse form of the text '{}' appears as follows '{}'".format(self.text, text))

    def getPythonWord(self):
        if(self.text.upper().find("PYTHON")):
            print('Python appears in this text')
        else:
            print('Python doesnt appears')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analizandoTexto  = AnalizadorDeTexto()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
