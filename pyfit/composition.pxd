cpdef double dailyWaterNeed(double weight)

cdef class Index:
    cdef readonly double weight
    cdef readonly double height

    cpdef double bai(self, double hipCircumference)

    cpdef double bmi(self)

    cpdef double bmi_prime(self, double upper_limit=*)

    cpdef double bsi(self, double waist_circumference)

    cpdef double corpulence(self)

    cpdef double sbsi(self, double bsa, double vertical_trunk_circumference, double waist_circumference)

    cpdef double WHR(self, double waistCircumference, double hipCircumference)

    cpdef double WHtR(self, double waistCircumference)

cdef class Mass:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double ffmChild(self, double resistance, double reactance)

    cpdef double ffmAdolescent(self, double resistance, double reactance)

    cpdef double ffmAdultLean(self, double resistance, double reactance)

    cpdef double ffmAdultObese(self, double resistance, double reactance)

    cpdef double ffmAdultAthlete(self, double resistance, double reactance)

cdef class Density:
    pass

cdef class BodyFat:
    pass

cdef class SurfaceArea:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double boyd(self)

    cpdef double costeff(self)

    cpdef double dubois(self)

    cpdef double fujimoto(self)

    cpdef double gehangeorge(self)

    cpdef double haycock(self)

    cpdef double mosteller(self)

    cpdef double schlich(self)

    cpdef double shuterAslani(self)

    cpdef double takahira(self)

cdef class Stature(object):
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double height

    cpdef double universal(self)

    cpdef double americanWhite(self, double femurLength)

    cpdef double americanBlack(self, double femurLength)

    cpdef double strideLength(self)
