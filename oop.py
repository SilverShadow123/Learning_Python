class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


        # self.name = 'sam'
        # self.gender = 'Male'
        # self.age = 22

    def talk(self):
        print('Hi, I am', self.name, 'I am a', self.gender, 'and I am', self.age, 'years old')

    def vote(self):
        if self.age <= 18:
            print('I am not eligible to vote')
        else:
            print('I am eligible to vote')


class car:
    def __init__(self,name,year=0,speed=0):
        self.name = name
        self.year = year
        self.speed = speed

    def getSpeed(self):
       print('Maximum Speed :', self.speed)
    def setSpeed(self, speed):
        self.speed = speed
    def getYear(self):
       print('Relesed :',self.year)


class Sedan(car):
    def accelerate(self):
        print('137')
    def openTrunk(self):
        print('Trunk has been opened')


class SUV(car):
    def accelerate(self):
        print('127')


objL = [Sedan('Camry'),SUV('RAV4')]

for obj in objL:
    print(obj.name+' : ', end='')
    obj.accelerate()





Honda = Sedan(2018, 150)
Honda.getSpeed()
Honda.accelerate()
Honda.openTrunk()

BMW = car(2018,155)
FORD = car(2016,140)
BMW.getYear()
BMW.setSpeed(143)
BMW.getSpeed()
FORD.getYear()

FORD.getSpeed()

obj1 = Person('Goku', 'Male', 100)
obj2 = Person('Naruto', 'Male', 16)
obj2.talk()
obj2.vote()
obj1.talk()
obj1.vote()




