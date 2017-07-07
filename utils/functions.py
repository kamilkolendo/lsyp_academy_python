class Animal:
    def __init__(self, name, method):
        self.name = name
        self.make_sound = method

def moo():
    print("Moooooo!")

def quack():
    print("Quack Quack!")

def kalamalu():
    print("KALAMALUUUUUUUUUU!")

me = Animal("Kamcio", kalamalu)
me.make_sound()