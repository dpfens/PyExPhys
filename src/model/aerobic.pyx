from libc.math import pow

cdef class Riegel(object):
    cdef readonly float d1
    cdef readonly float t1

    def __cinit__(self, float d1, float t1):
        self.d1 = d1
        self.t1 = t1

    cdef distance(self, float t2):
        if t2 <= 0:
            return 0
        return self.d1*pow(t2, 50/53)/pow(self.t1, 50/53)

    cdef time(self, float d2):
        if d2 <= 0:
            return 0
        return self.t1 * pow( (d2/self.d1), 1.06)

cdef class Cameron(object):
    cdef readonly float d1
    cdef readonly float t1

    def __cinit__(self, float d1, float t1):
        self.d1 = d1
        self.t1 = t1


    cdef __f__(self, float x):
        return 13.49681 - 0.048865*x + 2.438936/pow(x,0.7905)

    cdef time(self, d2):
        if d2 <= 0:
            return 0
        return (self.t1/self.d1) * (self.__f__(self.d1)/self.__f__(d2)) * d2
