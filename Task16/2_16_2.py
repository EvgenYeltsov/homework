# Task2

class Boss:

    def __init__(self, id_, name, company):
        self.id_ = id_
        self.name = name
        self.company = company
        self.workers = []

    def __repr__(self):
        return f"Boss {self.name} workers - {self.workers}"


class Worker:

    def __init__(self, id_, name_, company, boss: Boss):
        self.id_ = id_
        self.name_ = name_
        self.company = company
        self._boss = boss
        self._boss.workers.append(self)
        # self.boss = self.Boss()

    @property
    def boss(self):
        return self.boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss.workers.remove(self)
            self.boss = new_boss
        self.boss.workers.append(self)

    def __repr__(self):
        return repr((f"{self.name_}, iD - {self.id_}"))


b1 = Boss(1, 'Pit', 'G1')
w1 = Worker(10, 'And', 'G1', b1)
w2 = Worker(11, 'Kate', 'G1', b1)
w3 = Worker(11, 'Kat1', 'G1', b1)


b2 = Boss(2, 'Jhon', 'G2')
w5 = Worker(12, 'Rex', 'G1', b2)
w4 = Worker(13, 'Nix', 'G1', b2)


print(b1)
print(b2)



