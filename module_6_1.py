class Animal:
        self.alive = True
        self.fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.adible:   
            print(f'{self.name} съел {self.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {self.name}')
            self.fed = False
        
class Plant():
    adible = False
    def __init__(self, name):
        self.name = name
    

class Mammal(Animal):
    pass


class Predator(Animal):
    pass




class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, adible = False)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, adible = True)






a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
