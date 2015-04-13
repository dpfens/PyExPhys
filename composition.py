from math import log, pow
from datetime import datetime
from dateutil.relativedelta import relativedelta
from validate import validate
# Net Caloric Cost
# Mets must be in MET form (not mL/kg/min)


class Composition(object):
    
    def __init__(self, dateofbirth, weight, height):
        self.dob = dateofbirth
        self.weight = float(weight)
        self.height = float(height)
    
    def get_age(self):
        now = datetime.now()
        delta = relativedelta(now,self.dob)
        time = delta.years + float(delta.months/12.0)
        return time
        
    def net_cal_cost(self, mets):
        data = mets * 3.5 * (self.weight/200)
        return data                
    
    # Population-specific Formulas for converting Body Density (Db) to Percent Body Fat (%BF) 
    @staticmethod
    def db_to_bf(bd):
        bd = float(bd)
        data = {
            "Brozek": (4.570/bd)-4.142,
            "Siri": (4.95/bd)-4.50
        }
        return data    
    
                    
    
    # Calculation of body surface area in Meters^2
    # self.weight in kilogams (kg)
    # self.height in centimeters (cm)
    def bsa(self):
        height = self.height*100
        data = { 
            "Boyd": 0.03330 * pow(self.weight,(0.7285-0.0188*math.log(self.weight)))*pow(height,0.3),
            "Costeff": (4*self.weight+7)/(90+self.weight),
            "DuBois": 0.0087184 * pow(self.weight,0.425) * pow(height,0.725),
            "Fujimoto": 0.008883 * pow(self.weight, 0.444) * pow(height, 0.663),
            "GehanGeorge": 0.0235 * pow(self.weight, 0.51456) * pow(height, 0.42246),
            "Haycock": 0.024265 * pow(self.weight, 0.5378) * pow(height, 0.3964),
            "Mosteller": math.sqrt(self.weight*height)/60,
            "Takahira": 0.007241 * pow(self.weight, 0.425) * pow(height,0.725) }
        return data
    
                    
    
    # Body volume calculation from hydrostatic weighing
    # uww is Underwater self.weight
    # rv is Residual Volume in mL
    # gv is Volume of air in gastrointestinal tract (GV) (default: 100mL)
     
    def body_vol(self, uww, rv, gv, **kwargs):
        water_density = kwargs.get('water_density',1)
        uww = float(uww)
        rv = float(rv)
        gv = float(gv) or 0.1
        data = ((self.weight - uww)/ waterdensity) - (rv - gv)
        return data    
    
    
class Adult_Composition(Composition):
    
    def __init__(self, dateofbirth, weight, height):
        super(Adult_Composition, self).__init__(dateofbirth, weight, height)

class Man_Composition(Adult_Composition):
    def __init__(self, dateofbirth, weight, height):
        super(Man_Composition, self).__init__(dateofbirth, weight, height)
    
    
    # Calculate Body Density at TLCNS
    def db_at_tlcns(self, bd):
        bd = float(bd)
        data = 0.5829*bd+0.4059
        return data
    
    
    def skinfold_db(self, sum):
        age = self.get_age()
        sum = float(sum)
        data = {
            # Jackson and Pollock (1978)
            "black_hispanic": 1.112 - (0.00043499*sum) + (0.00000055*pow(sum, 2)) - (0.00028826*age),
            # Jackson and Pollock (1978)
            "white": 1.10938 - (0.0008267*sum) + (0.0000016*pow(sum, 2)) - (0.0002574*age),
            # Jackson and Pollock (1978)
            "athlete": 1.112 - (0.00043499*sum) + (0.00000055*pow(sum, 2)) - (0.00028826*age),
            # Evans et al. (2005)
            "collegiate_athlete": {
                "black": 8.997 + (0.2468*sum) - (6.343 * 1) - (1.998),
                "white": 8.997 + (0.2468*sum) - (6.343 * 1),
            },
        }
        return data
    
    # BMI to body fat %
    def bmi_to_bf(self):
        age = self.get_age()
        bmi = (self.weight/pow(self.height/100, 2))
        data = ((1.20*bmi) - (0.23*age) - (10.8) - 5.4) / 100
        return data
    
    # Total Daily Energy Expenditure of Children and Adults
    # age in years
    # self.weight in kilograms (kg)
    # self.height in meters
    # returns object with sedentary (1.0 < PAL < 1.4), low activity (1.4 < PAL < 1.6), active (1.6 < PAL < 1.9), and very active (1.9 < PAL < 2.5) 
    
    def predicted_tee(self):
        age = self.get_age()
        if (age >= 3 and age <= 18):
            data = {
                "sedentary": 88.5 - (61.9 * age) + 1*((26.7*self.weight)+(903*self.height)),
                "low": 88.5 - (61.9 * age) + 1.13*((26.7*self.weight)+(903*self.height)),
                "active": 88.5 - (61.9 * age) + 1.26*((26.7*self.weight)+(903*self.height)),
                "very_active": 88.5 - (61.9 * age) + 1.42*((26.7*self.weight)+(903*self.height)),
            }
        elif (age >= 19):
            data = {
                "sedentary": 662 - (9.53 * age) + 1*((15.9*self.weight)+(540*self.height)),
                "low": 662 - (9.53 * age) + 1.11*((15.9*self.weight)+(540*self.height)),
                "active": 662 - (9.53 * age) + 1.25*((15.9*self.weight)+(540*self.height)),
                "very_active": 662 - (9.53 * age) + 1.48*((15.9*self.weight)+(540*self.height)),
            }
        return data    
    
    
    # Calculate Fat Free Body Mass (FFM) based on impedance
    # resistance in ohms
    # height in centimeters (cm)
    # weight in kg
    # returns fat free mass (FFM) in kg
    
    def ffm(self, resistance, reactance):
        age = self.get_age()
        height = height*100
        resistance = float(resistance)
        reactance = float(reactance)
        results = {}
        
        if(age >= 17 and age <= 62): # Adults between 17 and 62
            results["adult"] = {
            
                # American Indian, black, Hispanic, and White Men
                # %BF < .20 Segal et al. (1988)
                "lean": (0.00066360*pow(height,2)) - (0.02117 * resistance) + (0.62854*self.weight) - (0.12380 * age) + 9.33285,
                
                # American Indian, black, Hispanic, and White Men
                # %BF > .20 Segal et al. (1988)
                "obese": (0.00088580*pow(height,2)) - (0.02999 * resistance) + (0.42688*self.weight) - (0.07002 * age) + 14.52435,
            }
        
         # Male athletes 19-40 years
         # Oppliger et al. (1991)
         
        if (age >= 19 and age <= 40):
            results["athlete"] = (0.186*(pow(height,2)/resistance)) + (0.701*self.weight) + 1.949
        results["adult"]["average"] = (results["adult"]["lean"] + results["adult"]["obese"]) / 2
        return results
    
    # Resting Metabolic Rate
    # self.weight in kg, height in cm, age in years
    def rmr(self):
        data = {
            'Harris-Benedict': 66.473 + 13.751*self.weight + 5.0033*height - 6.755*age,
            'Mifflin': (9.99*self.weight + 6.25*height + - 4.92*age)+5
        }
        return data

class Woman_Composition(Adult_Composition):
    
    def __init__(self, dateofbirth, weight, height):
        super(Woman_Composition, self).__init__(dateofbirth, weight, height)
    
    # Calculate Body Density at TLCNS
    def db_at_tlcns(self, bd):
        bd = float(bd)
        data = 0.4745*bd + 0.5173
        return data
    
    def skinfold_db(self, sum):
        age = self.get_age()
        sum = float(sum)
        data = {
            # Jackson et al. (1980)
            "black_hispanic": 1.0970 - (0.00046971*sum) + (0.00000056*pow(sum, 2)) - (0.00012828*age),
            # Jackson et al. (1980)
            "white_anorexic": 1.0994921 - (0.0009929*sum) + (0.0000023*pow(sum, 2)) - (0.00001392*age),
            # Jackson et al. (1980)
            "athlete": 1.096095 - (0.0006952*sum) + (0.0000011*pow(sum, 2)) - (0.0000714*age),
            # Evans et al. (2005)
            "collegiate_athlete": {
                "black": 8.997 + (0.2468*sum) - (1.998),
                "white": 8.997 + (0.2468*sum),
            },
        }
        return data
    
    def bmi_to_bf(self):
        age = self.get_age()
        bmi = (self.weight/pow(self.height/100, 2))
        data = ((1.20*bmi) - (0.23*age) - 5.4) / 100
        return data
    
    
     # Total Daily Energy Expenditure of Children and Adults
    # age in years
    # self.weight in kilograms (kg)
    # self.height in meters
    # returns object with sedentary (1.0 < PAL < 1.4), low activity (1.4 < PAL < 1.6), active (1.6 < PAL < 1.9), and very active (1.9 < PAL < 2.5) 
    
    def predicted_tee(self):
        age = self.get_age()
        if (age >= 3 and age <= 18):
            data = {
                "sedentary": 135.3 - (30.8 * age) + 1*((10*self.weight)+(934*self.height)),
                "low": 135.3 - (30.8 * age) + 1.16*((10*self.weight)+(934*self.height)),
                "active": 135.3 - (30.8 * age) + 1.31*((10*self.weight)+(934*self.height)),
                "very_active": 135.3 - (30.8 * age) + 1.56*((10*self.weight)+(934*self.height)),
            }
        elif (age >= 19):
            data = {
                "sedentary": 354 - (6.91 * age) + 1*((9.36*self.weight)+(726*self.height)),
                "low": 662 - (9.53 * age) + 1.12*((15.9*self.weight)+(540*self.height)),
                "active": 662 - (9.53 * age) + 1.27*((15.9*self.weight)+(540*self.height)),
                "very_active": 662 - (9.53 * age) + 1.45*((15.9*self.weight)+(540*self.height)),
            }
        return data   
    
    # Calculate Fat Free Body Mass (FFM) based on impedance
    # resistance in ohms
    # self.height in centimeters (cm)
    # self.weight in kg
    # returns fat free mass (FFM) in kg
    
    def ffm(self, resistance, reactance):
        age = self.get_age()
        height = self.height*100
        resistance = float(resistance)
        reactance = float(reactance)
        results = {}

        if(age >= 17 and age <= 62): # Adults between 17 and 62
            results['adult'] = {
            
                # American Indian, black, Hispanic, and White Women
                # %BF < .30 Segal et al. (1988)
             
                "lean": (0.000646*pow(height,2)) - (0.014 * resistance) + (0.421*self.weight) + 10.4,
            
                # American Indian, black, Hispanic, and White Women
                # %BF > .30 Segal et al. (1988)
             
                "obese": (0.00091186*pow(height,2)) - (0.1466 * resistance) + (0.29990*self.weight) - (0.07012 * age) + 9.37938,
            }
            results["adult"]["average"] = (results["adult"]["lean"] + results["adult"]["obese"]) / 2
        
         # Female athletes 18-27 years
         # Fornetti et al. (1999)
         
        if (age >= 18 and age <=27):
            results["athlete"] = (0.282*height) + (0.415*self.weight) - (0.037*resistance) + (0.096*reactance) - 9.734
        return results
    
    # Resting Metabolic Rate
    # self.weight in kg, self.height in cm, age in years
    def rmr(self):
        age = self.get_age()
        height = self.height*100
        data = {
            'Harris-Benedict': 655.0955 + 9.463*self.weight + 1.8496*height - 4.6756*age,
            'Mifflin': (9.99*self.weight + 6.25*height + - 4.92*age)-161
        }
        return data

class Child_Composition(Composition):
    
    def __init__(self, dateofbirth, weight, height):
        super(Child_Composition, self).__init__(dateofbirth, weight, height)
    
    def ffm(self, resistance, reactance):
        age = self.get_age()
        resistance = float(resistance)
        reactance = float(reactance)
        results = {}      
        
        # White boys and girls, 8-15 years
        # Lohman(1992)
        if(age >= 8 and age <= 15):
            results["child"] = (0.62*(pow(self.height,2)/resistance)) + (0.21*self.weight) + (0.1*reactance) + 4.2
                        
        
        # White boys and girls, 10-19 years
        # Houtkooper e al. (1992)
        if(age >= 10 and age <= 19):
            results["adolescent"] = (0.61*(pow(self.height,2)/resistance)) + (0.25*self.weight) + 1.31
        return results

class Boy_Composition(Child_Composition):
    
    def __init__(self, dateofbirth, weight, height):
        super(Boy_Composition, self).__init__(dateofbirth, weight, height)
    
    def skinfold_db(self, sum):
        sum = float(sum)
        data = (0.735*sum) + 1.0
        return data
    
    def bmi_to_bf(self):
        age = self.get_age()
        bmi = (self.weight/pow(self.height/100, 2))
        data =  ((1.51*bmi) - (0.70*age) - (3.6) + 1.4) / 100,
        return data
    
     # Total Daily Energy Expenditure of Children and Adults
    # age in years
    # self.weight in kilograms (kg)
    # self.height in meters
    # returns object with sedentary (1.0 < PAL < 1.4), low activity (1.4 < PAL < 1.6), active (1.6 < PAL < 1.9), and very active (1.9 < PAL < 2.5) 
    
    def predicted_tee(self):
        age = self.get_age()
        data = {}
        if (age >= 3 and age <= 18):
            data = {
                "sedentary": 88.5 - (61.9 * age) + 1*((26.7*self.weight)+(903*self.height)),
                "low": 88.5 - (61.9 * age) + 1.13*((26.7*self.weight)+(903*self.height)),
                "active": 88.5 - (61.9 * age) + 1.26*((26.7*self.weight)+(903*self.height)),
                "very_active": 88.5 - (61.9 * age) + 1.42*((26.7*self.weight)+(903*self.height)),
            }
        return data   
    
    # Resting Metabolic Rate
    # self.weight in kg, self.height in cm, age in years
    def rmr(self):
        age = self.get_age()
        height = self.height*100
        data = {
            'Harris-Benedict': 66.473 + 13.751*self.weight + 5.0033*height - 6.755*age,
            'Mifflin': (9.99*self.weight + 6.25*height + - 4.92*age)+5
        }
        return data

class Girl_Composition(Child_Composition):
    def __init__(self, dateofbirth, weight, height):
        super(Girl_Composition, self).__init__(dateofbirth, weight, height)
    
    def skinfold_db(self, sum):
        sum = float(sum)
        data = (0.610*sum) + 5.1
        return data
    
    def bmi_to_bf(self):
        age = self.get_age()
        bmi = (self.weight/pow(self.height/100, 2))
        data = ((1.51*bmi) - (0.70*age) + 1.4) / 100
        return data
    
     # Total Daily Energy Expenditure of Children and Adults
    # age in years
    # self.weight in kilograms (kg)
    # self.height in meters
    # returns object with sedentary (1.0 < PAL < 1.4), low activity (1.4 < PAL < 1.6), active (1.6 < PAL < 1.9), and very active (1.9 < PAL < 2.5) 
    
    def predicted_tee(self):
        age = self.get_age()
        data = {}
        if (age >= 3 and age <= 18):
            data = {
                "sedentary": 135.3 - (30.8 * age) + 1*((10*self.weight)+(934*self.height)),
                "low": 135.3 - (30.8 * age) + 1.16*((10*self.weight)+(934*self.height)),
                "active": 135.3 - (30.8 * age) + 1.31*((10*self.weight)+(934*self.height)),
                "very_active": 135.3 - (30.8 * age) + 1.56*((10*self.weight)+(934*self.height)),
            }
        return data
    
    # Resting Metabolic Rate
    # self.weight in kg, self.height in cm, age in years
    def rmr(self):
        age = self.get_age()
        height = self.height*100
        data = {
            'Harris-Benedict': 655.0955 + 9.463*self.weight + 1.8496*self.height - 4.6756*age,
            'Mifflin': (9.99*self.weight + 6.25*self.height + - 4.92*age)-161
        }
        return data
    