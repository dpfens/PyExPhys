cdef class BMREstimator:
    cdef readonly int gender
    cdef double predict(BMREstimator self, double age, double weight, double height)

cdef class HB(BMREstimator):

    cpdef double predict(HB self, double age, double weight, double height)

cdef class RevisedHB(BMREstimator):

    cpdef double predict(RevisedHB self, double age, double weight, double height)

cdef class MSJ(BMREstimator):

    cpdef double predict(MSJ self, double age, double weight, double height)

cdef class RMR:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double quick(RMR self)

    cpdef double bsa(RMR self, double bsa)

cpdef double kma(double lbm)


cpdef double cunningham(double lbm)

cdef class TEEEstimator:
    cdef readonly int gender
    cdef readonly int pal

    cdef double predict(TEEEstimator self, double age, double weight, double height)

    cpdef double fromActivity(TEEEstimator self, double weight, double mets)

cdef class ChildTEE(TEEEstimator):

    cpdef double predict(ChildTEE self, double age, double weight, double height)

cdef class AdultTEE(TEEEstimator):

    cpdef double predict(AdultTEE self, double age, double weight, double height)

cdef class Terrain:
    cdef readonly double weight
    cdef readonly double speed
    cdef readonly double load

    cpdef double pandolf(Terrain self, double terrain, double slope)

    cpdef double santee(Terrain self, double terrain, double slope)
