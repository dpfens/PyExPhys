cpdef double daily_water_need(double weight)

cdef class Index:
    cdef readonly double weight
    cdef readonly double height

    cpdef double bai(Index self, double hip_circumference)

    cpdef double bmi(Index self)

    cpdef double bmi_prime(Index self, double upper_limit=*)

    cpdef double bsi(Index self, double waist_circumference)

    cpdef double corpulence(Index self)

    cpdef double sbsi(Index self, double bsa, double vertical_trunk_circumference, double waist_circumference)

    cpdef double whr(Index self, double waist_circumference, double hip_circumference)

    cpdef double whtr(Index self, double waist_circumference)

cdef class Mass:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double ffm_child(Mass self, double resistance, double reactance)

    cpdef double ffm_adolescent(Mass self, double resistance, double reactance)

    cpdef double ffm_adult_lean(Mass self, double resistance, double reactance)

    cpdef double ffm_adult_obese(Mass self, double resistance, double reactance)

    cpdef double ffm_adult_athlete(Mass self, double resistance, double reactance)

cdef class Density:
    pass

cdef class BodyFat:
    pass

cdef class SurfaceArea:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double boyd(SurfaceArea self)

    cpdef double costeff(SurfaceArea self)

    cpdef double dubois(SurfaceArea self)

    cpdef double fujimoto(SurfaceArea self)

    cpdef double gehan_george(SurfaceArea self)

    cpdef double haycock(SurfaceArea self)

    cpdef double mosteller(SurfaceArea self)

    cpdef double schlich(SurfaceArea self)

    cpdef double shuter_aslani(SurfaceArea self)

    cpdef double takahira(SurfaceArea self)

cdef class Stature(object):
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double height

    cpdef double universal(Stature self)

    cpdef double american_white(Stature self, double femur_length)

    cpdef double american_black(Stature self, double femur_length)

    cpdef double stride_length(Stature self)
