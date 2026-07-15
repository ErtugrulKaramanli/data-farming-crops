class Corn:
    def __init__(self):
        # grains isimli instance variable sıfırla başlatılır
        self.grains = 0

    def water(self):
        # her çağrıldığında 10 tane grain ekler
        self.grains += 10

    def ripe(self):
        # grain sayısı en az 15 ise True, değilse False döner
        return self.grains >= 15
