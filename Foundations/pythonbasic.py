# Classes and Inheritance

class Pet(object):
    

    def __init__(self, species, name):
        self.species = species
        self.name = name

    
    def __str__(self) -> str:

        """
        Will printt this when Object of the class is printed
        """
        return f'{self.species} named {self.name} '

    
    def change_name(self, new_name):
        self.name = new_name

    

# Child class
class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(species="dog", name=name)
        self.breed = breed

    def __str__(self) -> str:
        return f' A  {self.breed} doggo named {self.name} '

    @classmethod
    def from_dict(cls, d):

        return cls(name=d["name"],breed = d["breed"]) # Create class instances by passing uninstatiated class itself
    
    @staticmethod
    def is_cute(breed): #can be called from uninstantiated object of the class
        return True


scooby = Pet(species="dog",  name = "Scooby")
# print(scooby )

d  ={"name":"A","breed":"Labra"}
cassie  = Dog.from_dict(d)
print(cassie)

Dog.is_cute(breed="A") # static method
