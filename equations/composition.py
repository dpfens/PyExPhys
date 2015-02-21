import math
from validate import validate
# Net Caloric Cost
# Mets must be in MET form (not mL/kg/min)

    
def net_caloric_cost(weight, mets):
    data = mets * 3.5 * (weight/200)
    return data

                   
def bmi_to_body_fat(gender, age, bmi):
    bmi = float(bmi)
    data = {}
    if validate.male(gender): 
        data = {
            "child": ((1.51*bmi) - (0.70*age) - (3.6) + 1.4) / 100,
            "adult": ((1.20*bmi) - (0.23*age) - (10.8) - 5.4) / 100
        }
    elif validate.female(gender):
        data = {
            "child": ((1.51*bmi) - (0.70*age) + 1.4) / 100,
            "adult": ((1.20*bmi) - (0.23*age) - 5.4) / 100
        }
    return data

                

# Population-specific Formulas for converting Body Density (Db) to Percent Body Fat (%BF) 
def Db_to_bf(bd):
    bd = float(bd)
    data = {"Brozek": ((4.570/bd)-4.142) , "Siri": ((495/bd)-450)}
    return data    

# Skinfold tests

def skinfold_Db(gender, age, sum):
    sum = float(sum)
    data = {}
    if validate.male(gender): # male
        data = {
            "black": 1.112 - (0.00043499*sum) + (0.00000055*Math.pow(sum, 2)) - (0.00028826*age),
            "white": 1.10938 - (0.0008267*sum) + (0.0000016*Math.pow(sum, 2)) - (0.0002574*age),
            "collegiate_athlete": {
            "black": 8.997 - (0.2468*sum) - (6.343 * 1) - (1.998),
            "white": 8.997 - (0.2468*sum) - (6.343 * 1),
            },
            "child": (0.735*sum) + 1.0
        }
    elif validate.female(gender):
        data = {
            "black_hispanic": 1.0970 - (0.00046971*sum) + (0.00000056*Math.pow(sum, 2)) - (0.00012828*age),
            "white_anorexic": 1.0994921 - (0.0009929*sum) + (0.0000023*Math.pow(sum, 2)) - (0.00001392*age),
            "athlete": 1.096095 - (0.0006952*sum) + (0.0000011*Math.pow(sum, 2)) - (0.0000714*age),
            "collegiate_athlete": {
                "black": 8.997 - (0.2468*sum) - (1.998),
                "white": 8.997 - (0.2468*sum),
            },
            "child": (0.610*sum) + 5.1
        }
    return data



# Calculate Body Density at TLCNS

def Db_at_tlcns(gender, bd):
    bd = float(bd)
    if validate.female(gender):
        data = 0.4745*bd + 0.5173
    elif validate.male(gender):
        data = 0.5829*bd+0.4059
    return data

                

# Calculation of body surface area in Meters^2
# weight in kilogams (kg)
# height in centimeters (cm)

def bsa(weight, height):
    data = { 
        "Boyd": 0.03330 * Math.pow(weight,(0.7285-0.0188*Math.log(weight)))*Math.pow(height,0.3),
        "Costeff": (4*weight+7)/(90+weight),
        "DuBois": 0.0087184 * Math.pow(weight,0.425) * Math.pow(height,0.725),
        "Fujimoto": 0.008883 * Math.pow(weight, 0.444) * Math.pow(height, 0.663),
        "GehanGeorge": 0.0235 * Math.pow(weight, 0.51456) * Math.pow(height, 0.42246),
        "Haycock": 0.024265 * Math.pow(weight, 0.5378) * Math.pow(height, 0.3964),
        "Mosteller": Math.sqrt(weight*height)/60,
        "Takahira": 0.007241 * Math.pow(weight, 0.425) * Math.pow(height,0.725) }
    return data

                

# Body volume calculation from hydrostatic weighing
# uww is Underwater weight
# rv is Residual Volume in mL
# gv is Volume of air in gastrointestinal tract (GV) (default: 100mL)
 
def body_volume( uww, rv, gv, **kwargs):
    water_density = kwargs.get('water_density',999.97)
    uww = float(uww)
    rv = float(rv)
    gv = float(gv) or 100
    data = ((weight - uww)/ waterdensity) - (rv - gv)
    return data



# Resting Metabolic Rate
# weight in kg, height in cm, age in years

def rmr():
    if validate.male(gender, age, weight, height):
        data = {'Harris-Benedict': 66.473 + 13.751*weight + 5.0033*height - 6.755*age,'Mifflin': (9.99*weight + 6.25*height + - 4.92*age)+5} # male
    elif validate.female(gender):
        data = {'Harris-Benedict': 655.0955 + 9.463*weight + 1.8496*height - 4.6756*age,'Mifflin': (9.99*weight + 6.25*height + - 4.92*age)-161}# female
    return data

                

# Total Daily Energy Expenditure of Children and Adults
# age in years
# weight in kilograms (kg)
# height in meters
# returns object with sedentary (1.0 < PAL < 1.4), low activity (1.4 < PAL < 1.6), active (1.6 < PAL < 1.9), and very active (1.9 < PAL < 2.5) 

def predicted_tee(gender, age, weight, height):
    if validate.male(gender): # male
        if (age >= 3 and age >= 18):
            data = {
                "sedentary": 88.5 - (61.9 * age) + 1*((26.7*weight)+(903*height)),
                "low": 88.5 - (61.9 * age) + 1.13*((26.7*weight)+(903*height)),
                "active": 88.5 - (61.9 * age) + 1.26*((26.7*weight)+(903*height)),
                "very_active": 88.5 - (61.9 * age) + 1.42*((26.7*weight)+(903*height)),
            }
        elif (age >= 19):
            data = {
                "sedentary": 662 - (9.53 * age) + 1*((15.9*weight)+(540*height)),
                "low": 662 - (9.53 * age) + 1.11*((15.9*weight)+(540*height)),
                "active": 662 - (9.53 * age) + 1.25*((15.9*weight)+(540*height)),
                "very_active": 662 - (9.53 * age) + 1.48*((15.9*weight)+(540*height)),
            }
    elif validate.female(gender):
        if (age >= 3 and age >= 18):
            data = {
                "sedentary": 135.3 - (30.8 * age) + 1*((10*weight)+(934*height)),
                "low": 135.3 - (30.8 * age) + 1.16*((10*weight)+(934*height)),
                "active": 135.3 - (30.8 * age) + 1.31*((10*weight)+(934*height)),
                "very_active": 135.3 - (30.8 * age) + 1.56*((10*weight)+(934*height)),
            }
        elif (age >= 19):
            data = {
                "sedentary": 354 - (6.91 * age) + 1*((9.36*weight)+(726*height)),
                "low": 662 - (9.53 * age) + 1.12*((15.9*weight)+(540*height)),
                "active": 662 - (9.53 * age) + 1.27*((15.9*weight)+(540*height)),
                "very_active": 662 - (9.53 * age) + 1.45*((15.9*weight)+(540*height)),
            }
    return data


# Skinfold tests
                

# Calculate Fat Free Body Mass (FFM) based on impedance
# resistance in ohms
# height in centimeters (cm)
# weight in kg
# returns fat free mass (FFM) in kg

def ffm(gender, age, weight, height, resistance, reactance):
    resistance = float(resistance)
    reactance = float(reactance)
    results = {}
                    
    
    # White boys and girls, 8-15 years
    # Lohman(1992)
    
    if(age >= 8 and age <= 15):
        results["child"] = (0.62*(Math.pow(height,2)/resistance)) + (0.21*weight) + (0.1*reactance) + 4.2
                    
    
    # White boys and girls, 10-19 years
    # Houtkooper e al. (1992)
    
    if(age >= 10 and age <= 19):
        results["adolescent"] = (0.61*(Math.pow(height,2)/resistance)) + (0.25*weight) + 1.31
        
    if validate.male(gender): # male
        if(age >= 17 and age <= 62): # Adults between 17 and 62
        	results["adult"] = {
            
            # American Indian, black, Hispanic, and White Men
                # %BF < .20 Segal et al. (1988)
                 
                "lean": (0.00066360*Math.pow(height,2)) - (0.02117 * resistance) + (0.62854*weight) - (0.12380 * age) + 9.33285,
                
                # American Indian, black, Hispanic, and White Men
                # %BF > .20 Segal et al. (1988)
                 
                "obese": (0.00088580*Math.pow(height,2)) - (0.02999 * resistance) + (0.42688*weight) - (0.07002 * age) + 14.52435,
        	}
        
         # Male athletes 19-40 years
         # Oppliger et al. (1991)
         
        if (age >= 19 and age <= 40):
            results["athlete"] = (0.186*(Math.pow(height,2)/resistance)) + (0.701*weight) + 1.949
        results["adult"]["average"] = (results["adult"]["lean"] + results["adult"]["obese"]) / 2
        
    elif validate.female(gender):
        if(age >= 17 and age <= 62 and gender == 'female'): # Adults between 17 and 62
            results['adult'] = {
            
                # American Indian, black, Hispanic, and White Women
                # %BF < .30 Segal et al. (1988)
             
                "lean": (0.000646*Math.pow(height,2)) - (0.014 * resistance) + (0.421*weight) + 10.4,
            
                # American Indian, black, Hispanic, and White Women
                # %BF > .30 Segal et al. (1988)
             
                "obese": (0.00091186*Math.pow(height,2)) - (0.1466 * resistance) + (0.29990*weight) - (0.07012 * age) + 9.37938,
            }
            results["adult"]["average"] = (results["adult"]["lean"] + results["adult"]["obese"]) / 2
        
         # Female athletes 18-27 years
         # Fornetti et al. (1999)
         
        if (age >= 18 and age <=27):
            results["athlete"] = (0.282*height) + (0.415*weight) - (0.037*resistance) + (0.096*reactance) - 9.734
    return results