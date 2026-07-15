class Rice:
    def __init__(self):
        # grains değişkeni sıfırla başlar
        self.grains = 0

    def water(self):
        # water metodu yalnızca 5 grains ekler
        self.grains += 5

    def ripe(self):
        # Corn ile aynı davranış: grain sayısı en az 15 ise True, değilse False
        return self.grains >= 15

    def transplant(self):
        # Rice sınıfına özel transplant metodu: 10 grain ekler
        self.grains += 10
