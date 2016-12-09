from libc.math cimport pow, exp, log10, sqrt
from libcpp cimport bool

from enums import Gender

cdef class Compare(object):

    def __cinit__(self, int gender, double weight):
        self.gender = gender
        self.weight = weight

    cpdef double ocarroll(self, double weight_lifted):
        return weight_lifted/pow(self.weight-35, 1/3)

    cpdef double siff_weight(self):
        cdef double a = 512.245
        cdef double b = 146230
        cdef double c = 1.605
        if self.gender == Gender.Female:
            a = 943.063
            b = 0.05142
            c = 257.314
            return c-a*exp(-b*self.weight)
        return a-b*pow(self.weight, -c)

    cpdef double siff_power(self):
        cdef double a = 512.245
        cdef double b = 172970
        cdef double c = 1.3925
        if self.gender == Gender.Female:
            return 0
        return a-b*pow(self.weight, -c)

    cpdef double siff(self, bint power=False):
        if power:
            return self.siff_power()
        return self.siff_weight()

    cpdef double sinclair(self, double obtained_total):
        cdef double coefficient_a = 0.794358141
        cdef double coefficient_b = 174.393
        if self.gender == Gender.Female:
            coefficient_a = 0.897260740
            coefficient_b = 148.026
        if self.weight > coefficient_b:
             return 1
        cdef double exponent = pow( coefficient_a * log10(self.weight/coefficient_b), 2 )
        cdef double multiplier = pow(10, exponent)
        return multiplier * obtained_total

    cpdef double wilks(self, double weight_lifted):
        cdef double a = -216.0475144
        cdef double b = 16.2606339
        cdef double c = -0.002388645
        cdef double d = -0.00113732
        cdef double e = 7.01863E-06
        cdef double f = -1.291E-08

        if self.gender == Gender.Female:
            a = 594.31747775582
            b = -27.23842536447
            c = 0.82112226871
            d = -0.00930733913
            e = 4.731582E-05
            f = -9.054E-08
        cdef double coefficient = 500/(a + b*self.weight + c * pow(self.weight, 2) + d * pow(self.weight, 3) + e * pow(self.weight, 4) + f * pow(self.weight, 5) )
        return coefficient * weight_lifted

cdef class Jump(object):

    def __cinit__(self, double weight, double height):
        self.weight = weight
        self.height = height

    cpdef double bosco(self, double duration, double jump_count, double total_flight_time):
        return (total_flight_time * duration * pow(9.81,2)) / (4 * jump_count * (duration - total_flight_time) )

    cpdef double lewis(self, double jump_reach_score):
        return sqrt(4.9 * self.weight) * sqrt(jump_reach_score) * 9.81

    cpdef double harman(self, double v_jump_height, bint peak=False):
        cdef double v_jump_height_cm = v_jump_height * 100
        if peak:
            return 61.9*v_jump_height_cm + 36*self.weight + 1822
        return 21.1 *v_jump_height_cm + 2.3*self.weight + 1393

    cpdef double jb(self, double v_jump_height, bint peak=False):
        cdef double body_height_cm = self.height * 100
        cdef double v_jump_height_cm = v_jump_height * 100
        if peak:
            return 78.6*v_jump_height_cm +60.3*self.weight + 15.3*body_height_cm + 1308
        return 43.8*v_jump_height_cm + 32.7*self.weight - 16.8*body_height_cm + 431

    cpdef double sayer(self, double v_jump_height):
        cdef double v_jump_height_cm = v_jump_height * 100
        return 60.7*v_jump_height_cm + 45.3*self.weight - 2055

    cpdef double mk(self, double v_jump_height, double time):
        return (self.weight * (v_jump_height/time)) * 9.81

cdef class RMEstimator:

    def __cinit__(self, int reps):
        self.reps = reps

    cdef double predict(self, double weight):
        raise NotImplementedError("The prediction method is not implemented")

cdef class Abadie(RMEstimator):

    cpdef double predict(self, double weight):
        return 7.24 + (1.05* weight)

    cpdef double weight(self, double rm):
        return (4./105)*(25*rm-181)

cdef class Baechle(RMEstimator):

    cpdef double predict(self, double weight):
        return weight * (1+(0.033* self.reps) )

    cpdef double weight(self, double rm):
        return (1000*rm)/(33*self.reps + 1000)

cdef class Brzycki(RMEstimator):

    cpdef double predict(self, double weight):
        return weight/(1.0278-(0.0278 * self.reps))

    cpdef double weight(self, double rm):
        return (1.0278-(0.0278 * self.reps))

    cpdef double twoSet(self, double weight, int rep2, double weight2):
        return ((weight - weight2)/(rep2 - self.reps)) * (self.reps - 1) + weight

cdef class Epley(RMEstimator):

    cpdef double predict(self, double weight):
        return (weight * self.reps * 0.033)+weight

cdef class Landers(RMEstimator):

    cpdef double predict(self, double weight):
        return weight/(1.013 - (0.0267123 * self.reps) )

    cpdef double weight(self, double rm):
        return rm*(1.013 - (0.0267123 * self.reps) )

    cpdef double percent(self):
        cdef double value = 101.3 - (2.67123 * self.reps )
        return value / 100

cdef class Lombardi(RMEstimator):

    cpdef double predict(self, double weight):
        return weight*pow(self.reps,0.10)

    cpdef double weight(self, double rm):
        return rm/pow(self.reps,0.10)

cdef class Mayhew(RMEstimator):

    cpdef double football(self):
        return 226.7 + 7.1*(self.reps)

    cpdef double predict(self, double weight):
        return (100*weight)/( 52.2 + 41.9 * exp(-0.055 * self.reps) )

    cpdef double percent(self):
        cdef double value = 52.2 + 41.9* exp(-0.055* self.reps)
        return value / 100

    cpdef double weight(self, double rm):
        return (rm*( 52.2 + 41.9 * exp(-0.055 * self.reps) ) )/100

cdef class McGlothin(RMEstimator):

    cpdef double predict(self, double weight):
        return (100 * weight)/(101.3 - 2.67123 * self.reps)

    cpdef double weight(self, double rm):
        return (rm*(101.3 - 2.67123 * self.reps) )/100

cdef class  OConnor(RMEstimator):

    cpdef double predict(self, double weight):
        return weight * (1+0.025*self.reps)

    cpdef double percent(self, double weight):
        return (0.025 * (weight * self.reps)+ weight)

    cpdef double weight(self, double rm):
        return (40.*rm)/(self.reps+40)

cdef class ReynoldsCP(RMEstimator):

    cpdef double predict(self, double weight):
        return (1.1307 * weight) + 0.6998

cdef class ReynoldsLP(RMEstimator):

    cpdef double predict(self, double weight):
        return (1.09703 * weight) + 14.2546

cdef class Wathan(RMEstimator):

    cpdef double predict(self, double weight):
        return (100*weight) / (48.8+(53.8*exp(-0.075 * self.reps) ) )

    cpdef double weight(self, double rm):
        return (rm*(48.8+(53.8*exp(-0.075 * self.reps) ) ) )/100

cdef class RM(object):

    def __cinit__(self, int gender, double age):
        self.gender = gender
        self.age = age

    cpdef double ymca_upper_body(self, int reps):
        if self.gender == Gender.Female:
            return (0.31 * reps) + 19.2
        return (1.55 * reps) + 37.9

    cpdef double female_middle_age(self, int reps, double weight):
        return  (1.06 * weight) + (0.58 * reps) - (0.20 * self.age) - 3.41

    cpdef double female_older(self, int reps, double weight):
        return (0.92 * weight) + (0.79 * reps) - (0.20 * self.age) - 3.73

cpdef double relative(double weight, double rm):
        return rm / weight
