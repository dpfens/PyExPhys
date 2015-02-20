import math
from validate import Validator
from errors import InputError

validate = Validator()
    
    #  20m Shuttle Run Test
    #  Leger et al. (1988)
    #  Children 8-19 years old)
def shuttle_run_vo2():
    if age >= 8 and age<= 19:
        data =  31.025 + (3.238*speed) - (3.248*age) + 0.1536*(age*speed)
    else:
        raise InputError('age must be between 8 and 19 (years)')
    return data
        
    
    
    # 1.0 mile run/walk (8-17 years old)
    # Cureton et al. (1995)
    # for gender field, 1 for male, 0 for female
    # time in minutes
def mile_run_vo2(gender, age, time, bmi):
    if validate.male(gender):
        gender = 1
    elif validate.female(gender):
        gender = 0
    else:
        raise InputError("gender must be male or female")
    return 108.94 - (8.41 * time) + 0.34 * math.pow(time,2) + 0.21*(age*gender) - (0.84*bmi)
        

         # 12 minute Run Test
         # Cooper (1968)
         # distance expected in meters
def twelve_minute_vo2(distance):
    return 0.0268*distance - 11.3
        
        # 15 minute run test
        # Balke (1963)
        # distance expected in meters
def fifteen_minute_vo2(distance):
    return 0.0178*distance + 9.6
                                
    
    #  1 Mile Walk Test
    #  Kline et al. (1987)
    #  for gender field, 1 for male, 0 for female
    #  
def mile_walk_vo2(gender, age, time, weight, hr):
    if validate.male(gender):
        gender = 1
    elif validate.female(gender):
        gender = 0
    else:
        raise InputError("gender must be male or female")
    return 132.853 - .0769*weight - 0.3877*age + 6.315*gender - 3.2649*time - 0.1565*hr
                                
    
    # 1.0 mile steady-state jog
    # George et al. (1993)
def mile_steady_jog_vo2(weight, time, hr):
    return  100.5 - 0.1636 * weight - 1.438 * time - 0.1928 * hr
    
def mile_half_run_vo2(gender, time, weight, **kwargs):
    hr = kwargs.get('hr',None)
    if validate.male(gender):
        gender = 1
        data = 88.02 - (0.1656*weight) - (2.76*time) + (3.716*gender)
    elif validate.female(gender) and hr:
        gender = 0
        data = 100.16 + (7.30*gender) - (0.164*weight) - (1.273 * time) - (0.1563 * hr)
    else:
        raise InputError("gender must be male or female")
    return data
        
        # Astrand Step Test
        # Marley and Linnerud (1976)
        # Queen's College Step Test
        # McArdle et al. (1972)
        # For gender field, 1 for male, 0 for female
        # Male
def step_test(gender, weight, hr):
        if validate.male(gender):
            data = {"astrand":3.744*((weight+5)/(hr-62)),
            "queenscollege" :111.33 - (0.42 * hr)}
        # Female
        elif validate.female(gender): 
            data = {"astrand":3.750*((weight-3)/(hr-65)),
            "queens_college": 65.81 - (0.1847 * hr) } 
        else:
            raise InputError("gender must be male or female")
        return data
                            
# VO2 Max
def pop_vo2_max(time, time2=None, time3=None):
    time = int(time)
    time2 = int(time2)
    time3 = int(time3)
    if validate.male(gender):
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
    
    elif validate.female(gender): 
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
        data["elderly_cardiac"] = (2.282*time) + 8.545,
    return results
                        

# Walking VO2
# speed of treadmill in meters / minute
# grade (% incline) of treadmill in decimal form (e.g. 10% = 0.10) 
def walking_vo2(speed, grade):
    speed = int(speed)
    grade = int(grade)
    return (speed * 0.1) + (1.8 * speed * grade) + 3.5

# Running VO2
# speed of treadmill in meters / minute
# grade (% incline) of treadmill in decimal form (e.g. 10% = 0.10) 
def running_vo2(speed, grade):
    speed = int(speed)
    grade = int(grade)
    return (speed * 0.2) + (0.9 * speed * grade) + 3.5
                        
# Leg Ergometry VO2
# work rate in kgm / min 1 Watt = 6 kgm / min
# body mass in kilograms 1 kg = 2.2 lb
def leg_ergometry_vo2(work, mass):
    work = int(work)
    mass = int(mass)
    return 1.8 * work/mass + 3.5 + 3.5
                        
# Arm Ergometry VO2
# work rate in kgm / min 1 Watt = 6 kgm / min
# body mass in kilograms 1 kg = 2.2 lb
def arm_ergometry_vo2(work, mass):
    work = int(work)
    mass = int(mass)
    return 3.0 * work/mass + 3.5
                        
# Stepping VO2
# frequency of stepping in steps per minute
# bench height in meters 1 inch = 0.0254 meters
def stepping_vo2(frequency, height):
    frequency = int(frequency)
    height = int(height)
    return (frequency * 0.2) + (frequency * height * 1.8 * 1.33)+3.5
                        
# Submaximal Tests
                        

# VO2 Reserve
# max is Max VO2
# rest is Resting VO2
# reserve and rest must be of same unit type (METs or mL/kg/min)
# 1 MET = 3.5 mL/kg/min
def vo2_reserve(max, rest):
    max = int(max)
    rest = int(rest)
    data = max - rest
    return data
                        

# Target VO2 
# intensity as relative exercise percentage (e.g. 10% = 0.10)
# reserve is Reserve VO2
# rest is Resting VO2
# reserve and rest must be of same unit type (METs or mL/kg/min)
# 1 MET = 3.5 mL/kg/min
def target_vo2(intensity, reserve, rest):
    intensity = int(intensity)
    reserve = int(reserve)
    rest = int(rest)
    data = (intensity * reserve) + rest
    return data
                        
# HR Max
def heart_rate_max(age):
    age = int(age)
    data = 208 - (0.7 * age)
    return data
                        

# Target Heart Rate
# intensity as relative exercise percentage (e.g. 10% = 0.10)
# ACSM (2010) recommendati using 40% to 85% Hear Rate Reserve (HRR) for intensity
# rest is resting heart rate
# max is maximum heart rate
# max and rest must be of same unit type
def target_heart_rate(intensity, rest, max):
    intensity = int(intensity)
    rest = int(rest)
    max = int(max)
    data = (intensity * (max - rest)) + rest
    return data
                        
# Device Specific Formulas
                        

# Accurate StairMaster 4000 PT METs
# setting is the Stairmaster MET setting
def stairmaster_mets(setting):
    setting = int(setting)
    return 0.556 + 7.45 * setting
                        

# Tidal Volume (TV = IC - IRV) 
# Inspiratory Reserve Volume (IRV = ERV + TV - VC)
# Expiratory Reserve Volume (ERV = FRC - RV) 
# Residual Volume (RV)
# age in years
# bsa in meters squared ( body surface area for females) or kilograms (body mass for males)
def residual_volume(gender, age, height, weight, **kwargs):
    bsa = kwargs.get('bsa',None)
    weight = kwargs.get('weight',None)
    gender = gender.lower()
    age = int(age)
    height = int(height)
    if validate.male(gender) and weight:
        data = {
        "Berglund": (0.0115*age) + (0.019* height) - 2.24,
        "Boren": (0.022*age) + (0.0198*height) - (0.015*weight) - 1.54,
        "Goldman": (0.017*age) + (0.027*height) - 3.477,
        }
    if validate.female(gender) and bsa:
        data = {
        "Berglund": (0.0115*age) + (0.019* height) - 2.24,
        "Black": (0.021*age) + (0.023*height) - 2.978,
        "Goldman": (0.017*age) + (0.027*height) - 3.477,
        "Obrien": (0.03*age) + (0.0387*height) - (0.73*bsa) - 4.78
        }
    return data  

# Vital Capacity (VC = ERB + TV + IRV)
# Inspiratory Capacity (IC = TV + IRV)
# Functional Residual Capacity (FRC = RV + ERV)
# Total Lung Capacity (TLC = RV + VC)
def total_lung_capacity(rv,vc):
    rv = int(rv) or 1300
    vc = int(vc) or 4700                       
    return rv + vc
