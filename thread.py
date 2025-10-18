from threading import*
def show():
    print('This is a child thread')
t= Thread(target=show())
t.start()
print('this is the parent thread')

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print('This is a child class')
t=MyThread()
t.start()
for i in range(5):
    print('This is the parent class')

class Demo:
    def show(self):
        for i in range(5):
            print('This is a child class')
obj=Demo()
t = Thread(target=obj.show())
t.start()
for i in range(5):
    print('This is the parent class')

