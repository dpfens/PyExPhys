from libc.math cimport exp, pow
from cpython cimport array
import array

cdef double percentVO2(double hrPercentage):
    cdef double convertedPercentage = hrPercentage * 100
    cdef double formulaResult = (convertedPercentage - 37.182) / 0.6463
    return formulaResult / 100

cdef double percentHrMax(double vO2MaxPercentage):
    cdef double convertedPercentage = vO2MaxPercentage * 100
    cdef double formulaResult = (0.6463 * convertedPercentage) + 37.182
    return formulaResult / 100

cdef double vVO2Max(double vO2Max):
    return vO2Max/3.5

cpdef double velocity(double vO2):
    return 29.54 + 5.000663*vO2 - 0.007546 * pow(vO2, 2)

cpdef double vO2(double velocity):
    return -4.60 + 0.182258 * velocity + 0.000104 * pow(velocity, 2)

cpdef double vO2Percentage(double time):
    return 0.8 + pow(0.1894393, -0.012778*time)+ exp(-0.1932605*time)

cpdef double hrSpeed(double percentHR, double vO2Max):
    cdef double vO2MaxPercent = percentVO2(percentHR)
    cdef double vO2Speed = vVO2Max(vO2Max)
    return vO2MaxPercent * vO2Speed

cpdef double hrPace(double percentHR, double vO2Max):
    cdef double kph =  hrSpeed(percentHR, vO2Max)
    return 60 / kph

cdef class Pace(object):

    def __cinit__(self, double vO2Max):
        self.vO2Max = vO2Max

    cpdef double percent(self, double percentage):
        return hrPace(percentage, self.vO2Max)

    cpdef float[:] easy(self):
        cdef array.array paces = array.array('f', [hrPace(0.6, self.vO2Max), hrPace(0.79, self.vO2Max)])
        return paces

    cpdef float[:] marathon(self):
        cdef array.array paces = array.array('f', [hrPace(0.8, self.vO2Max), hrPace(0.85, self.vO2Max) ])
        return paces

    cpdef float[:] threshold(self):
        cdef array.array paces = array.array('f', [hrPace(0.82, self.vO2Max), hrPace(0.88, self.vO2Max)] )
        return paces

    cpdef float[:] interval(self):
        cdef array.array paces = array.array('f', [hrPace(0.97, self.vO2Max), hrPace(1, self.vO2Max)] )
        return paces
