from libc.math import pow, log10f, sqrt
from enums import Gender

cdef float dailyNeed(float weight):
    return 0.033 * weight

cdef class Index(object):
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, float weight, float height):
        self.weight = weight
        self.height = height
    
    cdef float bmi(self):
        return self.weight/(self.height * self.height)

    cdef float ponderal(self):
        return self.weight/pow(self.height, 3)

cdef class Mass(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, int gender, float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cdef float ffmChild(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        return (0.62*(pow(cm,2)/resistance)) + (0.21*self.weight) + (0.1*reactance) + 4.2

    cdef float ffmAdolescent(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        return (0.61*(pow(cm,2)/resistance)) + (0.25*self.weight) + 1.31
        
    cdef float ffmAdultLean(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.000646*pow(cm,2)) - (0.014 * resistance) + (0.421*self.weight) + 10.4
        return (0.00066360*pow(cm,2)) - (0.02117 * resistance) + (0.62854*self.weight) - (0.12380 * self.age) + 9.33285

    cdef float ffmAdultObese(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.00091186*pow(cm,2)) - (0.1466 * resistance) + (0.29990*self.weight) - (0.07012 * self.age) + 9.37938
        return (0.00088580*pow(cm,2)) - (0.02999 * resistance) + (0.42688*self.weight) - (0.07002 * self.age) + 14.52435

    cdef float ffmAdultAthlete(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.282*cm) + (0.415*self.weight) - (0.037*resistance) + (0.096*reactance) - 9.734
        return (0.186*(pow(cm,2)/resistance)) + (0.701*self.weight) + 1.949

cdef class Density(object):

    def __cinit__(self,int gender, float age):
        self.gender = gender
        self.age = age

cdef class BodyFat(object):

    def __cinit__(self, int gender, float age):
        self.gender = gender
        self.age = age

cdef class SurfaceArea(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, int gender, float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cdef boyd(self):
        cdef float cm = self.height * 100
        return 0.03330 * pow(self.weight,(0.7285-0.0188*log10f(self.weight)))*pow(self.height,0.3)

    cdef costeff(self):
        return (4*self.weight+7)/(90+self.weight)

    cdef dubois(self):
        cdef float cm = self.height * 100
        return 0.007184 * pow(self.weight,0.425) * pow(cm,0.725)
        
    cdef fujimoto(self):
        cdef float cm = self.height * 100
        return 0.008883 * pow(self.weight, 0.444) * pow(cm, 0.663) 

    cdef gehangeorge(self):
        cdef float cm = self.height * 100
        return 0.0235 * pow(self.weight, 0.51456) * pow(cm, 0.42246) 

    cdef haycock(self):
        cdef float cm = self.height * 100
        return 0.024265 * pow(self.weight, 0.5378) * pow(cm, 0.3964)

    cdef mosteller(self):
        return sqrt(self.weight*self.height)/6

    cdef schlich(self):
        cdef float cm = self.height * 100
        if self.gender == Gender.Female:
            return 0.000975482 * pow(self.weight, 0.46) * pow(cm, 1.08)
        return 0.000579479 * pow(self.weight, 0.38) * pow(cm, 1.24)

    cdef shuterAslani(self):
        cdef float cm = self.height * 100
        return 0.00949 * pow(self.weight, 0.441) * pow(cm, 0.655)
        
    cdef takahira(self):
        cdef float cm = self.height * 100
        return 0.007241 * pow(self.weight, 0.425) * pow(cm, 0.725)        

cdef class Stature(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float height

    def __cinit__(self, int gender, float age, float height):
        self.gender = gender
        self.age = age
        self.height = height

    cdef universal(self):
        return 1.009 * self.height - 0.426 * self.age + 12.1

    cdef americanWhite(self, float femurLength):
        if self.gender == Gender.Female:
            return 2.47 * femurLength + 54.10
        return 2.32 * femurLength + 65.53

    cdef americanBlack(self, float femurLength):
        if self.gender == Gender.Female:
            return 2.28 * femurLength + 59.76
        return 2.10 * femurLength + 72.22 

    cdef strideLength(self):
        cdef float heightCm = self.height * 100
        if self.gender == Gender.Female:
            return 0.413 * heightCm
        return 0.415 * heightCm
