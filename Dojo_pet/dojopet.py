from classes.ninja import Ninja
from classes.pet import Pet, Pug

smoky_the_pug = Pug("Smoky", "Pug", "Sing", 80, 100)
jake_the_dog = Pet("Jake", "English Bulldog", "Dance", 100, 50)
ninja_finn = Ninja("Finn", "Mertens", "Ice Cream",
                   "Everything Burrito", smoky_the_pug)
# smoky_the_pug.sleep()
ninja_finn.walk().feed().bathe()


# print(smoky_the_pug)
