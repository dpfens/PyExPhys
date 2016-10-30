#include <Python.h>
#include "hydration.h"

static PyObject * pyDailyNeeds(PyObject *self, PyObject *args) {
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "d", &weight))
        	return NULL;

        result = dailyNeeds(weight);
	return Py_BuildValue("d", result);
}

static PyMethodDef HydrationMethods[] = {
	{"dailyNeeds", pyDailyNeeds, METH_VARARGS, "Calculate the total amount of water needed daily"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC inithydration(void)
{
    (void) Py_InitModule("hydration", HydrationMethods);
}
