cdef class ResidualVolume:
    cdef readonly int gender
    cdef readonly double height  # meters
    cdef readonly double age  # years
    cdef readonly double weight  # kg

    cpdef double normal(ResidualVolume self)

    cpdef double overweight(ResidualVolume self)

    cpdef double berglund(ResidualVolume self)

    cpdef double black(ResidualVolume self)

    cpdef double boren(ResidualVolume self)

    cpdef double goldman(ResidualVolume self)

    cpdef double obrien(ResidualVolume self, double bsa)

cdef class VO2:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    cpdef double reserve(VO2 self, double vo2Max, double vo2Rest=*)

    cpdef double target(VO2 self, double vo2Max, double vo2Rest, double intensity)

    cpdef double cooper(VO2 self, double distance)

    cpdef double walking_gross(VO2 self, double speed, double grade)

    cpdef double running_gross(VO2 self, double speed, double grade)

    cpdef double leg_ergometry_gross(VO2 self, double mass, double work)

    cpdef double arm_ergometry_gross(VO2 self, double mass, double work)

    cpdef double stepping_gross(VO2 self, double height, double frequency)

    cpdef double usop(VO2 self, double hrMax, double restingHR)

    cpdef double fox_ergometry(VO2 self, double hr5)

    cpdef double ebbeling_treadmill(VO2 self, double speed, double hr)

    cpdef double kline(VO2 self, double time, double hrPeak)

    cpdef double larsen(VO2 self, double time, double hr)

    cpdef double astrand_step(VO2 self, double hr)

    cpdef double qc_step(VO2 self, double hr)

    cpdef double george_rw(VO2 self, double time)

    cpdef double george_steady(VO2 self, double time, double hr)

    cpdef double george_treadmill(VO2 self, double speed, double hr)

    cpdef double treadmill_submax_single_stage(VO2 self, double sm1, double hr1, double hrmax)

    cpdef double treadmill_submax_vo2_multistage(VO2 self, double sm1, double hr1, double sm2, double hr2, double hrmax)

    cpdef double cureton_child(VO2 self, double time)

    cpdef double balke(VO2 self, double time)

    cpdef double balke_15min_run(VO2 self, double distance)

    cpdef double bruce_male(VO2 self, double time, double time2, double time3)

    cpdef double bruce_female(VO2 self, double time)

    cpdef double bruce_ec(VO2 self, double time)

    cpdef double leger(VO2 self, double speed)

    cpdef double gilbert_daniels(VO2 self, double velocity, double time)
