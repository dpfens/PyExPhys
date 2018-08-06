from libc.math cimport pow, log10, sqrt
from pyfit.enums cimport Gender
cimport cython

@cython.nonecheck(False)
cpdef double daily_water_need(double weight):
    return 0.033 * weight

cdef class Index(object):

    def __cinit__(Index self, double weight, double height):
        self.weight = weight
        self.height = height

    cpdef double bai(Index self, double hip_circumference):
        cdef double numerator = 100 * hip_circumference
        cdef double denominator = self.height * sqrt(self.height)
        return (numerator / denominator) - 18

    cpdef double bmi(Index self):
        return self.weight / (self.height * self.height)

    cpdef double bmi_prime(Index self, double upper_limit=25.9):
        return self.bmi() / upper_limit

    cpdef double bsi(Index self, double waist_circumference):
        return waist_circumference / pow(self.bmi(), 2 / 3) * pow(self.height, 0.5)

    cpdef double corpulence(Index self):
        return self.weight / pow(self.height, 3)

    cpdef double sbsi(Index self, double bsa, double vertical_trunk_circumference, double waist_circumference):
        return (pow(self.height, 7 / 4) * pow(waist_circumference, 5 / 6)) / (bsa * vertical_trunk_circumference)

    cpdef double whr(Index self, double waist_circumference, double hip_circumference):
        return waist_circumference / hip_circumference

    cpdef double whtr(Index self, double waist_circumference):
        return waist_circumference / self.height

cdef class Mass(object):

    def __cinit__(Mass self, int gender, double age, double weight, double height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cpdef double ffm_child(Mass self, double resistance, double reactance):
        cdef double cm = self.height * 100
        return (0.62 * (pow(cm, 2) / resistance)) + (0.21 * self.weight) + (0.1 * reactance) + 4.2

    cpdef double ffm_adolescent(Mass self, double resistance, double reactance):
        cdef double cm = self.height * 100
        return (0.61 * (pow(cm, 2) / resistance)) + (0.25 * self.weight) + 1.31

    cpdef double ffm_adult_lean(Mass self, double resistance, double reactance):
        cdef double cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.000646 * pow(cm, 2)) - (0.014 * resistance) + (0.421 * self.weight) + 10.4
        return (0.00066360 * pow(cm, 2)) - (0.02117 * resistance) + (0.62854 * self.weight) - (0.12380 * self.age) + 9.33285

    cpdef double ffm_adult_obese(Mass self, double resistance, double reactance):
        cdef double cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.00091186 * pow(cm, 2)) - (0.1466 * resistance) + (0.29990 * self.weight) - (0.07012 * self.age) + 9.37938
        return (0.00088580 * pow(cm, 2)) - (0.02999 * resistance) + (0.42688 * self.weight) - (0.07002 * self.age) + 14.52435

    cpdef double ffm_adult_athlete(Mass self, double resistance, double reactance):
        cdef double cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.282 * cm) + (0.415 * self.weight) - (0.037 * resistance) + (0.096 * reactance) - 9.734
        return (0.186 * (pow(cm, 2) / resistance)) + (0.701 * self.weight) + 1.949

cdef class Density(object):

    def __cinit__(Density self, int gender, double age):
        self.gender = gender
        self.age = age

cdef class BodyFat(object):

    def __cinit__(BodyFat self, int gender, double age):
        self.gender = gender
        self.age = age

cdef class SurfaceArea(object):

    def __cinit__(SurfaceArea self, int gender, double age, double weight, double height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cpdef double boyd(SurfaceArea self):
        cdef double cm = self.height * 100
        cdef double g = self.weight * 1000
        return 0.0003330 * pow(g, (0.7285 - (0.0188 * log10(g)))) * pow(cm, 0.3)

    cpdef double costeff(SurfaceArea self):
        return (4 * self.weight + 7) / (90 + self.weight)

    cpdef double dubois(SurfaceArea self):
        cdef double cm = self.height * 100
        return 0.007184 * pow(self.weight, 0.425) * pow(cm, 0.725)

    cpdef double fujimoto(SurfaceArea self):
        cdef double cm = self.height * 100
        return 0.008883 * pow(self.weight, 0.444) * pow(cm, 0.663)

    cpdef double gehan_george(SurfaceArea self):
        cdef double cm = self.height * 100
        return 0.0235 * pow(self.weight, 0.51456) * pow(cm, 0.42246)

    cpdef double haycock(SurfaceArea self):
        cdef double cm = self.height * 100
        return 0.024265 * pow(self.weight, 0.5378) * pow(cm, 0.3964)

    cpdef double mosteller(SurfaceArea self):
        return sqrt(self.weight * self.height) / 6

    cpdef double schlich(SurfaceArea self):
        cdef double cm = self.height * 100
        if self.gender == Gender.Female:
            return 0.000975482 * pow(self.weight, 0.46) * pow(cm, 1.08)
        return 0.000579479 * pow(self.weight, 0.38) * pow(cm, 1.24)

    cpdef double shuter_aslani(SurfaceArea self):
        cdef double cm = self.height * 100
        return 0.00949 * pow(self.weight, 0.441) * pow(cm, 0.655)

    cpdef double takahira(SurfaceArea self):
        cdef double cm = self.height * 100
        return 0.007241 * pow(self.weight, 0.425) * pow(cm, 0.725)

cdef class Stature(object):

    def __cinit__(Stature self, int gender, double age, double height):
        self.gender = gender
        self.age = age
        self.height = height

    cpdef double universal(Stature self):
        cdef double height_cm = self.height * 100
        cdef double stature = 1.009 * height_cm - 0.426 * self.age + 12.1
        return stature / 100

    cpdef double american_white(Stature self, double femur_length):
        cdef double femur_length_cm = femur_length * 100
        cdef double stature
        if self.gender == Gender.Female:
            stature = 2.47 * femur_length_cm + 54.10
        else:
            stature = 2.32 * femur_length_cm + 65.53
        return stature / 100

    cpdef double american_black(Stature self, double femur_length):
        cdef double femur_length_cm = femur_length * 100
        if self.gender == Gender.Female:
            stature = 2.28 * femur_length_cm + 59.76
        else:
            stature = 2.10 * femur_length_cm + 72.22
        return stature / 100

    cpdef double stride_length(Stature self):
        cdef double height_cm = self.height * 100
        cdef double length
        if self.gender == Gender.Female:
            length = 0.413 * height_cm
        else:
            length = 0.415 * height_cm
        return length / 100
