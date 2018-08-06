cdef struct MET:
    double value
    char *code
    char *description

cdef class METs(object):
    cdef readonly MET mets[831]

cpdef double karvonen(double mets, double intensity)

cpdef double from_vo2(double vo2)

cpdef double stairmaster_mets(int setting)

cpdef double to_kcal(double mets, double weight)

cpdef double target(double vo2max, double intensity)
