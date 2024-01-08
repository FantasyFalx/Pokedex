# File to structure data properly to be sent to pokedata dir

# Pokemon object class 

class Pokemon():

    name = ""
    height = 0
    type = []
    sprite_image = ""


    # Constructor

    def __init__(self, name, height, type, sprite):

        self.name = name
        self.height = height
        self.type = type
        self.sprite_image = sprite