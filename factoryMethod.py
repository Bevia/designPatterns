# The Factory Method design pattern is a creational pattern that provides an interface
# for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
#
# Here is a simple example in Python to demonstrate the Factory Method design pattern.
# Let('s say we want to create different types of animals (like Dog and Cat), and we want '
#     'to use a factory method to create these animals.)

### Step 1: Define an interface for the products (animals)


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


### Step 2: Implement concrete products (Dog and Cat)


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


### Step 3: Create the Factory Method in a Creator class


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


### Step 4: Use the Factory Method to create objects


def get_animal(factory: AnimalFactory):
    animal = factory.create_animal()
    print(f"The animal says: {animal.speak()}")


# Create a Dog using the DogFactory
dog_factory = DogFactory()
get_animal(dog_factory)  # Output: The animal says: Woof!

# Create a Cat using the CatFactory
cat_factory = CatFactory()
get_animal(cat_factory)  # Output: The animal says: Meow!

### Explanation

# 1. Animal: An abstract base class that defines the interface `speak` which all concrete animal classes must implement.
# 2. Dog and Cat: Concrete implementations of the `Animal` interface.
# 3. AnimalFactory: An abstract base class for the factory that declares the factory method `create_animal`.
# 4. DogFactory and CatFactory: Concrete implementations of the `AnimalFactory` that create instances of `Dog` and `Cat`, respectively.
# 5. get_animal function: This function takes an `AnimalFactory`, uses it to create an animal, and prints the animal's sound.
#
# By using this pattern, you can easily add new types of animals without changing the existing code. Just create a new factory for
# the new animal type, and everything else remains the same.
