from enums import Gender, Activity

cdef class TEE(object):
    cdef readonly int gender
    cdef readonly float age
    cdef readonly float weight
    cdef readonly float height

    def __cinit__(self, int gender, float age, float weight, float height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    cdef float child(self, int activity):
        if activity == Activity.Sedentary and self.gender == Gender.Male:
            return 88.5 - (61.9 * self.age) + 1*((26.7*self.weight)+(903*self.height))
        elif activity == Activity.Sedentary and self.gender == Gender.Female:
            return 135.3 - (30.8 * self.age) + 1*((10*self.weight)+(934*self.height))            
        elif activity == Activity.Low and self.gender == Gender.Male:
            return 88.5 - (61.9 * self.age) + 1.13*((26.7*self.weight)+(903*self.height))
        elif activity == Activity.Low and self.gender == Gender.Female:
            return 135.3 - (30.8 * self.age) + 1.16*((10*self.weight)+(934*self.height))
        elif activity == Activity.Active and self.gender == Gender.Male:
            return 88.5 - (61.9 * self.age) + 1.26*((26.7*self.weight)+(903*self.height))
        elif activity == Activity.Active and self.gender == Gender.Female:
            return 135.3 - (30.8 * self.age) + 1.31*((10*self.weight)+(934*self.height))
        elif activity == Activity.VeryActive and self.gender == Gender.Male:
            return 88.5 - (61.9 * self.age) + 1.42*((26.7* self.weight)+(903* self.height))
        elif activity == Activity.VeryActive and self.gender == Gender.Female:
            return 135.3 - (30.8 * self.age) + 1.56*((10*self.weight)+(934*self.height))
        return 0

    cdef float adult(self, int activity):
        if activity == Activity.Sedentary and self.gender == Gender.Male:
            return 662 - (9.53 * self.age) + 1*((15.9 * self.weight) + (540 * self.height))
        elif activity == Activity.Sedentary and self.gender == Gender.Female:
            return 354 - (6.91 * self.age) + 1*((9.36*self.weight)+(726*self.height))
        elif activity == Activity.Low and self.gender == Gender.Male:
            return 662 - (9.53 * self.age) + 1.11*((15.9*self.weight)+(540*self.height))
        elif activity == Activity.Low and self.gender == Gender.Female:
            return 662 - (9.53 * self.age) + 1.12*((15.9*self.weight)+(540*self.height))
        elif activity == Activity.Active and self.gender == Gender.Male:
            return 662 - (9.53 * self.age) + 1.25*((15.9*self.weight)+(540*self.height))
        elif activity == Activity.Active and self.gender == Gender.Female:
            return 662 - (9.53 * self.age) + 1.27*((15.9*self.weight)+(540*self.height))
        elif activity == Activity.VeryActive and self.gender == Gender.Male:
            return 662 - (9.53 * self.age) + 1.48*((15.9*self.weight)+(540*self.height))
        elif activity == Activity.VeryActive and self.gender == Gender.Female:
            return 662 - (9.53 * self.age) + 1.45*((15.9*self.weight)+(540*self.height))
        return 0
