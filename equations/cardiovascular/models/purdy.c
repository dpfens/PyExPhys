#include <Python.h>
#include "purdy.h"

/*
The Purdy point system is calculated from a table of running performances
compiled in 1936 called the Portuguese scoring Tables. The table lists
distance and velocity from 40 meters to 100,000 meters. These velocity
measures are assumed to be maximum possible velocity in a straight line.
These performances are arbitrarily given a Purdy point of 950.
World record times in 1970 have about 1035 Purdy points.
Times are calculated from the table (t=d/v) by linear interpolation.
Additionally, a time factor for startup and running on a curve of a track
is also added.  This "standard Calculated" time is used to generate
the points given some performace time at the same distance.
          P = A(Ts/Tp - B)
  where P - is purdy points
        Ts - Standard time from tables + time factor
        Tp - Performance time to be compared
        A, B - the scaling factors.

  However A and B have to change for different distances.
   A sliding scale for A and B was found by comparing velocity
  at 3 miles and 100 meters at 950 and 1035 pt. performances.
       Purdy comes up with:
                   k = 0.0654 - 0.00258V
                   A = 85/k
                   B = 1-950/A
         where V is the avg. velocity of Tp
*/
static PyObject * pyPurdy(PyObject *self, PyObject *args) {
	double distance;
	float tsec;
	double result;
	if (!PyArg_ParseTuple(args, "df", &distance, &tsec))
    return NULL;

    result = purdy(distance, tsec);
	return Py_BuildValue("f", result);
}

static PyObject * pyPurdyLS(PyObject *self, PyObject *args) {
	double distance;
	double seconds;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &distance, &seconds))
    return NULL;

    result = purdyLS(distance, seconds);
	return Py_BuildValue("d", result);
}


static PyMethodDef PurdyMethods[] = {
	{"points", pyPurdy, METH_VARARGS, "Calculate Purdy points based on a running performance."},
	{"pointsLS", pyPurdyLS, METH_VARARGS, "Calculate Purdy points based on a running performance based on a least squared curve."},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initpurdy(void)
{
    (void) Py_InitModule("purdy", PurdyMethods);
}
