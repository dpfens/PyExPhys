from libc.math cimport pow

cdef class Riegel:

    def __cinit__(self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1

    cpdef double distance(self, double t2):
        if t2 <= 0:
            return 0
        return self.d1*(pow(t2, 50.0/53.0)/pow(self.t1, 50.0/53.0))

    cpdef double time(self, double d2):
        if d2 <= 0:
            return 0
        return self.t1 * pow( (d2/self.d1), 1.06)

cdef class Cameron:

    def __cinit__(self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1


    cdef double __f__(self, double x):
        return 13.49681 - 0.048865*x + 2.438936/pow(x,0.7905)

    cpdef double time(self, double d2):
        cdef double d1Miles = self.d1 / 1609.34
        cdef double d2Miles = d2 / 1609.34
        if d2 <= 0:
            return 0
        return (self.t1/d1Miles) * (self.__f__(d1Miles)/self.__f__(d2Miles)) * d2Miles

cdef class VV:

    def __cinit__(self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1

    cdef double adj_timer(self, double d1, double t1):
        return d1/(d1/t1)

    cdef double riegel_velocity(self, double distance):
        cdef double adj_timer = self.adj_timer(self.d1, self.t1)
        return distance/(adj_timer* pow(distance/self.d1,1.06) )

    cpdef double time(self, double mileage, double d2=42195.0):
        cdef double riegel_velocity = self.riegel_velocity(d2)
        cdef double velocity = 0.16018617+(0.83076202*riegel_velocity)+(0.6423826*(mileage/10) )
        cdef double minutes = (d2/60)/velocity
        return minutes
