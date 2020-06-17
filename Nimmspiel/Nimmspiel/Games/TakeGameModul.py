from Games.Game import Game
class TakeGame(Game):
    def __init__(self):
        self.__steine = 23
        self.__spielende = False


    def play(self):
        while not self.__spielende:
            self.__exceuteTurns ()

    def __exceuteTurns(self):
        self.__spielerzug()
        self.__computerzug()

    def __spielerzug(self):
        while True:
            zug = int(input("Es gibt {steine} Steine. Bitte nehmen Sie 1,2 oder 3.".format(steine = self.__steine)))
            if zug >= 1 and zug <= 3:
                break
            print("Ungültiger Zug")
        self.__steine -= zug

    def __computerzug(self):
        if self.__steine <= 0:
            print("Du Loser")
            self.__spielende = True
            return

        if self.__steine == 1:
            print("Du hast nur Glück gehabt")
            self.__spielende = True
            return

        zuege = (3,1,1,2)
        zug = zuege[self.__steine % 4]

        print ("Computer nimmt {zug} Steine".format(zug = zug))

        self.__steine -= zug


