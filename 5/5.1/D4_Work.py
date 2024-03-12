class Programmer:

    def __init__(self, name, position):
        self.position_salary = {'Junior': 10, 'Middle': 15, 'Senior': 20}
        self.name = name
        self.time = 0
        self.salary = self.position_salary[position]
        self.full_salary = 0

    def work(self, time):
        self.time += time
        self.full_salary += time * self.salary

    def info(self):
        output = f'{self.name} {self.time}ч. {self.full_salary}тгр.'
        return output

    def rise(self):
        if self.salary < 20:
            self.salary += 5
        else:
            self.salary += 1


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
