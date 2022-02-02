import datetime

class Dog:
    def __init__(self, name, age, temperment):
        self.name = name
        self.age = age
        self.temperment = temperment
       #self.species = species
    
    #Dog Sparking
    def description(self):
        return f"{self.name} is {self.age} years old"
    #Dog Snoring
    def speak(self, x):
        return f"{self.name} says {x}"
    #changes method name to output of function (dunder method)
    def __str__(self) -> str:
        return f"{self.name} the greatest goodboy"

class Staffie(Dog):
    def speak(self, x = "HMPPPPPPPPPPPPPFF"):
        return f"{self.name} says {x}"

class CockerSpaniel(Dog):
    def speak(self, x = "HMPPPPPPPPPPPPPFF"):
        return super().speak(x)

class Dalmation(Dog):
    pass


jeffrey = Staffie(
            name = "Jeffrey", 
            age = 10, 
            temperment = "touchy",
)

bruno = CockerSpaniel(
            name = "Bruno", 
            age = 1, 
            temperment = "playful",
)

seven = Dalmation(
            name = "Seven", 
            age = 20, 
            temperment = "Silly",
)



print(bruno.speak())