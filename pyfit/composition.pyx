from libc.math cimport pow, log10, sqrt
from pyfit.enums import Gender

cpdef float dailyWaterNeed(float weight):
    return 0.033 * weight

cdef class Index(object):
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, float weight, float height):
        self.weight = weight
        self.height = height

    cpdef float bai(self, float hipCircumference):
        cdef float  numerator = 100 * hipCircumference
        cdef float denominator = self.height * sqrt(self.height)
        return (numerator/denominator) - 18

    cpdef float bmi(self):
        return self.weight/(self.height * self.height)

    cpdef float bmi_prime(self, float upper_limit=25.9):
        return self.bmi()/upper_limit

    cpdef float bsi(self, float waist_circumference):
        return waist_circumference / pow(self.bmi(), 2/3) * pow(self.height, 0.5)

    cpdef float corpulence(self):
        return self.weight/pow(self.height, 3)

    cpdef float sbsi(self, float bsa, float vertical_trunk_circumference, float waist_circumference):
        return (pow(self.height, 7/4)* pow(waist_circumference, 5/6) )/(bsa * vertical_trunk_circumference)

    cpdef float WHR(self, float waistCircumference, float hipCircumference):
        return waistCircumference/hipCircumference

    cpdef float WHtR(self, float waistCircumference):
        return waistCircumference/self.height

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

    cpdef float ffmChild(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        return (0.62*(pow(cm,2)/resistance)) + (0.21*self.weight) + (0.1*reactance) + 4.2

    cpdef float ffmAdolescent(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        return (0.61*(pow(cm,2)/resistance)) + (0.25*self.weight) + 1.31

    cpdef float ffmAdultLean(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.000646*pow(cm,2)) - (0.014 * resistance) + (0.421*self.weight) + 10.4
        return (0.00066360*pow(cm,2)) - (0.02117 * resistance) + (0.62854*self.weight) - (0.12380 * self.age) + 9.33285

    cpdef float ffmAdultObese(self, float resistance, float reactance):
        cdef float cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.00091186*pow(cm,2)) - (0.1466 * resistance) + (0.29990*self.weight) - (0.07012 * self.age) + 9.37938
        return (0.00088580*pow(cm,2)) - (0.02999 * resistance) + (0.42688*self.weight) - (0.07002 * self.age) + 14.52435

    cpdef float ffmAdultAthlete(self, float resistance, float reactance):
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

    cpdef float boyd(self):
        cdef float cm = self.height * 100
        cdef float g = self.weight * 1000
        return 0.0003330 * pow(g,(0.7285-(0.0188*log10(g) ) ))*pow(cm,0.3)

    cpdef float costeff(self):
        return (4*self.weight+7)/(90+self.weight)

    cpdef float dubois(self):
        cdef float cm = self.height * 100
        return 0.007184 * pow(self.weight,0.425) * pow(cm,0.725)

    cpdef float fujimoto(self):
        cdef float cm = self.height * 100
        return 0.008883 * pow(self.weight, 0.444) * pow(cm, 0.663)

    cpdef float gehangeorge(self):
        cdef float cm = self.height * 100
        return 0.0235 * pow(self.weight, 0.51456) * pow(cm, 0.42246)

    cpdef float haycock(self):
        cdef float cm = self.height * 100
        return 0.024265 * pow(self.weight, 0.5378) * pow(cm, 0.3964)

    cpdef float mosteller(self):
        return sqrt(self.weight*self.height)/6

    cpdef float schlich(self):
        cdef float cm = self.height * 100
        if self.gender == Gender.Female:
            return 0.000975482 * pow(self.weight, 0.46) * pow(cm, 1.08)
        return 0.000579479 * pow(self.weight, 0.38) * pow(cm, 1.24)

    cpdef float shuterAslani(self):
        cdef float cm = self.height * 100
        return 0.00949 * pow(self.weight, 0.441) * pow(cm, 0.655)

    cpdef float takahira(self):
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

    cpdef float universal(self):
        cdef float heightCm = self.height * 100
        cdef float stature = 1.009 * heightCm - 0.426 * self.age + 12.1
        return stature / 100

    cpdef float americanWhite(self, float femurLength):
        cdef float femurLengthCm = femurLength * 100
        cdef float stature
        if self.gender == Gender.Female:
            stature = 2.47 * femurLengthCm + 54.10
        else:
            stature = 2.32 * femurLengthCm + 65.53
        return stature / 100

    cpdef float americanBlack(self, float femurLength):
        cdef float femurLengthCm = femurLength * 100
        if self.gender == Gender.Female:
            stature = 2.28 * femurLengthCm + 59.76
        stature = 2.10 * femurLengthCm + 72.22
        return stature / 100

    cpdef float strideLength(self):
        cdef float heightCm = self.height * 100
        cdef float strideLength
        if self.gender == Gender.Female:
            strideLength = 0.413 * heightCm
        strideLength = 0.415 * heightCm
        return strideLength / 100
