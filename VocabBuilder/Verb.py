class Verb:
    def __init__(self, name, defintion):
        self.name = name
        self.defintion = defintion

    

    def __str__(self):
        return self.name + ' : ' + self.defintion