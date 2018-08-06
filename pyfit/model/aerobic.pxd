cdef class Riegel:
    cdef readonly double d1
    cdef readonly double t1

    cpdef double distance(Riegel self, double t2, double multiplier=*)

    cpdef double time(Riegel self, double d2, double multiplier=*)

cdef class Cameron:
    cdef readonly double d1
    cdef readonly double t1

    cdef double __f__(Cameron self, double x)

    cpdef double time(Cameron self, double d2)

cdef class VV:
    cdef readonly double d1
    cdef readonly double t1

    cdef double adj_timer(VV self, double d1, double t1)

    cdef double riegel_velocity(VV self, double distance, double multiplier=*)

    cpdef double time(VV self, double mileage, double d2=*)

    cpdef double time2(VV self, double mileage, double d2, double t2, double distance=*)
