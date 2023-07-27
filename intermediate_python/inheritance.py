class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        # str return string, if we use print(person), this string will be printed
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def become_older(self, years):
        self.age += years


# in brackets () we say from what class will new obj inherit...
class Worker(Person):
    def __init__(self, name, age, height, salary):
        # super is accessing the parent class, then we target init...
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    # Overriding do not need more annotation like in java, just simply override
    # function that you already defined in parent class...
    # in this case we could use function from parent, so we did but unneccessary to do that
    def __str__(self):
        return super(Worker, self).__str__() + ", Salary: {}".format(self.salary)


    def calc_yearly_salary(self):
        return self.salary * 12


# we can go on and on with an inheritance...
class Programmer(Worker):
    def __init__(self, name, age, height, salary, languages):
        # super is accessing the parent class, then we target init...
        super(Programmer, self).__init__(name, age, height, salary)
        self.languages = languages


if __name__ == '__main__':
    worker1 = Worker("Henry", 40, 176, 3000)
    print(worker1)
    print(worker1.calc_yearly_salary())


