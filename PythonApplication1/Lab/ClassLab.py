class Aniaml(object):
    def run(self):
        print('Haha');

class Dog(Aniaml):
    pass;
class Cat(Aniaml):
    pass;

dog=Dog();
cat=Cat();

dog.run();
cat.run();
