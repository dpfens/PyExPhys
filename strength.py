import math
from validate import validate

class Strength(object):
    def __init__(self, age, weight,**kwargs):
            self.age = float(age)
            self.weight = float(weight)

    muscle_balance_ratios = {
        "hip": 1.0,
        "elbow": 1.0,
        "trunk": 1.0,
        "ankle": 1.0,
        "shoulders": (2/3),
        "knee": 1.5,
        "shoulder_rotation": 1.5,
        "ankle_flexion": 3.0
    	}
    
    def is_muscle_balanced(group, rm1, rm):
        rm1 = float(rm1)
        rm2 = float(rm2)
        ratio = rm1/rm2
        if ratio > 0.9 * muscle_balance_ratios[group] and ratio < 1.1 * muscle_balance_ratios[group]:
        	return true
        return false
    
    
    # 1-RM Formula
    # Based on number of repetitions to fatigue in one set
    # reps must not exceed 10
    # weight is the weight lifted in lb
    def fatigue_rep_max(reps, weight):
        reps = float(reps)
        weight = float(weight)
        data = weight / (1.0278 - (reps * 0.0278))
        return data
    
    # 1-RM Formula
    # Based on the number of repetitions to fatigue obtained in two submaximal sets so long as number of reps is under 10
    # weight1 and weight2 must be of same unit (kg or lb)
    def two_set_max(rep1, wt1, rep2, wt2):
        rep1 = float(reps)
        wt1 = float(wt)
        rep2 = float(reps)
        wt2 = float(wt)
        data = ((wt1 - wt2)/(rep2 - rep1)) * (rep1 - 1) + wt1
        return data
    
    # Relative Strength
    # rm is 1-Rep Maximum
    # weight is the body mass of the individual
    # rm and weight must be of the same unit (kg or lbs)
    def relative_strength(rm, weight):
        rm = float(rm)
        weight = float(weight)
        return rm / weight
    
class Adult_Strength(Strength):
    
    def __init__(self, age, weight,**kwargs):
        self.age = float(age)
        self.weight = float(weight)
    
    #  gender-specific 1-RM Formula for Younger adults (22 - 36 years old)
    #  Kim, Mayhew, and Peterson (2002)
    #  return value in kg
    #  For gender field, 1 for male, 0 for female
    def ymca_upper_body_rep_max (reps):
        reps = float(reps) or 0
        data
        if validate.male(self.gender):
                data = (1.55 * reps) + 37.9
        elif validate.female(self.gender):
                data = (0.31 * reps) + 19.2 
        return data
    

class Man_Strength(Adult_Strength):
    def __init__(self,age, weight,**kwargs):
        self.age = float(age)
        self.weight = float(weight)
    
class Woman_Strength(Adult_Strength):
    def __init__(self,age, weight,**kwargs):
        self.age = float(age)
        self.weight = float(weight)
        
    # Middle Age (40-50 years old) & Older adult (60-70 years old) 1-RM
    # Kuramoto & Payne (1995)
    def female_rep_max(self, reps, weight):
        reps = float(reps)
        weight = float(weight)
        if (self.age >= 40 and self.age <= 50):
            data = (1.06 * weight) + (0.58 * reps) - (0.20 * self.age) - 3.41
        elif(self.age >= 60 and self.age <= 70):
            data = (0.92 * weight) + (0.79 * reps) - (0.20 * self.age) - 3.73
        return data
    
    @staticmethod
    def hip_rep_max(reps, wt):
        data = 100 * wt/(48.8+math.pow(53.8,(-0.075*reps) ))
        return data
    
class Child_Strength(Strength):
    def __init__(self, age, weight,**kwargs):
        self.age = float(age)
        self.weight = float(weight)
    
class Boy_Strength(Child_Strength):
    def __init__(self, age, weight,**kwargs):
        self.age = float(age)
        self.weight = float(weight)
    
class Girl_Strength(Child_Strength):
    def __init__(self, age, weight,**kwargs):
        self.age = float(age)
        self.weight = float(weight)