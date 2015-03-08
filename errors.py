class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, value, expected_type):
        self.value = value
        self.type = expected_type
    
    def __str__(self):
        return rep("%s must be type %s" % self.value, self.type)
    
class EquationError(Error):
    def __init__(selfvalue):
        self.value = value
    
    def __str__(self):
        return self.value