cdef class HR(object):
    cdef int age
    cdef readonly dict __dir__

    def __cinit__(self, int age):
        self.age = age

    """
    Fox(1971)
    @description Recommended for use with older adults
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """
    cdef float maxFox(self):
        return 208.0 - (0.7 * self.age)

    """
    Gellish (2007)
    @description For use on men and women participants in an adult fitness program with broad range of age and fitness levels
    @see http://www.myfitnesspal.com/blog/mmmaddox/view/american-college-of-sports-medicine-american-heart-association-training-recommendations-254928
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """
    cdef float maxGellish(self):
        return 207 - (0.7 * self.age)

    """
    Astrand (1952)
    @description For use on men and women ages 4 to 34 yr
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """
    cdef float maxAstrand(self):
        return 216.6-(0.84*self.age)

    """
    Tanaka (2001)
    @description For use on healthy men and women
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """
    cdef float maxTanaka(self):
        return 208-(0.7*self.age)

    """
    Gulati (2010)
    @description For use on asymptomatic middle aged women referred for stress testing
    @params {Number} age in years
    @returns {Number} max heart rate in bpm
    """
    cdef float maxGulati(self):
        return 206-(0.88*self.age)

    cdef float mean_arterial_pressure(self, int diastolic_bp, int systolic_bp):
        return ((2 * diastolic_bp) + systolic_bp) / 3 

    cdef float target_hr(self, float intensity, int rest, int maximum):
        return intensity * (maximum - rest) + rest

cdef class ResidualVolume(object):
    cdef float height # meters
    cdef float age # years
    cdef float weight # kg
    cdef readonly dict __dict__

    def __cinit__(self, float age, float weight, float height):
        self.age = age
        self.weight = weight
        self.height = height

    cdef berglund(self):
        cdef float height_meters = self.height / 100
        return (0.0115*self.age) + (0.019* height_meters) - 2.24;

    cdef boren(self):
        cdef float height_meters = self.height / 100
        return (0.022*self.age) + (0.0198*height_meters) - (0.015*self.weight) - 1.54

    cdef goldman(self):
        cdef float height_meters = self.height / 100
        return (0.017*self.age) + (0.027*self.height) - 3.477

    cdef obrien(self, float bsa):
        cdef float height_meters = self.height / 100
        return (0.03*self.age) + (0.0387*height_meters) - (0.73*bsa) - 4.78
