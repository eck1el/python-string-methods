# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class AnalizadorDeTexto:

    def __init__(self):
        self.letras = []
        self.texto = self.__solicitudTexto()
        self.__solicitudCincoLetras()
        self.__contamosAparicionLetras()
        self.__contamosCuantasPalabras()
        self.__showsFirstAndLastWord()

    def __solicitudTexto(self):
        texto = input("Por favor ingresa un texto: ")
        return texto

    def __solicitudCincoLetras(self):

        print("Por favor ingrese tres letras a su elección para procesar la información")
        for i in range(0, 3):
            letra = input("Por favor ingrese la letra {} para el analisis de texto: ".format((i+1)))
            self.letras.append(letra)

    def __contamosAparicionLetras(self):

        for i in range(0, len(self.letras)):
            print("La letra {} aparece {} veces en el texto".format(self.letras[i], self.texto.upper().count(self.letras[i].upper())))

    def __contamosCuantasPalabras(self):
        countingWords = len(self.texto.split())
        print ("El texto esta compuesto de {} palabra(s)".format(countingWords))

    def __showsFirstAndLastWord(self):
        first = self.texto[0]
        last = self.texto[-1]
        print("The first word is {} and the last one is {}".format(first, last))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analizandoTexto  = AnalizadorDeTexto()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
