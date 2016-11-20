from libc.math cimport pow

cdef class Riegel(object):

    def __cinit__(self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1

    cpdef distance(self, double t2):
        if t2 <= 0:
            return 0
        return self.d1*(pow(t2, 50.0/53.0)/pow(self.t1, 50.0/53.0))

    cpdef time(self, double d2):
        if d2 <= 0:
            return 0
        return self.t1 * pow( (d2/self.d1), 1.06)

cdef class Cameron(object):

    def __cinit__(self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1


    cdef __f__(self, double x):
        return 13.49681 - 0.048865*x + 2.438936/pow(x,0.7905)

    cpdef time(self, double d2):
        cdef double d1Miles = self.d1 / 1609.34
        cdef double d2Miles = d2 / 1609.34
        if d2 <= 0:
            return 0
        return (self.t1/d1Miles) * (self.__f__(d1Miles)/self.__f__(d2Miles)) * d2Miles
