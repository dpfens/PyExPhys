cdef class HREstimator:
    cdef double predict(self, double age)
    cdef double age(self, double hr)

cdef class Astrand(HREstimator):
    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class HF(HREstimator):
    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class Gellish(HREstimator):
    cpdef double predict(self, double age)
    cpdef double age(self, double hr)

cdef class Gulati(HREstimator):
    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class LM(HREstimator):

    cpdef double predict(self, double age)
    cpdef double age(self, double hr)

cdef class Miller(HREstimator):

    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class Nes(HREstimator):

    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class OaklandL(HREstimator):

    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class OaklandNL1(HREstimator):

    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class OaklandNL2(HREstimator):

    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class RL(HREstimator):

    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cdef class TMS(HREstimator):

    cpdef double predict(self, double age)

    cpdef double age(self, double hr)

cpdef double mean_arterial_pressure(int diastolic_bp, int systolic_bp)

cpdef double karvonen(double intensity, int rest, int maximum)

cpdef double zoladz(double hrMax, double adjuster)
