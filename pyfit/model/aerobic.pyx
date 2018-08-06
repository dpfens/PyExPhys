from libc.math cimport log, pow
cimport cython

cdef class Riegel:
    RUNNING_MEN = 1.07732
    RUNNING_MEN_40 = 1.05352
    RUNNING_MEN_50 = 1.05374
    RUNNING_MEN_60 = 1.05603
    RUNNING_MEN_70 = 1.06370
    RUNNING_WOMEN = 1.08283

    SWIMMING_MEN = 1.02977
    SWIMMING_WOMEN = 1.03256

    NORDIC_MEN = 1.01421
    WALKING_MEN = 1.05379
    ROLLER_SKATING_MEN = 1.13709
    CYCLING_MEN = 1.04834
    SPEED_SKATING_MEN = 1.06017

    def __cinit__(Riegel self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1

    @cython.cdivision(True)
    cpdef double distance(Riegel self, double t2, double multiplier=1.06):
        if t2 <= 0:
            return 0
        return self.d1 * (pow(t2, 1 / multiplier) / pow(self.t1, 1 / multiplier))

    @cython.cdivision(True)
    cpdef double time(Riegel self, double d2, double multiplier=1.06):
        if d2 <= 0:
            return 0
        return self.t1 * pow((d2 / self.d1), multiplier)


cdef class Cameron:

    def __cinit__(Cameron self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1

    @cython.cdivision(True)
    cdef double __f__(Cameron self, double x):
        return 13.49681 - 0.048865 * x + 2.438936 / pow(x, 0.7905)

    @cython.cdivision(True)
    cpdef double time(Cameron self, double d2):
        cdef double d1_miles = self.d1 / 1609.34
        cdef double d2_miles = d2 / 1609.34
        if d2 <= 0:
            return 0
        return (self.t1 / d1_miles) * (self.__f__(d1_miles) / self.__f__(d2_miles)) * d2_miles


cdef class VV:

    def __cinit__(VV self, double d1, double t1):
        self.d1 = d1
        self.t1 = t1

    @cython.cdivision(True)
    cdef double adj_timer(VV self, double d1, double t1):
        return d1 / (d1 / t1)

    @cython.cdivision(True)
    cdef double riegel_velocity(VV self, double distance, double multiplier=1.06):
        cdef double adj_timer = self.adj_timer(self.d1, self.t1)
        return distance / (adj_timer * pow(distance / self.d1, multiplier))

    @cython.cdivision(True)
    cpdef double time(VV self, double mileage, double d2=42195.0):
        cdef double riegel_velocity = self.riegel_velocity(d2)
        cdef double velocity = 0.16018617 + (0.83076202 * riegel_velocity) + (0.6423826 * (mileage / 10))
        cdef double minutes = (d2 / 60) / velocity
        cdef double seconds = minutes * 60
        return seconds

    @cython.cdivision(True)
    cpdef double time2(VV self, double mileage, double d2, double t2, double distance=42195.0):
        cdef double adj_timer_r1 = self.adj_timer(self.d1, self.t1)
        cdef double adj_timer_r2 = self.adj_timer(d2, t2)
        cdef k_r2_r1 = log(adj_timer_r2 / adj_timer_r1) / log(d2 / self.d1)
        cdef double k_marathon = 1.4510756 + (-0.23797948 * k_r2_r1) + (-0.01410023 * (mileage / 10))
        cdef double seconds = (adj_timer_r2 * pow(distance / d2, k_marathon))
        return seconds
