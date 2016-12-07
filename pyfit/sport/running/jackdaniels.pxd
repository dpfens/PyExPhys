cdef double percentVO2(double hrPercentage)

cdef double percentHrMax(double vO2MaxPercentage)

cdef double vVO2Max(double vO2Max)

cpdef double velocity(double vO2)

cpdef double vO2(double velocity)

cpdef double vO2Percentage(double time)

cpdef double hrSpeed(double percentHR, double vO2Max)

cpdef double hrPace(double percentHR, double vO2Max)

cdef class Pace:
    cdef readonly double vO2Max

    cpdef double percent(self, double percentage)

    cpdef float[:] easy(self)

    cpdef float[:] marathon(self)

    cpdef float[:] threshold(self)

    cpdef float[:] interval(self)
