class Square:

    def __init__(self, width, length):
        self._width = int(width)
        self.length = int(length)

    @property
    def width(self):
        return self._width
    
    @property
    def length(self):
        return self.length

    @property
    def area(self):
        return self._width ** 2 

