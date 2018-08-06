from libc.math cimport exp, pow
from cpython cimport array
import array

cdef double percent_vo2(double hr_percentage):
    cdef double converted_percentage = hr_percentage * 100
    cdef double formula_result = (converted_percentage - 37.182) / 0.6463
    return formula_result / 100

cdef double percent_hrmax(double vo2max_percentage):
    cdef double converted_percentage = vo2max_percentage * 100
    cdef double formula_result = (0.6463 * converted_percentage) + 37.182
    return formula_result / 100

cdef double vvo2max(double vo2max):
    return vo2max / 3.5

cpdef double velocity(double vo2):
    return 29.54 + 5.000663 * vo2 - 0.007546 * pow(vo2, 2)

cpdef double vo2(double velocity):
    return - 4.60 + 0.182258 * velocity + 0.000104 * pow(velocity, 2)

cpdef double vo2_percentage(double time):
    return 0.8 + pow(0.1894393, - 0.012778 * time) + exp(-0.1932605 * time)

cpdef double hr_speed(double percent_hr, double vo2max):
    cdef double vo2max_percent = percent_vo2(percent_hr)
    cdef double vo2_speed = vvo2max(vo2max)
    return vo2max_percent * vo2_speed

cpdef double hr_pace(double percent_hr, double vo2max):
    cdef double kph = hr_speed(percent_hr, vo2max)
    return 60 / kph

cdef class Pace(object):

    def __cinit__(Pace self, double vo2max):
        self.vo2max = vo2max

    cpdef double percent(Pace self, double percentage):
        return hr_pace(percentage, self.vo2max)

    cpdef double[:] easy(Pace self):
        cdef array.array paces = array.array('dd', [hr_pace(0.6, self.vo2max), hr_pace(0.79, self.vo2max)])
        return paces

    cpdef double[:] marathon(Pace self):
        cdef array.array paces = array.array('dd', [hr_pace(0.8, self.vo2max), hr_pace(0.85, self.vo2max)])
        return paces

    cpdef double[:] threshold(Pace self):
        cdef array.array paces = array.array('dd', [hr_pace(0.82, self.vo2max), hr_pace(0.88, self.vo2max)])
        return paces

    cpdef double[:] interval(Pace self):
        cdef array.array paces = array.array('dd', [hr_pace(0.97, self.vo2max), hr_pace(1, self.vo2max)])
        return paces
