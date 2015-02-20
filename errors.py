class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return rep(self.value)
    
class EquationError(Error):
    def __init__(selfvalue):
        self.value = value
    
    def __str__(self):
        return self.value