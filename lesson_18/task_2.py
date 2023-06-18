class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = None
        self.boss = boss

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.__boss = new_boss


boss1 = Boss(1, "Ivan", "Google")
boss2 = Boss(2, "Viktor", "Facebook")

worker1 = Worker(1, "Nastya", "Google", boss1)
worker2 = Worker(2, "Kateryna", "Facebook", boss1)
worker3 = Worker(3, "Oksana", "Google", boss2)

boss1.add_worker(worker1)
boss1.add_worker(worker2)
boss2.add_worker(worker3)

print(worker1.boss.name)
print(worker3.boss.name)
print(worker2.boss.name)
