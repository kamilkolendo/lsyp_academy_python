class Animal:

    some_string = "adadada" #cos jak pole statyczne dla klasy ale jak sie odwolujemy to i tak trzeba przez self.some_string

    def __init__(self, name):
        self.name = name
        self._private_field = name #konwencja ze _ oznacza pole prywatne, w rzeczywistosci masz dostep do wszystkiego

    def introduce_yourself(self):
        print(f"My name is {self.name}")
        print(self.some_string)

    @staticmethod
    def static_animal_method():
        print("as")


a = Animal('Jeff')
a.introduce_yourself()