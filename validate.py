import datetime, math
from errors import EquationError, InputError

class Validator(object):
    
    def __init__(self):
        self.genders = {"male": ["male", "m", "boy", "man", 1],
                       "female": ["female", "f", "girl", "woman", 0]}
        
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
        if value.lower() in self.genders['male']:
            valid =  True
        else:
            valid = False
        return valid
    
    def female(self, value):
        if value.lower() in self.genders['female']:
            valid =  True
        else:
            valid = False
        return valid
    
    def date(self, value):
        if isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
            valid =  True
        else:
            valid = False
        return valid
        
validate = Validator()
            
        
         