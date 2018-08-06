cdef class HREstimator:
    cdef double predict(self, double age)
    cdef double age(self, double hr)

cdef class Astrand(HREstimator):
    cpdef double predict(Astrand self, double age)

    cpdef double age(Astrand self, double hr)

cdef class HF(HREstimator):
    cpdef double predict(HF self, double age)

    cpdef double age(HF self, double hr)

cdef class Gellish(HREstimator):
    cpdef double predict(Gellish self, double age)
    cpdef double age(Gellish self, double hr)

cdef class Gulati(HREstimator):
    cpdef double predict(Gulati self, double age)

    cpdef double age(Gulati self, double hr)

cdef class LM(HREstimator):

    cpdef double predict(LM self, double age)
    cpdef double age(LM self, double hr)

cdef class Miller(HREstimator):

    cpdef double predict(Miller self, double age)

    cpdef double age(Miller self, double hr)

cdef class Nes(HREstimator):

    cpdef double predict(Nes self, double age)

    cpdef double age(Nes self, double hr)

cdef class OaklandL(HREstimator):

    cpdef double predict(OaklandL self, double age)

    cpdef double age(OaklandL self, double hr)

cdef class OaklandNL1(HREstimator):

    cpdef double predict(OaklandNL1 self, double age)

    cpdef double age(OaklandNL1 self, double hr)

cdef class OaklandNL2(HREstimator):

    cpdef double predict(OaklandNL2 self, double age)

    cpdef double age(OaklandNL2 self, double hr)

cdef class RL(HREstimator):

    cpdef double predict(RL self, double age)

    cpdef double age(RL self, double hr)

cdef class TMS(HREstimator):

    cpdef double predict(TMS self, double age)

    cpdef double age(TMS self, double hr)

cpdef double mean_arterial_pressure(int diastolic_bp, int systolic_bp)

cpdef double karvonen(double intensity, int rest, int maximum)

cpdef double zoladz(double hrMax, double adjuster)
