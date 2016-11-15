from libc.math cimport pow, exp, log10, sqrt
from libcpp cimport bool

from enums import Gender

cdef class Compare(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float weight

    def __cinit__(self, int gender, float weight):
        self.gender = gender
        self.weight = weight

    cpdef float oCarroll(self, float weightLifted):
        return weightLifted/pow(self.weight-35, 1/3)

    cpdef float siffWeight(self):
        cdef float a = 512.245
        cdef float b = 146230
        cdef float c = 1.605
        if self.gender == Gender.Female:
            a = 943.063
            b = 0.05142
            c = 257.314
            return c-a*exp(-b*self.weight)
        return a-b*pow(self.weight, -c)

    cpdef float siffPower(self):
        cdef float a = 512.245
        cdef float b = 172970
        cdef float c = 1.3925
        if self.gender == Gender.Female:
            return 0
        return a-b*pow(self.weight, -c)

    cpdef float siff(self, bint power=False):
        if power:
            return self.siffPower()
        return self.siffWeight()

    cpdef float sinclair(self, float obtainedTotal):
        cdef float coefficientA = 0.794358141
        cdef float coefficientB = 174.393
        if self.gender == Gender.Female:
            coefficientA = 0.897260740
            coefficientB = 148.026
        if self.weight > coefficientB:
             return 1
        cdef float exponent = pow( coefficientA * log10(self.weight/coefficientB), 2 )
        cdef float multiplier = pow(10, exponent)
        return multiplier * obtainedTotal

    cpdef float wilks(self, float weightLifted):
        cdef float a = -216.0475144
        cdef float b = 16.2606339
        cdef float c = -0.002388645
        cdef float d = -0.00113732
        cdef float e = 7.01863E-06
        cdef float f = -1.291E-08

        if self.gender == Gender.Female:
            a = 594.31747775582
            b = -27.23842536447
            c = 0.82112226871
            d = -0.00930733913
            e = 4.731582E-05
            f = -9.054E-08
        cdef float coefficient = 500/(a + b*self.weight + c * pow(self.weight, 2) + d * pow(self.weight, 3) + e * pow(self.weight, 4) + f * pow(self.weight, 5) )
        return coefficient * weightLifted

cdef class Jump(object):
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, float weight, float height):
        self.weight = weight
        self.height = height

    cpdef float bosco(self, float duration, float jump_count, float total_flight_time):
        return (total_flight_time * duration * pow(9.81,2)) / (4 * jump_count * (duration - total_flight_time) )

    cpdef float lewis(self, float vJumpHeight):
        return sqrt(4.9 * self.weight) * sqrt(vJumpHeight) * 9.81

    cpdef float harman(self, float vJumpHeight, peak=False):
        cdef float vJumpHeightCm = vJumpHeight * 100
        if peak:
            return 61.9*vJumpHeightCm + 36*self.weight + 1822
        return 21.1 *vJumpHeightCm + 2.3*self.weight + 1393

    cpdef float jb(self, float vJumpHeight, peak=False):
        cdef float bodyHeightCm = self.height * 100
        cdef float vJumpHeightCm = vJumpHeight * 100
        if peak:
            return 78.6*vJumpHeightCm +60.3*self.weight + 15.3*bodyHeightCm + 1308
        return 43.8*vJumpHeightCm + 32.7*self.weight - 16.8*bodyHeightCm + 431

    cpdef float sayer(self, float vJumpHeight):
        cdef float vJumpHeightCm = vJumpHeight * 100
        return 60.7*vJumpHeightCm + 45.3*self.weight - 2055

    cpdef float mk(self, float vJumpHeight, float time):
        return (self.weight * (vJumpHeight/time)) * 9.81

cdef class RMEstimator:
    cdef readonly int reps

    def __cinit__(self, int reps):
        self.reps = reps

    cdef float predict(self, float weight):
        raise NotImplementedError("The prediction method is not implemented")

cdef class Abadie(RMEstimator):

    cpdef float predict(self, float weight):
        return 7.24 + (1.05* weight)

    cpdef float weight(self, float rm):
        return (4./105)*(25*rm-181)

cdef class Baechle(RMEstimator):

    cpdef float predict(self, float weight):
        return weight * (1+(0.033* self.reps) )

    cpdef float weight(self, float rm):
        return (1000*rm)/(33*self.reps + 1000)

cdef class Brzycki(RMEstimator):

    cpdef float predict(self, float weight):
        return weight/(1.0278-(0.0278 * self.reps))

    cpdef float weight(self, float rm):
        return (1.0278-(0.0278 * self.reps))

    cpdef float twoSet(self, float weight, int rep2, float weight2):
        return ((weight - weight2)/(rep2 - self.reps)) * (self.reps - 1) + weight

cdef class Epley(RMEstimator):

    cpdef float predict(self, float weight):
        return (weight * self.reps * 0.033)+weight

cdef class Landers(RMEstimator):

    cpdef float predict(self, float weight):
        return weight/(1.013 - (0.0267123 * self.reps) )

    cpdef float weight(self, float rm):
        return rm*(1.013 - (0.0267123 * self.reps) )

    cpdef float percent(self):
        cdef float value = 101.3 - (2.67123 * self.reps )
        return value / 100

cdef class Lombardi(RMEstimator):

    cpdef float predict(self, float weight):
        return weight*pow(self.reps,0.10)

    cpdef float weight(self, float rm):
        return rm/pow(self.reps,0.10)

cdef class Mayhew(RMEstimator):

    cpdef float football(self):
        return 226.7 + 7.1*(self.reps)

    cpdef float predict(self, float weight):
        return (100*weight)/( 52.2 + 41.9 * exp(-0.055 * self.reps) )

    cpdef float percent(self):
        cdef float value = 52.2 + 41.9* exp(-0.055* self.reps)
        return value / 100

    cpdef float weight(self, float rm):
        return (rm*( 52.2 + 41.9 * exp(-0.055 * self.reps) ) )/100

cdef class McGlothin(RMEstimator):

    cpdef float predict(self, float weight):
        return (100 * weight)/(101.3 - 2.67123 * self.reps)

    cpdef float weight(self, float rm):
        return (rm*(101.3 - 2.67123 * self.reps) )/100

cdef class  OConnor(RMEstimator):

    cpdef float predict(self, float weight):
        return weight * (1+0.025*self.reps)

    cpdef float percent(self, float weight):
        return (0.025 * (weight * self.reps)+ weight)

    cpdef float weight(self, float rm):
        return (40.*rm)/(self.reps+40)

cdef class ReynoldsCP(RMEstimator):

    cpdef float predict(self, float weight):
        return (1.1307 * weight) + 0.6998

cdef class ReynoldsLP(RMEstimator):

    cpdef float predict(self, float weight):
        return (1.09703 * weight) + 14.2546

cdef class Wathan(RMEstimator):

    cpdef float predict(self, float weight):
        return (100*weight) / (48.8+(53.8*exp(-0.075 * self.reps) ) )

    cpdef float weight(self, float rm):
        return (rm*(48.8+(53.8*exp(-0.075 * self.reps) ) ) )/100

cdef class RM(object):
    cdef readonly int gender
    cdef readonly float age

    def __cinit__(self, int gender, float age):
        self.gender = gender
        self.age = age

    cpdef float ymcaUpperBody(self, int reps):
        if self.gender == Gender.Female:
            return (0.31 * reps) + 19.2
        return (1.55 * reps) + 37.9

    cpdef float femaleMiddleAge(self, int reps, float weight):
        return  (1.06 * weight) + (0.58 * reps) - (0.20 * self.age) - 3.41

    cpdef float femaleOlder(self, int reps, float weight):
        return (0.92 * weight) + (0.79 * reps) - (0.20 * self.age) - 3.73

cpdef float relative(float weight, float rm):
        return rm / weight
