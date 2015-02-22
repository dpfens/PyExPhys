import mets
from abc import ABCMeta, abstractmethod
from cardiovascular import *
from composition import *
from strength import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from validate import validate

class Person(object):
    
    def __init__(self, name, dateofbirth, height=1, weight=1, race=None):
        if validate.date(dateofbirth):
            self.name = name
            self.dob = dateofbirth
            self.height= height
            self.weight = weight
            self.race = race
            self.strength = Strength(self.get_age(), weight)
            self.cardio = Cardiovascular(self.get_age(), weight, height)
            self.composition = Composition(self.get_age(), weight, height)
        else:
            raise TypeError("date of birth must be a Date or DateTime object")
    
    def get_age(self):
        now = datetime.now()
        delta = relativedelta(now,self.dob)
        time = delta.years + float(delta.months/12.0)
        return time
    
        
class Adult(Person):
    def __init__(self, name, dateofbirth, height=1, weight=1, race=None):
        super(Adult, self).__init__(name, dateofbirth, height, weight, race)
        self.cardio = Adult_Cardiovascular(self.get_age(), weight, height)
        self.composition = Adult_Composition(self.get_age(), weight, height)
        self.strength = Adult_Strength(self.get_age(), weight)


class Man(Adult):
    def __init__(self, name, dateofbirth, height=1, weight=1, race=None):
        super(Man, self).__init__(name, dateofbirth, height, weight, race)
        self.cardio = Man_Cardiovascular(self.get_age(), weight, height)
        self.composition = Man_Composition(self.get_age(), weight, height)
        self.strength = Man_Strength(self.get_age(), weight)
    
    
class Woman(Adult):
    def __init__(self, name, dateofbirth, height=1, weight=1, race=None):
        super(Woman, self).__init__(name, dateofbirth, height, weight, race)
        self.cardio = Woman_Cardiovascular(self.get_age(), weight, height)
        self.composition = Woman_Composition(self.get_age(), weight, height)
        self.strength = Woman_Strength(self.get_age(), weight)
        


  
class Child(Person):
    def __init__(self, name, dateofbirth, height=1, weight=1, race=None):
        super(Child, self).__init__(name, dateofbirth, height, weight, race)
        self.cardio = Child_Cardiovascular(self.get_age(), weight, height)
        self.composition = Child_Composition(self.get_age(), weight, height)
        self.strength = Child_Strength(self.get_age(), weight)
    
class Boy(Child):
    def __init__(self, name, dateofbirth, height=1, weight=1, race=None):
        super(Boy, self).__init__(name, dateofbirth, height, weight, race)
        self.cardio = Boy_Cardiovascular(self.get_age(), weight, height)
        self.composition = Boy_Composition(self.get_age(), weight, height)
        self.strength = Boy_Strength(self.get_age(), weight)

class Girl(Child):
    def __init__(self, name, dateofbirth, height=1, weight=1, race=None):
        super(Girl, self).__init__(name, dateofbirth, height, weight, race)
        self.cardio = Girl_Cardiovascular( self.get_age(), weight, height)
        self.composition = Girl_Composition( self.get_age(), weight, height)
        self.strength = Girl_Strength(self.get_age(), weight)