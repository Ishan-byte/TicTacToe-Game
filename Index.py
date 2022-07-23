# Index class that will save a lot of time
# in short, index or the number inside the game box

class Index():
    # Constructor that creates and index object with a input name and value if provided
    def __init__(self, name, value = None):
        if(value != None):
            self.value =  value
        self.name = name
        self.value = value

   # method that sets the value for the index object 
    def setValue(self, value):
        self.value = value