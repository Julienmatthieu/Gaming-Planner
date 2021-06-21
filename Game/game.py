class Game(object):
    id = 0
    name = ""
    image = ""

    def __init__(self, id, name, image):
        self.id = id
        self.name = name
        self.image = image

    def print(self):
        print(f"this is game id {self.id}: \n\
                            \name = {self.name} \n\
                            \nimage = {self.image} \n\
                            \n")