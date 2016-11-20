cdef class Riegel:
    cdef readonly double d1
    cdef readonly double t1

    cpdef distance(self, double t2)

    cpdef time(self, double d2)

cdef class Cameron:
    cdef readonly double d1
    cdef readonly double t1

    cdef __f__(self, double x)

    cpdef time(self, double d2)
