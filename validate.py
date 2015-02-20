import math
from errors import EquationError, InputError

class Validator(object):
    
    def __init__(self):
        self.gender = {"male": ["male", "m", "boy", "man", 1],
                       "female": ["female", "f", "girl", "woman", 0]}
    
    @staticmethod
    def number(self, value):
        if isinstance(value, int) or isinstance(value, float) and value > 0:
            valid = True
        else:
            valid = False
        return valid
    
    def gender(self, value):
        if self.male(value) or self.female(value):
            valid =  True
        else:
            valid = False
        return valid
    
    def male(self,value):
        if value.lower() in self.gender['male']:
            valid =  True
        else:
            valid = False
        return valid
    
    def female(self, value):
        if value.lower() in self.gender['female']:
            valid =  True
        else:
            valid = False
        return valid
            
        
         