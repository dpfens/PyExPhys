cdef class ResidualVolume:
    cdef readonly int gender
    cdef readonly double height # meters
    cdef readonly double age # years
    cdef readonly double weight # kg

    cpdef double normal(self)

    cpdef double overweight(self)

    cpdef double berglund(self)

    cpdef double black(self)

    cpdef double boren(self)

    cpdef double goldman(self)

    cpdef double obrien(self, double bsa)

cdef class VO2:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double reserve(self, double vo2Max, double vo2Rest=*)

    cpdef double target(self, double vo2Max, double vo2Rest, double intensity)

    cpdef double cooper(self, double distance)

    cpdef double walkingGross(self, double speed, double grade)

    cpdef double runningGross(self, double speed, double grade)

    cpdef double legErgometryGross(self, double mass, double work)

    cpdef double armErgometryGross(self, double mass, double work)

    cpdef double steppingGross(self, double height, double frequency)

    cpdef double usop(self, double hrMax, double restingHR)

    cpdef double foxErgometry(self, double hr5)

    cpdef double ebbelingTreadmill(self, double speed, double hr)

    cpdef double kline(self, double time, double hrPeak)

    cpdef double larsen(self, double time, double hr)

    cpdef double astrandStep(self, double hr)

    cpdef double qcStep(self, double hr)

    cpdef double georgeRW(self, double time)

    cpdef double georgeSteady(self, double time, double hr)

    cpdef double georgeTreadmill(self, double speed, double hr)

    cpdef double treadmillSubmaxSingleStage(self, double sm1, double hr1, double hrmax)

    cpdef double treadmillSubmaxVO2Multistage(self, double sm1, double hr1, double sm2, double hr2, double hrMax)

    cpdef double curetonChild(self, double time)

    cpdef double balke(self, double time)

    cpdef double balke15MinRun(self, double distance)

    cpdef double bruceMale(self, double time, double time2, double time3)

    cpdef double bruceFemale(self, double time)

    cpdef double bruceEC(self, double time)

    cpdef double leger(self, double speed)

    cpdef double gilbertDaniels(self, double velocity, double time)
