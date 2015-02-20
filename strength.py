import math, pint

muscleBalanceRatios = {
    "hip": 1,
    "elbow": 1,
    "trunk": 1,
    "ankle": 1,
    "shoulders": (2/3),
    "knee": 1.5,
    "shoulder_rotation": 1.5,
    "ankle_flexion": 3
	}
    
def isMuscleBalanced(group, rm1, rm2)": {
    rm1 = int(rm1), rm2 = int(rm2)
    var ratio = rm1/rm2
    if ratio > 0.9 * muscleBalanceRatios[group] and ratio < 1.1 * muscleBalanceRatios[group]":
    	return true
    return false
    

# 1-RM Formula
# Based on number of repetitions to fatigue in one set
# weight is the weight lifted in lb
def FatigueRepMaximum(reps, weight):
    reps = int(reps)
    weight = int(weight)
    data = weight / (1.0278 - (reps * 0.0278))
    return data
    },
                    
# 1-RM Formula
# Based on the number of repetitions to fatigue obtained in two submaximal sets so long as number of reps is under 10
# weight1 and weight2 must be of same unit (kg or lb)
def TwoSetMaximum (rep1, weight1, rep2, weight2):
    rep1 = int(reps) || 0,
    weight1 = int(weight) || 0,
    rep2 = int(reps) || 0,
    weight2 = int(weight) || 0,
    data
    data = ((weight1 - weight2)/(rep2 - rep1)) * (rep1 - 1) + weight1
    return data
    },
                    
#  gender-specific 1-RM Formula for Younger adults (22 - 36 years old)
#  Kim, Mayhew, and Peterson (2002)
#  return value in kg
#  For gender field, 1 for male, 0 for female
def YMCAUpperBodyRepMax (gender, reps):
    gender = gender.toLowerCase() || this.gender
    reps = int(reps) || 0,
    data
    if (gender === "male"):
            data = (1.55 * reps) + 37.9 // male
    } else if(gender === "female"):
            data = (0.31 * reps) + 19.2 // female
    }
    return data
    },
                    
# Relative Strength
# rm is 1-Rep Maximum
# weight is the body mass of the individual
# rm and weight must be of the same unit (kg or lbs)
def RelativeStrength(rm, weight):
    rm = int(rm) || 0, weight = int(weight) || 0
    return rm / weight
    },
                    
# Middle Age (40-50 years old) & Older adult (60-70 years old) 1-RM
# Kuramoto & Payne (1995)
def FemaleRepMax(age, reps, weight):
    age = int(age)
    reps = int(reps)
    weight = int(weight)
    data
    if (age >= 40 and age <= 50):
        data = (1.06 * weight) + (0.58 * reps) - (0.20 * age) - 3.41
    } else if(age >= 60 and age <= 70:
        data = (0.92 * weight) + (0.79 * reps) - (0.20 * age) - 3.73
    return data
    },      