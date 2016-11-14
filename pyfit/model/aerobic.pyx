from libc.math cimport pow

cdef class Riegel(object):
    cdef readonly float d1
    cdef readonly float t1

    def __cinit__(self, float d1, float t1):
        self.d1 = d1
        self.t1 = t1

    cpdef distance(self, float t2):
        if t2 <= 0:
            return 0
        return self.d1*(pow(t2, 50.0/53.0)/pow(self.t1, 50.0/53.0))

    cpdef time(self, float d2):
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

    cpdef time(self, float d2):
        cdef float d1Miles = self.d1 / 1609.34
        cdef float d2Miles = d2 / 1609.34
        if d2 <= 0:
            return 0
        return (self.t1/d1Miles) * (self.__f__(d1Miles)/self.__f__(d2Miles)) * d2Miles
