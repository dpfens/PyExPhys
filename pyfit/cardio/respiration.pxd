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

    cpdef double walking_gross(self, double speed, double grade)

    cpdef double running_gross(self, double speed, double grade)

    cpdef double leg_ergometry_gross(self, double mass, double work)

    cpdef double arm_ergometry_gross(self, double mass, double work)

    cpdef double stepping_gross(self, double height, double frequency)

    cpdef double usop(self, double hrMax, double restingHR)

    cpdef double fox_ergometry(self, double hr5)

    cpdef double ebbeling_treadmill(self, double speed, double hr)

    cpdef double kline(self, double time, double hrPeak)

    cpdef double larsen(self, double time, double hr)

    cpdef double astrand_step(self, double hr)

    cpdef double qc_step(self, double hr)

    cpdef double george_rw(self, double time)

    cpdef double george_steady(self, double time, double hr)

    cpdef double george_treadmill(self, double speed, double hr)

    cpdef double treadmill_submax_single_stage(self, double sm1, double hr1, double hrmax)

    cpdef double treadmill_submax_vo2_multistage(self, double sm1, double hr1, double sm2, double hr2, double hrmax)

    cpdef double cureton_child(self, double time)

    cpdef double balke(self, double time)

    cpdef double balke_15min_run(self, double distance)

    cpdef double bruce_male(self, double time, double time2, double time3)

    cpdef double bruce_female(self, double time)

    cpdef double bruce_ec(self, double time)

    cpdef double leger(self, double speed)

    cpdef double gilbert_daniels(self, double velocity, double time)
