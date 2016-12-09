cpdef double daily_water_need(double weight)

cdef class Index:
    cdef readonly double weight
    cdef readonly double height

    cpdef double bai(self, double hip_circumference)

    cpdef double bmi(self)

    cpdef double bmi_prime(self, double upper_limit=*)

    cpdef double bsi(self, double waist_circumference)

    cpdef double corpulence(self)

    cpdef double sbsi(self, double bsa, double vertical_trunk_circumference, double waist_circumference)

    cpdef double whr(self, double waist_circumference, double hip_circumference)

    cpdef double whtr(self, double waist_circumference)

cdef class Mass:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double ffm_child(self, double resistance, double reactance)

    cpdef double ffm_adolescent(self, double resistance, double reactance)

    cpdef double ffm_adult_lean(self, double resistance, double reactance)

    cpdef double ffm_adult_obese(self, double resistance, double reactance)

    cpdef double ffm_adult_athlete(self, double resistance, double reactance)

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

    cpdef double gehan_george(self)

    cpdef double haycock(self)

    cpdef double mosteller(self)

    cpdef double schlich(self)

    cpdef double shuter_aslani(self)

    cpdef double takahira(self)

cdef class Stature(object):
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double height

    cpdef double universal(self)

    cpdef double american_white(self, double femur_length)

    cpdef double american_black(self, double femur_length)

    cpdef double stride_length(self)
