cdef class Compare:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight

    cpdef double ocarroll(Compare self, double weight_lifted)

    cpdef double siff_weight(Compare self)

    cpdef double siff_power(Compare self)

    cpdef double siff(Compare self, bint power=*)

    cpdef double sinclair(Compare self, double obtained_total)

    cpdef double wilks(Compare self, double weight_lifted)

cdef class Jump:
    cdef readonly double weight
    cdef readonly double height

    cpdef double bosco(Jump self, double duration, double jump_count, double total_flight_time)

    cpdef double lewis(Jump self, double jump_reach_score)

    cpdef double harman(Jump self, double v_jump_height, bint peak=*)

    cpdef double jb(Jump self, double v_jump_height, bint peak=*)

    cpdef double sayer(self, double v_jump_height)

    cpdef double mk(Jump self, double v_jump_height, double time)

cdef class RMEstimator:
    cdef readonly int reps

    cdef double predict(RMEstimator self, double weight)

cdef class Abadie(RMEstimator):

    cpdef double predict(Abadie self, double weight)

    cpdef double weight(Abadie self, double rm)

cdef class Baechle(RMEstimator):

    cpdef double predict(Baechle self, double weight)

    cpdef double weight(Baechle self, double rm)

cdef class Brzycki(RMEstimator):

    cpdef double predict(Brzycki self, double weight)

    cpdef double weight(Brzycki self, double rm)

    cpdef double twoSet(Brzycki self, double weight, int rep2, double weight2)

cdef class Epley(RMEstimator):

    cpdef double predict(Epley self, double weight)

cdef class Landers(RMEstimator):

    cpdef double predict(Landers self, double weight)

    cpdef double weight(Landers self, double rm)

    cpdef double percent(Landers self)

cdef class Lombardi(RMEstimator):

    cpdef double predict(Lombardi self, double weight)

    cpdef double weight(Lombardi self, double rm)

cdef class Mayhew(RMEstimator):

    cpdef double football(Mayhew self)

    cpdef double predict(Mayhew self, double weight)

    cpdef double percent(Mayhew self)

    cpdef double weight(Mayhew self, double rm)

cdef class McGlothin(RMEstimator):

    cpdef double predict(McGlothin self, double weight)

    cpdef double weight(McGlothin self, double rm)

cdef class OConnor(RMEstimator):

    cpdef double predict(OConnor self, double weight)

    cpdef double percent(OConnor self, double weight)

    cpdef double weight(OConnor self, double rm)

cdef class ReynoldsCP(RMEstimator):

    cpdef double predict(ReynoldsCP self, double weight)

cdef class ReynoldsLP(RMEstimator):

    cpdef double predict(ReynoldsLP self, double weight)

cdef class Wathan(RMEstimator):

    cpdef double predict(Wathan self, double weight)

    cpdef double weight(Wathan self, double rm)

cdef class RM(object):
    cdef readonly int gender
    cdef readonly double age

    cpdef double ymca_upper_body(RM self, int reps)

    cpdef double female_middle_age(RM self, int reps, double weight)

    cpdef double female_older(RM self, int reps, double weight)

cpdef double relative(double weight, double rm)
