class Orchestra:
    def play(self):
        raise NotImplementedError ("Method should be realised")
    def set_melody(self, new_melody):
        self.melody = new_melody

class Piano(Orchestra):
    def __init__(self, melody="--___-"):
        self.melody = melody

    def play(self, times=1):
        for _ in range(times):
            print(self.melody, end='')
        print()
class Violin(Orchestra):
    pass

piano = Piano("----...---")
piano.set_melody(new_melody="....||.|")
piano.play(5)

