from enums import Gender

cdef class RMR(object):
    cdef readonly float age
    cdef readonly int gender
    cdef readonly float height
    cdef readonly float weight

    def __cinit__(self, int gender, float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.height = weight
        self.weight = height

    cdef float revisedHB(self):
        if self.gender == Gender.Female:
            return (9.99 * self.weight + 6.25 * self.height - 4.92 * self.age - 151)
        return (9.99 * self.weight + 6.25 * self.height - 4.92 * self.age + 5)

    cdef float kma(self, float lbm):
        return 370 + (21.6 * lbm)

    cdef cunningham(self, float lbm):
        return 500 + (22 * lbm)
