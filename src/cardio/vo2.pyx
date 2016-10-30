from libc.math cimport exp, pow
from enums import Gender


cdef class VO2(object):
    cdef readonly float age
    cdef readonly int gender
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, int gender, float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cdef float reserve(self, float vo2Max, float vo2Rest=3.5):
        return vo2Max - vo2Rest

    cdef float twelveMinVO2(self, float distance):
        return 0.0268 * distance - 11.3

    cdef float walkingGrossVO2(self, float speed, float grade):
        return (0.1*speed) + (1.8*speed*grade) + 3.5

    cdef float runningGrossVo2(self, float speed, float grade):
        return (0.2*speed) + (0.9*speed*grade) + 3.5

    cdef float armErgometryGrossVO2(self, float mass, float work):
        return 3.0 * work/mass

    cdef float steppingVO2(self, float height, float frequency):
        return (0.2*frequency) + (frequency * self.height * 1.8 * 1.33)

    cdef float stairmasterMets(self, int setting):
        return 0.556 * 7.45 * setting

    cdef float usopVO2Max(self, float hrMax, float restingHR):
        return 15.3 * (hrMax/restingHR)

    cdef float foxErgometryVO2max(self, float hr5):
        return 6300.0 - (19.26 * hr5)

    cdef float treadmillWalkVO2MaxMale(self, float speed, float hr):
        return 15.1+(21.8*speed)-(0.327*hr)-(0.263*self.age)+( 0.00504*(hr*self.age) )+(5.48*1.0)

    cdef float treadmillWalkVO2MaxFemale(self, float speed, float hr):
        return 15.1 + (21.8 * speed) - (0.327*hr) - (0.263*self.age) + (0.00504 * (hr*self.age) )+(5.48 * 0.0)
        

    cdef float mileWalkVO2(self, float time, float hrPeak):
        if self.gender == Gender.Female:
            return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*0.0 - 3.2649*time - 0.1565*hrPeak
        return 132.853 - 0.0769*self.weight - 0.3877*self.age + 6.315*1.0 - 3.2649*time - 0.1565*hrPeak

    cdef float mileHalfVo2George(self, float time):
        if self.gender == Gender.Female:
            return 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*0.0)
        return 88.02 - (0.1656*self.weight) - (2.76*time) + (3.716*1.0)

    cdef float mileHalfVo2Larson(self, float time, float hr):
        if self.gender == Gender.Female:
            return 100.16 + (7.30*0.0) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr)
        return 100.16 + (7.30*1.0) - (0.164*self.weight) - (1.273 * time) - (0.1563 * hr);

    cdef float stepTestAstrand(self, float hr):
        if self.gender == Gender.Female:
            return 3.750*((self.weight+3)/(hr-65))
        return 3.744*((self.weight+5)/(hr-62))

        
    cdef float stepTestQueensCollege(self, float hr):
        if self.gender == Gender.Female:
            return 65.81-(0.1847 * hr)
        return 111.33 - (0.42 * hr)

    cdef float treadmillJoggingVO2(self, float speed, float hr):
        if self.gender == Gender.Female:
            return 54.07-(0.1938* self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*0.0)
        return 54.07-(0.1938*self.weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*1.0)



    cdef float treadmillSubmaxSingleStage(self, float sm1, float hr1, float hrmax):
        if self.gender == Gender.Female:
            return sm1*( (hrmax-72) / (hr1-72) )
        return sm1*( (hrmax-61) / (hr1-61) )

        
    cdef float treadmillSubmaxVO2Multistage(self, float sm1, float hr1, float sm2, float hr2, float hrMax):
        cdef float b = (sm2 - sm1) / (hr2 - hr1)
        return sm2+b*(hrMax-hr2)

    cdef float mileVo2Child(self, float time):
        cdef float bmi = (self.weight/pow(self.height/100, 2))
        return 108.94 - (8.41 * time) + 0.34 * 108.94 - (8.41 * time) + 0.34 * pow(time,2) + 0.21*self.age - (0.84*bmi)

    cdef float vo2maxBalke(self, float time):
        if self.gender == Gender.Female:
            return 1.38 * time + 5.22
        return 1.444 * time + 14.99

    cdef float vo2maxBruceMale(self, float time, float time2, float time3):
        return 14.76 - 1.379*time + 0.451*time2 - 0.012*time3

    cdef float vo2MaxBruceFemale(self, float time):
        return 4.38 * time - 3.90

    cdef float vo2maxElderlyCardiac(self, float time):
        return (2.282*time) + 8.545

    cdef float shuttleRunVo2(self, float speed):
        return 31.025 + (3.238*speed) - (3.248*self.age) + 0.1536*(self.age*speed)

    cdef float cooper(self, float distance):
        return (distance - 504.9)  / 44.73

    cdef float copperMiles(self, float distance):
        return (35.97*distance) - 11.29

    cdef float gilbertDaniels(self, float velocity, float time):
        cdef float numerator = 0.000104*pow(velocity,2)+0.182258* velocity-4.6
        cdef float denominator= 0.2989558*exp(-0.1932605*time)+0.1894393*exp(-0.012778*time)+0.8
        return numerator/denominator
