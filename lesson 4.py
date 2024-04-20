class Human:
    height = 170


class Student(Human):
    height = 175



class Worker(Human):
    pass


vasya = Student()
lilya = Worker()


print(vasya.height)
print(lilya.height)
