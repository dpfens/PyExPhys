from libc.math import pow, exp, log10f, sqrt
from enums import Gender


cdef class Lifting(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float weight

    def __cinit__(self, int gender, float age, float weight):
        self.gender = gender
        self.age = age
        self.weight = weight

    cdef oCarroll(self, float weightLifted):
        return weightLifted/pow(self.weight-35, 1/3)

    cdef siffWeight(self):
        cdef float a = 512.245
        cdef float b = 146230
        cdef float c = 1.605
        if self.gender == Gender.Female:
            a = 943.063
            b = 0.05142
            c = 257.314
            return c-a*exp(-b*self.weight)
        return a-b*pow(self.weight, -c)

    cdef siffPower(self):
        cdef float a = 512.245
        cdef float b = 172970
        cdef float c = 1.3925
        if self.gender == Gender.Female:
            return 0
        return a-b*pow(self.weight, -c)

    cpdef siff(self, power=False):
        if power:
            return self.siffPower()
        return self.siffWeight()

    cdef sinclair(self, float obtainedTotal):
        cdef float coefficientA = 0.794358141
        cdef float coefficientB = 174.393
        if self.gender == Gender.Female:
            coefficientA = 0.897260740
            coefficientB = 148.026
        if self.weight >= coefficientB:
             return 1
        cdef float exponent = pow(  coefficientA * log10f(self.weight/coefficientB), 2 )
        return pow(10, exponent)

    cdef wilks(self, float weightLifted):
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

cdef class Power(object):
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, float weight, float height):
        self.weight = weight
        self.height = height

    cdef lewis(self, float jumpHeight):
        return sqrt(4.9 * self.weight) * sqrt(jumpHeight) * 9.81

    cdef harman(self, float jumpHeight, peak=False):
        cdef float jumpHeightCm = jumpHeight * 100
        if peak:
            return 61.9*jumpHeightCm + 36*self.weight + 1822
        return 21.1 *jumpHeightCm + 2.3*self.weight + 1393

    cdef jb(self, float jumpHeight, peak= False):
        cdef float bodyHeightCm = self.height * 100
        cdef float jumpHeightCm = jumpHeight * 100
        if peak:
            return 78.6*jumpHeightCm +60.3*self.weight + 15.3*bodyHeightCm + 1308
        return 43.8*jumpHeightCm + 32.7*self.weight - 16.8*bodyHeightCm + 431
        
    cdef sayer(self, float jumpHeight):
        cdef float jumpHeightCm = jumpHeight * 100
        return 60.7*jumpHeightCm + 45.3*self.weight - 2055

    cdef mk(self, float verticalHeight, float time):
        return (self.weight * (verticalHeight/time)) * 9.81


cpdef float brzycki(int reps, float weight):
    return weight/(1.0278-(0.0278 * reps))

cpdef float epley(int reps, float weight):
    return (weight * reps * 0.033)+weight

cpdef float lander(int reps, float weight):
    return weight/(1.013 - (0.0267123 * reps) )

cpdef float lombardi(int reps, float weight):
    return weight*pow(reps,0.10)

cpdef float mayhew(int reps, float weight):
    return (100*weight) / ( (52.2+41.9) * exp(-0.055*reps) )

cpdef float mayhewFootball(int reps):
    return 226.7 + 7.1*(reps)

cpdef float oConnor(int reps, float weight):
    return weight * (1+0.025*reps)

cpdef float wathen(int reps, float weight):
    return (100*weight) / (48.8+(53.8*exp(-0.075 * reps) ) )

cpdef float fatigueRepMap(int reps, float weight):
    return weight / (1.0278 - (reps * 0.0278))

cpdef float twoSetMax(int rep1, float weight1, int rep2, float weight2):
    return ((weight1 - weight2)/(rep2 - rep1)) * (rep1 - 1) + weight1

cdef class RM(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, int gender, float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cdef relativeStrength(self, float rm):
        return rm / self.weight

    cdef ymcaUpperBodyMax(self, int reps):
        if self.gender == Gender.Female:
            return (0.31 * reps) + 19.2
        return (1.55 * reps) + 37.9

    cdef femaleMiddleAgeRepMax(self, int reps, float weight):
        return  (1.06 * weight) + (0.58 * reps) - (0.20 * self.age) - 3.41

    cdef femaleOlderRepMax(self, int reps, float weight):
        return (0.92 * weight) + (0.79 * reps) - (0.20 * self.age) - 3.73

    cdef femaleHipRepMax(self, int reps, float weight):
        return 100 * weight/(48.8 + pow(53.8,(-0.075 * reps) ))
