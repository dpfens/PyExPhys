from libc.math cimport exp, pow
from cpython cimport array
import array

cdef float percentVO2(float hrPercentage):
    cdef float convertedPercentage = hrPercentage * 100
    cdef float formulaResult = (convertedPercentage - 37.182) / 0.6463
    return formulaResult / 100

cdef float percentHrMax(float vO2MaxPercentage):
    cdef float convertedPercentage = vO2MaxPercentage * 100
    cdef float formulaResult = (0.6463 * convertedPercentage) + 37.182
    return formulaResult / 100

cdef float vVO2Max(float vO2Max):
    return vO2Max/3.5

cpdef float velocity(float vO2):
    return 29.54 + 5.000663*vO2 - 0.007546 * pow(vO2, 2)

cpdef float vO2(float velocity):
    return -4.60 + 0.182258 * velocity + 0.000104 * pow(velocity, 2)

cpdef float vO2Percentage(float time):
    return 0.8 + pow(0.1894393, -0.012778*time)+ exp(-0.1932605*time)

cpdef float hrSpeed(float percentHR, float vO2Max):
    cdef float vO2MaxPercent = percentVO2(percentHR)
    cdef float vO2Speed = vVO2Max(vO2Max)
    return vO2MaxPercent * vO2Speed

cpdef float hrPace(float percentHR, vO2Max):
    cdef float kph =  hrSpeed(percentHR, vO2Max)
    return 60 / kph

cdef class Pace(object):
    cdef readonly float vO2Max

    def __cinit__(self, float vO2Max):
        self.vO2Max = vO2Max

    cpdef float percent(self, float percentage):
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
