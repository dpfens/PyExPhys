cdef double percent_vo2(double hr_percentage)

cdef double percent_hrmax(double vo2max_percentage)

cdef double vvo2max(double vo2max)

cpdef double velocity(double vo2)

cpdef double vo2(double velocity)

cpdef double vo2_percentage(double time)

cpdef double hr_speed(double percent_hr, double vo2max)

cpdef double hr_pace(double percent_hr, double vo2max)

cdef class Pace:
    cdef readonly double vo2max

    cpdef double percent(self, double percentage)

    cpdef double[:] easy(self)

    cpdef double[:] marathon(self)

    cpdef double[:] threshold(self)

    cpdef double[:] interval(self)
