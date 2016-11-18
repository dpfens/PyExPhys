from libc.math cimport exp, pow
from pyfit.enums import Gender

cdef class ResidualVolume(object):
    cdef readonly int gender
    cdef readonly double height # meters
    cdef readonly double age # years
    cdef readonly double weight # kg

    def __cinit__(self, int gender,  double age, double weight, double height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height


    cpdef double normal(self):
        cdef double heightCm = self.height * 100
        return 0.0275 * self.age + 0.0189*heightCm - 2.6139

    cpdef double overweight(self):
        cdef double heightCm = self.height * 100
        return 0.0277 * self.age + 0.0138*heightCm - 2.3967

    cpdef double berglund(self):
        cdef double heightCm = self.height * 100
        if self.gender == Gender.Female:
            return 0.007*self.age + 0.0268*self.height - 3.42
        return (0.022*self.age) + (0.0198*heightCm) - (0.015*self.weight) - 1.54

    cpdef double black(self):
        cdef double heightCm = self.height * 100
        return 0.21 * self.age + 0.023*heightCm - 2.978

    cpdef double boren(self):
        cdef double heightCm = self.height * 100
        return (0.0115*self.age) + (0.019* heightCm) - 2.24

    cpdef double goldman(self):
        cdef double heightCm = self.height * 100
        if self.gender == Gender.Female:
            return 0.009*self.age + 0.032*heightCm - 3.9
        return (0.017*self.age) + (0.027*heightCm) - 3.477

    cpdef double obrien(self, double bsa):
        cdef double heightCm = self.height * 100
        return (0.03*self.age) + (0.0387*heightCm) - (0.73*bsa) - 4.78

cdef class VO2(object):
    cdef readonly int gender
    cdef readonly double age
    cdef readonly double weight
    cdef readonly double height

    def __cinit__(self, int gender, double age, double weight, double height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cpdef double reserve(self, double vo2Max, double vo2Rest=3.5):
        return vo2Max - vo2Rest

    cpdef double target(self, double vo2Max, double vo2Rest, double intensity):
        return intensity * (vo2Max - vo2Rest)+ vo2Rest

    cpdef double cooper(self, double distance):
        return 0.0268 * distance - 11.3

    cpdef double walkingGross(self, double speed, double grade):
        return (0.1*speed) + (1.8*speed*grade)

    cpdef double runningGross(self, double speed, double grade):
        return (0.2*speed) + (0.9*speed*grade)

    cpdef double legErgometryGross(self, double mass, double work):
        return 3.5 + 1.8* (work/mass)

    cpdef double armErgometryGross(self, double mass, double work):
        return (3.0 * work/mass)

    cpdef double steppingGross(self, double height, double frequency):
        return (0.2*frequency) + (frequency * self.height * 1.8 * 1.33)

    cpdef double usop(self, double hrMax, double restingHR):
        return 15.3 * (hrMax/restingHR)

    cpdef double foxErgometry(self, double hr5):
        return 6300.0 - (19.26 * hr5)

    cpdef double ebbelingTreadmill(self, double speed, double hr):
        if self.gender == Gender.Female:
            return 15.1 + (21.8 * speed) - (0.327*hr) - (0.263*self.age) + (0.00504 * (hr*self.age) )+(5.48 * 0.0)
        return 15.1+(21.8*speed)-(0.327*hr)-(0.263*self.age)+( 0.00504*(hr*self.age) )+(5.48*1.0)

    cpdef double kline(self, double time, double hrPeak):
        if self.gender == Gender.Female:
            return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*0.0 - 3.2649*time - 0.1565*hrPeak
        return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*1.0 - 3.2649*time - 0.1565*hrPeak

    cpdef double larsen(self, double time, double hr):
        if self.gender == Gender.Female:
            return 100.16 + (7.30*0.0) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr)
        return 100.16 + (7.30*1.0) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr);

    cpdef double astrandStep(self, double hr):
        if self.gender == Gender.Female:
            return 3.750*((self.weight+3)/(hr-65))
        return 3.744*((self.weight+5)/(hr-62))

    cpdef double qcStep(self, double hr):
        if self.gender == Gender.Female:
            return 65.81-(0.1847 * hr)
        return 111.33 - (0.42 * hr)

    cpdef double georgeRW(self, double time):
        if self.gender == Gender.Female:
            return 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*0.0)
        return 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*1.0)

    cpdef double georgeSteady(self, double time, double hr):
        if self.gender == Gender.Female:
            return 100.5 - 0.1636*self.weight - 1.438 * time - 0.1928 * hr
        return 100.5 - 0.1636*self.weight - 1.438 * time - 0.1928 * hr + 8.344

    cpdef double georgeTreadmill(self, double speed, double hr):
        if self.gender == Gender.Female:
            return 54.07-(0.1938* self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*0.0)
        return 54.07-(0.1938*self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*1.0)

    cpdef double treadmillSubmaxSingleStage(self, double sm1, double hr1, double hrmax):
        if self.gender == Gender.Female:
            return sm1*( (hrmax-72) / (hr1-72) )
        return sm1*( (hrmax-61) / (hr1-61) )

    cpdef double treadmillSubmaxVO2Multistage(self, double sm1, double hr1, double sm2, double hr2, double hrMax):
        cdef double b = (sm2 - sm1) / (hr2 - hr1)
        return sm2+b*(hrMax-hr2)

    cpdef double curetonChild(self, double time):
        cdef double bmi = (self.weight/pow(self.height/100, 2))
        return 108.94 - (8.41 * time) + 0.34 * 108.94 - (8.41 * time) + 0.34 * pow(time,2) + 0.21*self.age - (0.84*bmi)

    cpdef double balke(self, double time):
        if self.gender == Gender.Female:
            return 1.38 * time + 5.22
        return 1.444 * time + 14.99

    cpdef double balke15MinRun(self, double distance):
        return 0.0178*distance + 9.6

    cpdef double bruceMale(self, double time, double time2, double time3):
        return 14.76 - 1.379*time + 0.451*time2 - 0.012*time3

    cpdef double bruceFemale(self, double time):
        return 4.38 * time - 3.90

    cpdef double bruceEC(self, double time):
        return (2.282*time) + 8.545

    cpdef double leger(self, double speed):
        return 31.025 + (3.238*speed) - (3.248*self.age) + 0.1536*(self.age*speed)

    cpdef double gilbertDaniels(self, double velocity, double time):
        cdef double numerator = 0.000104*pow(velocity,2)+0.182258* velocity-4.6
        cdef double denominator= 0.2989558*exp(-0.1932605*time)+0.1894393*exp(-0.012778*time)+0.8
        return numerator/denominator
