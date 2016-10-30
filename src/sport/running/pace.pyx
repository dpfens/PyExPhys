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

cpdef float hrSpeed(float percentHR, float vO2Max):
    cdef float vO2MaxPercent = percentVO2(percentHR)
    cdef float vO2Speed = vVO2Max(vO2Max)
    return vO2MaxPercent * vO2Speed

cpdef float hrPace(float percentHR, vO2Max):
    cdef float kph =  hrSpeed(percentHR, vO2Max)
    return kph / 60

cpdef float elPace(float vO2Max):
    return hrPace(0.7, vO2Max)

cpdef float mPace(float vO2Max):
    return hrPace(0.825, vO2Max)

cpdef float tPace(float vO2Max):
    return hrPace(0.85, vO2Max)

cpdef float iPace(float vO2Max):
    return hrPace(1, vO2Max)
