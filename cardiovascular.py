import math
from errors import EquationError, InputError
from validate import validate

class Cardiovascular(object):
    
    def __init__(self, age, weight, height, **kwargs):
        # set Decimal precision
        self.age = age
        self.weight = float(weight)
        self.height= float(height)
    
    # 12 minute Run Test
    # Cooper (1968)
    # distance expected in meters
    @staticmethod
    def twelve_minute_vo2(distance):
        return 0.0268*distance - 11.3
            
    # 15 minute run test
    # Balke (1963)
    # distance expected in meters
    @staticmethod
    def fifteen_minute_vo2(distance):
        return 0.0178*distance + 9.6
                                    
        
    # 1.0 mile steady-state jog
    # George et al. (1993)
    # time in minutes
    def mile_steady_jog_vo2(self, time, hr):
        time = float(time)
        hr = float(hr)
        return  100.5 - 0.1636 * self.weight - 1.438 * time - 0.1928 * hr
      
    
    # Walking/Running Gross VO2
    # speed of treadmill in meters / minute
    # grade (% incline) of treadmill in decimal form (e.g. 10% = 0.10)
    @staticmethod 
    def wr_gross_vo2(speed, grade, **kwargs):
        walking = kwargs.get('walking', None)
        running = kwargs.get('running', None)
        speed = float(speed)
        grade = float(grade)
        if (speed >= 50 and speed <= 100 and not running) or walking: 
            # Walking (50-100m/min) or 1.9mph - 3.7mph
            data = (speed * 0.1) + (1.8 * speed * grade)
        
        elif (speed > 134 and not walking) or (speed > 80 and running):
            # Running (speed > 134 m/min) or speed > 5.0 mph
            # also used for speed > 80 m/min if running
            data = (speed * 0.2) + (0.9 * speed * grade)
        return data
                            
    # Leg Ergometry Gross VO2
    # work rate in kgm / min 1 Watt = 6 kgm / min
    # body mass in kilograms 1 kg = 2.2 lb
    @staticmethod 
    def leg_ergometry_vo2(work, mass):
        work = float(work)
        mass = float(mass)
        return 1.8 * work/mass + 3.5
                            
    # Arm Ergometry Gross VO2
    # work rate in kgm / min 1 Watt = 6 kgm / min
    # body mass in kilograms 1 kg = 2.2 lb
    @staticmethod 
    def arm_ergometry_vo2(work, mass, **kwargs):
        force = kwargs.get('force', Nones)
        work = float(work)
        mass = float(mass)
        return 3.0 * work/mass
                            
    # Stepping Gross VO2
    # frequency of stepping in steps per minute
    # bench self.height in meters 1 inch = 0.0254 meters
    def stepping_vo2(self, frequency):
        frequency = float(frequency)
        self.height = float(self.height)
        return (frequency * 0.2) + (frequency * self.height * 1.8 * 1.33)
                            
    # Submaximal Tests
                            
    
    # VO2 Reserve
    # max is Max VO2
    # rest is Resting VO2
    # reserve and rest must be of same unit type (METs or mL/kg/min)
    # 1 MET = 3.5 mL/kg/min
    @staticmethod 
    def vo2_reserve(max, rest):
        max = float(max)
        rest = float(rest)
        data = max - rest
        return data
                            
    
    # Target VO2 based on HR and VO2max
    # max = VO2max in mL/kg/min or METs
    # rest = VO2rest in mL/kg/min or METs
    # 1 MET = 3.5 mL/kg/min
    @staticmethod
    def vo2_target_vo2(intensity,max, rest):
        vo2_r = max - rest
        data = (intensity * vo2_r) + vo2_rest
        return data
    
    
    # Target VO2 
    # intensity as relative exercise percentself.age (e.g. 10% = 0.10)
    # reserve is Reserve VO2
    # rest is Resting VO2
    # reserve and rest must be of same unit type (METs or mL/kg/min)
    # 1 MET = 3.5 mL/kg/min
    @staticmethod 
    def karvonen_target_vo2(intensity, reserve, rest):
        intensity = float(intensity)
        reserve = float(reserve)
        rest = float(rest)
        data = (intensity * reserve) + rest
        return data
                            
    # HR Max
    def heart_rate_max(self):
        data = 208.0 - (0.7 * self.age)
        return data
                            
    # Target Heart Rate
    # intensity as relative exercise percentself.age (e.g. 10% = 0.10)
    # ACSM (2010) recommendation using 40% to 85% Hear Rate Reserve (HRR) for intensity
    # rest is resting heart rate
    # max is maximum heart rate
    # max and rest must be of same unit type
    @staticmethod
    def target_heart_rate(intensity, rest, max):
        intensity = float(intensity)
        rest = float(rest)
        max = float(max)
        data = (intensity * (max - rest)) + rest
        return data
                            
    # Device Specific Formulas
                            
    
    # Accurate StairMaster 4000 PT METs
    # setting is the Stairmaster MET setting
    @staticmethod
    def stairmaster_mets(setting):
        setting = float(setting)
        return 0.556 + 7.45 * setting 
    
    # Vital Capacity (VC = ERB + TV + IRV)
    # Inspiratory Capacity (IC = TV + IRV)
    # Functional Residual Capacity (FRC = RV + ERV)
    # Total Lung Capacity (TLC = RV + VC)
    @staticmethod 
    def total_lung_capacity(rv,vc):
        rv = float(rv) or 1300.0
        vc = float(vc) or 4700.0
        return rv + vc
    


class Adult_Cardiovascular(Cardiovascular):
    
    # Fox (1973) single stage cycle ergometer
    # single workload (900kgm/min or 150W) for 5 minutes
    # measure workload after 5 minutes
    @staticmethod
    def fox_cycle_ergometry_vo2max(hr5):
        return 6300.0-(19.26*hr5)
    
    

class Man_Cardiovascular(Adult_Cardiovascular):
    
    # Single Stage Treadmill Walk VO2max
    # Ebbeling and colleagues (1991)
    # used for low-risk adults 20-59 years old
    # speed in mph
    # heart rate (hr) in bpm
    def treadmill_walk_vo2max(self, speed, hr):
        gender = 1.0
        data = 15.1+(21.8*speed)-(0.327*hr)-(0.263*self.age)+( 0.00504*(hr*self.age) )+(5.48*gender)
        return data
    
    #  1 Mile Walk Test
    #  Kline et al. (1987)
    #  for gender field, 1 for male, 0 for female
    # time in minutes
    def mile_walk_vo2(self, time, hr):
        gender = 1.0
        return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*gender - 3.2649*time - 0.1565*hr
    
    
        # 1.5 mile run/walk
    # George et al. (1993)    
    # time in minutes
    def mile_half_wr_vo2(self, time, hr=None):
        gender = 1.0
        data = {}
        # George et al. (1993)
        data['george'] = 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*gender)
        
        if hr:
            # Larson et al (2002)
            data['larson'] = 100.16 + (7.30*gender) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr)
        return data
            
    # Astrand Step Test
    # Marley and Linnerud (1976)
    # Queen's College Step Test
    # McArdle et al. (1972)
    # For gender field, 1 for male, 0 for female
    # Male
    def step_test(self, hr):
        data = {
            "astrand":3.744*((self.weight+5)/(hr-62)),
            "queenscollege" :111.33 - (0.42 * hr)
        }
        return data
    
    # Single Stage Treadmill Jog VO2max
    # George et al. (1993)
    # used for younger adults (18 - 28 years old)
    # 4.5mph < speed < 6.5 mph for women
    # 4.3 mph < speed < 7.5 mph for men
    # client should jog at speed for 3 minutes
    # hr < 180 bpm
    # body weight in kg
    # speed in mph
    # hr in in bpm
    def treadmill_jogging_vo2max(self, speed, hr):
        gender= 1.0
        data = 54.07-(0.1938*self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*gender)
        return data
    
    
    # Submaximal protocols for VO2max calculation
    def treadmill_run_submax(self, sm1, hr1, sm2=None, hr2=None, **kwargs):
        hrmax = kwargs.get('hrmax', self.heart_rate_max())
        if sm2 and hr2:
            # Treadmill VO2 Max (MultiStage Model)
            # Client must reach steady state (115 < heart rate < 155)
            b = (sm2-sm1)/(hr2-hr1)
            data = sm2+b*(hrmax-hr2)
        else:
            # Treadmill VO2 Max (Single Stage Models)
            # Client must reach steady state (130 < heart rate < 150)
            data = sm1*( (hrmax-61) / (hr1-61) )
        return data
    
    
    def pop_vo2_max(self, time, time2=None, time3=None):
        time = float(time)
        time2 = float(time2)
        time3 = float(time3)
        data = {
            
            # Active & Sedentary Men
            # Pollock et al. (1976)
            # SEE = 2.50 (mL/kg/min)
            "balke": 1.444 * time + 14.99,
                
            # Naughton Protocol
            # Male cardiac patients
            # Foster et a. (1983)
            # SEE = 2.60 (mL/kg/min)
            "naughton": (1.61*time) +3.60, 
        }
        if time2 and time3:
            data["bruce"] = 14.76 - 1.379*time + 0.451*time2 - 0.012*time3
        # Bruce Protocol
            # Cardiac patients and Elderly Persons
            # McConnell and Clark (1987)
            # SEE = 4.9 (mL/kg/min)
        data["elderly_cardiac"] = (2.282*time) + 8.545
        return data
    
    
        # Tidal Volume (TV = IC - IRV) 
    # Inspiratory Reserve Volume (IRV = ERV + TV - VC)
    # Expiratory Reserve Volume (ERV = FRC - RV) 
    # Residual Volume (RV)
    # age in years
    # bsa in meters squared ( body surface area for females) or kilograms (body mass for males)
    def residual_volume(self):
        data = {
            "Berglund": (0.0115*self.age) + (0.019* self.height) - 2.24,
            "Boren": (0.022*self.age) + (0.0198*self.height) - (0.015*self.weight) - 1.54,
            "Goldman": (0.017*self.age) + (0.027*self.height) - 3.477,
        }
        return data  
    
    
    
class Woman_Cardiovascular(Adult_Cardiovascular):
    
    # Single Stage Treadmill Walk VO2max
    # Ebbeling and colleagues (1991)
    # used for low-risk adults 20-59 years old
    # speed in mph
    # heart rate (hr) in bpm
    def treadmill_walk_vo2max(self, speed, hr):
        gender = 0.0
        data = 15.1+(21.8*speed)-(0.327*hr)-(0.263*self.age)+( 0.00504*(hr*self.age) )+(5.48*gender)
        return data
    
    
    #  1 Mile Walk Test
    #  Kline et al. (1987)
    #  for gender field, 1 for male, 0 for female
    # time in minutes
    def mile_walk_vo2(self, time, hr):
        gender = 0.0
        return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*gender - 3.2649*time - 0.1565*hr
    
    
        # 1.5 mile run/walk
    # George et al. (1993)    
    # time in minutes
    def mile_half_wr_vo2(self, time, hr=None):
        gender = 0.0
        data = {}
        # George et al. (1993)
        data['george'] = 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*gender)
        
        if hr:
            # Larson et al (2002)
            data['larson'] = 100.16 + (7.30*gender) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr)
        return data
            
    # Astrand Step Test
    # Marley and Linnerud (1976)
    # Queen's College Step Test
    # McArdle et al. (1972)
    # For gender field, 1 for male, 0 for female
    # Male
    def step_test(self, hr):
            data = {
                "astrand":3.750*((self.weight-3)/(hr-65)),
                "queens_college": 65.81 - (0.1847 * hr)
            }  
            return data
    
    
    # Single Stage Treadmill Jog VO2max
    # George et al. (1993)
    # used for younger adults (18 - 28 years old)
    # 4.5mph < speed < 6.5 mph for women
    # 4.3 mph < speed < 7.5 mph for men
    # client should jog at speed for 3 minutes
    # hr < 180 bpm
    # body weight in kg
    # speed in mph
    # hr in in bpm
    def treadmill_jogging_vo2max(self, speed, hr):
        gender= 0.0
        data = 54.07-(0.1938*self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*gender)
        return data
    
    
    # Submaximal protocols for VO2max calculation
    def treadmill_run_submax(self, sm1, hr1, sm2=None, hr2=None, **kwargs):
        hrmax = kwargs.get('hrmax', self.heart_rate_max())
        if sm2 and hr2:
            # Treadmill VO2 Max (MultiStage Model)
            # Client must reach steady state (115 < heart rate < 155)
            b = (sm2-sm1)/(hr2-hr1)
            data = sm2+b*(hrmax-hr2)
        else:
            data = sm1*( (hrmax-72) / (hr1-72) )
        return data
    
    
    def pop_vo2_max(self, time, time2=None, time3=None):
        time = float(time)
        time2 = float(time2)
        time3 = float(time3)
        data = {
                   
                # Balke Protocol
                # Active & Sedentary Women
                # Pollock et al. (1982)
                # SEE = 2.20 (mL/kg/min)
                "balke": 1.38 * time + 5.22,
                    
                # Bruce Protocol
                # Active & Sedentary Women
                # Pollock et al. (1982)
                # SEE = 2.70 (mL/kg/min)
                "bruce": 4.38 * time - 3.90,
        },
               
            # Bruce Protocol
            # Cardiac patients and Elderly Persons
            # McConnell and Clark (1987)
            # SEE = 4.9 (mL/kg/min)
        data["elderly_cardiac"] = (2.282*time) + 8.545
        return data
    
    
        # Tidal Volume (TV = IC - IRV) 
    # Inspiratory Reserve Volume (IRV = ERV + TV - VC)
    # Expiratory Reserve Volume (ERV = FRC - RV) 
    # Residual Volume (RV)
    # age in years
    # bsa in meters squared ( body surface area for females) or kilograms (body mass for males)
    def residual_volume(self, bsa=None):
        data = {
            "Berglund": (0.0115*self.age) + (0.019* self.height) - 2.24,
            "Black": (0.021*self.age) + (0.023*self.height) - 2.978,
            "Goldman": (0.017*self.age) + (0.027*self.height) - 3.477,
        }
        if bsa:
            data["Obrien"]= (0.03*self.age) + (0.0387*self.height) - (0.73*bsa) - 4.78
        return data  
    
    
    
    
class Child_Cardiovascular(Cardiovascular):
    
    # 20m Shuttle Run Test
    # Leger et al. (1988)
    # Children 8-19 years old)
    def shuttle_run_vo2(speed):
        speed = float(speed)
        if self.age >= 8.0 and self.age<= 19.0:
            data = 31.025 + (3.238*speed) - (3.248*self.age) + 0.1536*(self.age*speed)
        else:
            raise EquationError('age must be between 8 and 19 (years)')
        return data
            
    
class Boy_Cardiovascular(Child_Cardiovascular):
    # 1.5 mile run/walk
    # George et al. (1993)    
    # time in minutes
    def mile_half_wr_vo2(self, time, hr=None):
        gender = 1.0
        
        # George et al. (1993)
        data['george'] = 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*gender)
        
        if hr:
            # Larson et al (2002)
            data['larson'] = 100.16 + (7.30*gender) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr)
        return data
            
    # Astrand Step Test
    # Marley and Linnerud (1976)
    # Queen's College Step Test
    # McArdle et al. (1972)
    # For gender field, 1 for male, 0 for female
    # Male
    def step_test(self, hr):
            data = {
                "astrand":3.744*((self.weight+5)/(hr-62)),
                "queenscollege" :111.33 - (0.42 * hr)
            }
            return data
        
    # 1.0 mile run/walk (8-17 years old)
    # Cureton et al. (1995)
    # for gender field, 1 for male, 0 for female
    # time in minutes
    def mile_run_walk_vo2(time, bmi):
        if self.age >= 8 and self.age <= 17:
            return 108.94 - (8.41 * time) + 0.34 * math.pow(time,2) + 0.21*(self.age*1.0) - (0.84*bmi)
        
    
    # Tidal Volume (TV = IC - IRV) 
    # Inspiratory Reserve Volume (IRV = ERV + TV - VC)
    # Expiratory Reserve Volume (ERV = FRC - RV) 
    # Residual Volume (RV)
    # age in years
    # bsa in meters squared ( body surface area for females) or kilograms (body mass for males)
    def residual_volume(self):
        data = {
            "Berglund": (0.0115*self.age) + (0.019* self.height) - 2.24,
            "Boren": (0.022*self.age) + (0.0198*self.height) - (0.015*self.weight) - 1.54,
            "Goldman": (0.017*self.age) + (0.027*self.height) - 3.477,
        }
        return data  

 
class Girl_Cardiovascular(Child_Cardiovascular):
    
    # 1.5 mile run/walk
    # George et al. (1993)    
    # time in minutes
    def mile_half_wr_vo2(self, time, hr=None):
        gender = 0.0
        
        # George et al. (1993)
        data['george'] = 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*gender)
        
        if hr:
            # Larson et al (2002)
            data['larson'] = 100.16 + (7.30*gender) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr)
        return data
            
    # Astrand Step Test
    # Marley and Linnerud (1976)
    # Queen's College Step Test
    # McArdle et al. (1972)
    # For gender field, 1 for male, 0 for female
    # Male
    def step_test(self, hr):
            data = {
                "astrand":3.750*((self.weight-3)/(hr-65)),
                "queens_college": 65.81 - (0.1847 * hr)
            }  
            return data
    
    # 1.0 mile run/walk (8-17 years old)
    # Cureton et al. (1995)
    # for gender field, 1 for male, 0 for female
    # time in minutes
    def mile_run_walk_vo2(time, bmi):
        if self.age >= 8 and self.age <= 17:
            return 108.94 - (8.41 * time) + 0.34 * math.pow(time,2) + 0.21*(self.age) - (0.84*bmi)
    
    
    # Tidal Volume (TV = IC - IRV) 
    # Inspiratory Reserve Volume (IRV = ERV + TV - VC)
    # Expiratory Reserve Volume (ERV = FRC - RV) 
    # Residual Volume (RV)
    # age in years
    # bsa in meters squared ( body surface area for females) or kilograms (body mass for males)
    def residual_volume(self, bsa=None):
        data = {
            "Berglund": (0.0115*self.age) + (0.019* self.height) - 2.24,
            "Black": (0.021*self.age) + (0.023*self.height) - 2.978,
            "Goldman": (0.017*self.age) + (0.027*self.height) - 3.477,
        }
        if bsa:
            data["Obrien"]= (0.03*self.age) + (0.0387*self.height) - (0.73*bsa) - 4.78
        return data  