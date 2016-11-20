cdef class Compare:
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight

    cpdef double oCarroll(self, double weightLifted)

    cpdef double siffWeight(self)

    cpdef double siffPower(self)

    cpdef double siff(self, bint power=*)

    cpdef double sinclair(self, double obtainedTotal)

    cpdef double wilks(self, double weightLifted)

cdef class Jump:
    cdef readonly double weight
    cdef readonly double height

    cpdef double bosco(self, double duration, double jump_count, double total_flight_time)

    cpdef double lewis(self, double vJumpHeight)

    cpdef double harman(self, double vJumpHeight, bint peak=*)

    cpdef double jb(self, double vJumpHeight, bint peak=*)

    cpdef double sayer(self, double vJumpHeight)

    cpdef double mk(self, double vJumpHeight, double time)

cdef class RMEstimator:
    cdef readonly int reps

    cdef double predict(self, double weight)

cdef class Abadie(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double weight(self, double rm)

cdef class Baechle(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double weight(self, double rm)

cdef class Brzycki(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double weight(self, double rm)

    cpdef double twoSet(self, double weight, int rep2, double weight2)

cdef class Epley(RMEstimator):

    cpdef double predict(self, double weight)

cdef class Landers(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double weight(self, double rm)

    cpdef double percent(self)

cdef class Lombardi(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double weight(self, double rm)

cdef class Mayhew(RMEstimator):

    cpdef double football(self)

    cpdef double predict(self, double weight)

    cpdef double percent(self)

    cpdef double weight(self, double rm)

cdef class McGlothin(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double weight(self, double rm)

cdef class  OConnor(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double percent(self, double weight)

    cpdef double weight(self, double rm)

cdef class ReynoldsCP(RMEstimator):

    cpdef double predict(self, double weight)

cdef class ReynoldsLP(RMEstimator):

    cpdef double predict(self, double weight)

cdef class Wathan(RMEstimator):

    cpdef double predict(self, double weight)

    cpdef double weight(self, double rm)

cdef class RM(object):
    cdef readonly int gender
    cdef readonly double age

    cpdef double ymcaUpperBody(self, int reps)

    cpdef double femaleMiddleAge(self, int reps, double weight)

    cpdef double femaleOlder(self, int reps, double weight)

cpdef double relative(double weight, double rm)
