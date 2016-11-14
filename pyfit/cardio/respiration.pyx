from libc.math cimport exp, pow
from pyfit.enums import Gender

cdef class ResidualVolume(object):
    cdef readonly int gender
    cdef readonly float height # meters
    cdef readonly float age # years
    cdef readonly float weight # kg

    def __cinit__(self, int gender,  float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height


    cpdef float normal(self):
        cdef float heightCm = self.height * 100
        return 0.0275 * self.age + 0.0189*heightCm - 2.6139

    cpdef float overweight(self):
        cdef float heightCm = self.height * 100
        return 0.0277 * self.age + 0.0138*heightCm - 2.3967

    cpdef float berglund(self):
        cdef float heightCm = self.height * 100
        if self.gender == Gender.Female:
            return 0.007*self.age + 0.0268*self.height - 3.42
        return (0.022*self.age) + (0.0198*heightCm) - (0.015*self.weight) - 1.54

    cpdef float black(self):
        cdef float heightCm = self.height * 100
        return 0.21 * self.age + 0.023*heightCm - 2.978

    cpdef float boren(self):
        cdef float heightCm = self.height * 100
        return (0.0115*self.age) + (0.019* heightCm) - 2.24

    cpdef float goldman(self):
        cdef float heightCm = self.height * 100
        if self.gender == Gender.Female:
            return 0.009*self.age + 0.032*heightCm - 3.9
        return (0.017*self.age) + (0.027*heightCm) - 3.477

    cpdef float obrien(self, float bsa):
        cdef float heightCm = self.height * 100
        return (0.03*self.age) + (0.0387*heightCm) - (0.73*bsa) - 4.78

cdef class VO2(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, int gender, float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cpdef float reserve(self, float vo2Max, float vo2Rest=3.5):
        return vo2Max - vo2Rest

    cpdef float target(self, float vo2Max, float vo2Rest, float intensity):
        return intensity * (vo2Max - vo2Rest)+ vo2Rest

    cpdef float cooper(self, float distance):
        return 0.0268 * distance - 11.3

    cpdef float walkingGross(self, float speed, float grade):
        return (0.1*speed) + (1.8*speed*grade)

    cpdef float runningGross(self, float speed, float grade):
        return (0.2*speed) + (0.9*speed*grade)

    cpdef float legErgometryGross(self, float mass, float work):
        return 3.5 + 1.8* (work/mass)

    cpdef float armErgometryGross(self, float mass, float work):
        return (3.0 * work/mass)

    cpdef float steppingGross(self, float height, float frequency):
        return (0.2*frequency) + (frequency * self.height * 1.8 * 1.33)

    cpdef float usop(self, float hrMax, float restingHR):
        return 15.3 * (hrMax/restingHR)

    cpdef float foxErgometry(self, float hr5):
        return 6300.0 - (19.26 * hr5)

    cpdef float ebbelingTreadmill(self, float speed, float hr):
        if self.gender == Gender.Female:
            return 15.1 + (21.8 * speed) - (0.327*hr) - (0.263*self.age) + (0.00504 * (hr*self.age) )+(5.48 * 0.0)
        return 15.1+(21.8*speed)-(0.327*hr)-(0.263*self.age)+( 0.00504*(hr*self.age) )+(5.48*1.0)

    cpdef float kline(self, float time, float hrPeak):
        if self.gender == Gender.Female:
            return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*0.0 - 3.2649*time - 0.1565*hrPeak
        return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*1.0 - 3.2649*time - 0.1565*hrPeak

    cpdef float larsen(self, float time, float hr):
        if self.gender == Gender.Female:
            return 100.16 + (7.30*0.0) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr)
        return 100.16 + (7.30*1.0) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr);

    cpdef float astrandStep(self, float hr):
        if self.gender == Gender.Female:
            return 3.750*((self.weight+3)/(hr-65))
        return 3.744*((self.weight+5)/(hr-62))

    cpdef float qcStep(self, float hr):
        if self.gender == Gender.Female:
            return 65.81-(0.1847 * hr)
        return 111.33 - (0.42 * hr)

    cpdef float georgeRW(self, float time):
        if self.gender == Gender.Female:
            return 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*0.0)
        return 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*1.0)

    cpdef float georgeSteady(self, float time, float hr):
        if self.gender == Gender.Female:
            return 100.5 - 0.1636*self.weight - 1.438 * time - 0.1928 * hr
        return 100.5 - 0.1636*self.weight - 1.438 * time - 0.1928 * hr + 8.344

    cpdef float georgeTreadmill(self, float speed, float hr):
        if self.gender == Gender.Female:
            return 54.07-(0.1938* self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*0.0)
        return 54.07-(0.1938*self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*1.0)

    cpdef float treadmillSubmaxSingleStage(self, float sm1, float hr1, float hrmax):
        if self.gender == Gender.Female:
            return sm1*( (hrmax-72) / (hr1-72) )
        return sm1*( (hrmax-61) / (hr1-61) )

    cpdef float treadmillSubmaxVO2Multistage(self, float sm1, float hr1, float sm2, float hr2, float hrMax):
        cdef float b = (sm2 - sm1) / (hr2 - hr1)
        return sm2+b*(hrMax-hr2)

    cpdef float curetonChild(self, float time):
        cdef float bmi = (self.weight/pow(self.height/100, 2))
        return 108.94 - (8.41 * time) + 0.34 * 108.94 - (8.41 * time) + 0.34 * pow(time,2) + 0.21*self.age - (0.84*bmi)

    cpdef float balke(self, float time):
        if self.gender == Gender.Female:
            return 1.38 * time + 5.22
        return 1.444 * time + 14.99

    cpdef float balke15MinRun(self, float distance):
        return 0.0178*distance + 9.6

    cpdef float bruceMale(self, float time, float time2, float time3):
        return 14.76 - 1.379*time + 0.451*time2 - 0.012*time3

    cpdef float bruceFemale(self, float time):
        return 4.38 * time - 3.90

    cpdef float bruceEC(self, float time):
        return (2.282*time) + 8.545

    cpdef float leger(self, float speed):
        return 31.025 + (3.238*speed) - (3.248*self.age) + 0.1536*(self.age*speed)

    cpdef float gilbertDaniels(self, float velocity, float time):
        cdef float numerator = 0.000104*pow(velocity,2)+0.182258* velocity-4.6
        cdef float denominator= 0.2989558*exp(-0.1932605*time)+0.1894393*exp(-0.012778*time)+0.8
        return numerator/denominator
