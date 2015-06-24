class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Pet):

    def __init__(self, name):
        Pet.__init__(self, name, "Dog")
    def __str__(self):
	return "Dog wong"

dog = Dog("Mister")
print dog
print dog.name
