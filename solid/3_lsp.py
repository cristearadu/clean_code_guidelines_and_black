class Bird:
    def fly(self):
        pass


# subclass of bird
class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")


# subclass of bird
class Penguin(Bird):
    # Penguins cannot fly, so we override the fly method
    def fly(self):
        print("Penguin cannot fly")


# take a bird object and make it fly
def make_bird_fly(bird):
    bird.fly()


sparrow = Sparrow()
penguin = Penguin()
make_bird_fly(sparrow)
make_bird_fly(penguin)