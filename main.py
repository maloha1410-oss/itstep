import random


class Student:
    def __init__(self, subjects):
        self.subjects = subjects
        self.money = 100
        self.knowledge = 50

    def __len__(self):
        return len(self.subjects)

    def study(self):
        print("Студент вчиться")
        self.knowledge += 10

    def work(self):
        print("Студент працює")
        self.money += 20

    def rest(self):
        print("Студент відпочиває")
        self.money -= 10
        self.knowledge -= 5

    def live_day(self):
        if self.money < 20:
            self.work()
        elif self.knowledge < 30:
            self.study()
        else:
            action = random.choice([self.study, self.work, self.rest])
            action()

        print("Гроші:", self.money, "Знання:", self.knowledge)


s1 = Student(["алгебра", "геометрія", "укрмова"])

print("Кількість предметів:", len(s1))

for day in range(365):
    print("\nДень", day + 1)
    s1.live_day()