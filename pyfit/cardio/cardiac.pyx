from libc.math cimport pow

cdef class HREstimator(object):
    def __cinit__(self):
        pass

    cdef float predict(self, float age):
        raise NotImplementedError("The prediction method is not implemented")

cdef class Astrand(HREstimator):
    """
    Astrand (1952)
    @description For use on men and women ages 4 to 34 yr
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """

    cpdef float predict(self, float age):
        return 216.6-(0.84*age)

    cpdef float age(self, float hr):
        return (hr-216.6)/-0.84

cdef class HF(HREstimator):
    """
    Fox(1971)
    @description Recommended for use with older adults
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """

    cpdef float predict(self, float age):
        return 220 - age

    cpdef float age(self, float hr):
        return 220 - hr

cdef class Gellish(HREstimator):
    """
    Gellish (2007)
    @description For use on men and women participants in an adult fitness program with broad range of age and fitness levels
    @see http://www.myfitnesspal.com/blog/mmmaddox/view/american-college-of-sports-medicine-american-heart-association-training-recommendations-254928
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """

    cpdef float predict(self, float age):
        return 207-(0.7 * age)

    cpdef float age(self, float hr):
        return (hr-207.0)/-0.7

cdef class Gulati(HREstimator):
    """
    Gulati (2010)
    @description For use on asymptomatic middle aged women referred for stress testing
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """

    cpdef float predict(self, float age):
        return 206-(0.88*age)

    cpdef float age(self, float hr):
        return (hr-206.0)/-0.88

cdef class LM(HREstimator):

    cpdef float predict(self, float age):
        return 206.3-(0.711 * age)

    cpdef float age(self, float hr):
        return (hr-206.3)/-0.711

cdef class Miller(HREstimator):

    cpdef float predict(self, float age):
        return 217-(0.85 * age)

    cpdef float age(self, float hr):
        return (hr-217)/-0.85

cdef class Nes(HREstimator):

    cpdef float predict(self, float age):
        return 211 - (0.64 * age)

    cpdef float age(self, float hr):
        return (hr-211)/-0.64

cdef class OaklandL(HREstimator):

    cpdef float predict(self, float age):
        return 206.9 - (0.67 * age)

    cpdef float age(self, float hr):
        return (hr-206.9)/-0.67

cdef class OaklandNL1(HREstimator):

    cpdef float predict(self, float age):
        return 191.5 - (0.002 * pow(age,2) )

    cpdef float age(self, float hr):
        return 5*sqrt(3830-20*hr)

cdef class OaklandNL2(HREstimator):

    cpdef float predict(self, float age):
        return 163 + (1.16 * age) - (0.018 * pow(age, 2))

    cpdef float age(self, float hr):
        return (-10./9)*(sqrt(8176-45*hr)-29)

cdef class RL(HREstimator):

    cpdef float predict(self, float age):
        return 205.8 - (0.685 * age)

    cpdef float age(self, float hr):
        return (hr-205.8)/-0.685

cdef class TMS(HREstimator):
    """
    Tanaka (2001)
    @description For use on healthy men and women
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """

    cpdef float predict(self, float age):
        return 208-(0.7*age)

    cpdef float age(self, float hr):
        return (hr-208)/-0.7

cpdef float mean_arterial_pressure(int diastolic_bp, int systolic_bp):
    return ((2 * diastolic_bp) + systolic_bp) / 3

cpdef float karvonen(float intensity, int rest, int maximum):
    return intensity * (maximum - rest) + rest

cpdef float zoladz(float hrMax, float adjuster):
      return hrMax - adjuster