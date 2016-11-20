cdef struct MET:
    double value
    char *code
    char *description

cdef class METs(object):
    cdef readonly MET mets[831]

cpdef double karvonen(double mets, double intensity)

cpdef double fromVO2(double vO2)

cpdef double stairmasterMets(self, int setting)

cpdef double toKCal(double mets, double weight)

cpdef double target(double vO2Max, intensity)
