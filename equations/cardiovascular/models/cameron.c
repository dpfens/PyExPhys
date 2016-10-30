#include <Python.h>
#include "cameron.h"

/*
  Cameron Running Model
  @description Works well for:
    post-1945 records at the 800m through the 10000m;
    from 1964 onward for the marathon
  @param {double} t1 = time in seconds
  @param {double} d1 = distance in miles
  @param {double} d2 = distance in miles
  @returns {double} t2 = estimated time to travel d2 in seconds
*/
static PyObject * pyPredictTime(PyObject *self, PyObject *args) {
	double t1;
	double d1;
	double d2;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &t1, &d1, &d2))
        	return NULL;

        result = predictTime(t1, d1, d2);
	return Py_BuildValue("d", result);
}

static PyMethodDef CameronMethods[] = {
	{"predictTime", pyPredictTime, METH_VARARGS, "Calculate time over a distance based on the Cameron Model"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initcameron(void)
{
    (void) Py_InitModule("cameron", CameronMethods);
}
