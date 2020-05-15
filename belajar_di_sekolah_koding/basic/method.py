class Player:
    job = 'pemain bola'

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    @staticmethod
    def retiredIn(age):
        return str (40 - age)

    @classmethod
    def generalInfo(cls, age=10):
        return cls.job + ' ini akan pensiun dalam ' + cls.retiredIn(age) + ' tahun'

print(Player.generalInfo())

