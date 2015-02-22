from abc import ABCMeta, abstractmethod
from models import *
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from validate import validate

person_objects = {"person": Person, "adult": Adult, "man": Man, "woman": Woman, "child": Child, "boy": Boy, "girl": Girl}

class Person_Factory(object):
    def create(self, name, gender, date_of_birth, height=1, weight=1, race=None):
        
        if not validate.date(date_of_birth):
            raise TypeError("date_of_birth must be of type date or datetime")

        # if male
        if validate.male(gender)  and self.get_age(date_of_birth) < 18:
            person = Boy(name, date_of_birth, height, weight, race)
        elif validate.male(gender)  and self.get_age(date_of_birth) >= 18:
            person = Man(name, date_of_birth, height, weight, race)
        # If Female
        elif validate.female(gender) and self.get_age(date_of_birth) < 18:
            person = Girl(name, date_of_birth, height, weight, race)
        elif validate.male(gender) and self.get_age(date_of_birth) >= 18:
            person = Woman(name, date_of_birth, height, weight, race)
        
        # If Not Male or Female
        elif not validate.gender(gender) and self.get_age(date_of_birth) < 18:
            person = Child(name, date_of_birth, height, weight, race)
        elif validate.gender(gender) and self.get_age(date_of_birth) >= 18:
            person = Adult(name, date_of_birth, height, weight, race)
        else:
            person = Person(name, date_of_birth, height, weight, race)
        return person
    
    @staticmethod
    def get_age(dob):
        now = datetime.now()
        delta = relativedelta(now,dob)
        time = delta.years + float(delta.months/12.0)
        return time