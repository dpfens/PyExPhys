#include <Python.h>
#include "riegel.h"

/*
  Riegel Running Model
  @description t2 = t1 * (d2/d1) ^ 1.06
  @static
  @param {Number} t1 = time
  @param {Number} d1 = old distance
  @param {Number} d2 = new distance
  d1 & d2 must be in the same unit
  @returns {Number} t2 = estimated time to travel d2 in same unit as t1
*/
static PyObject * py_predict_time(PyObject *self, PyObject *args) {
	double t1;
	double d1;
	double d2;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &t1, &d1, &d2))
        	return NULL;

        result = predict_time(t1, d1, d2);
	return Py_BuildValue("d", result);
}

/*
  Derived from the Riegel Running Model
  @static
  @description d2 = d1*t2^(50/53)/t1^(50/53)
  @param {Number} t1 = time
  @param {Number} d1 = old distance
  @param {Number} t2 = new time
  d1 & d2 must be in the same unit
  @returns {Number} d2 = estimated distance travelled in t2 in same unit as d1
*/
static PyObject * py_predict_distance(PyObject *self, PyObject *args) {
	double t1;
	double d1;
	double t2;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &t1, &d1, &t2))
        	return NULL;

        result = predict_distance(t1, d1, t2);
	return Py_BuildValue("d", result);
}

static PyMethodDef RiegelMethods[] = {
	{"predict_time", py_predict_time, METH_VARARGS, "Calculate time over a distance based on the Riegel Model."},
	{"predict_distance", py_predict_distance, METH_VARARGS, "Calculate distance over time based on the Riegel Model"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initriegel(void)
{
    (void) Py_InitModule("riegel", RiegelMethods);
}
