#include <Python.h>
#include "indices.h"

static PyObject * pyBmi(PyObject *self, PyObject *args) {
	double kg;
	double height;
	double result;
	if (!PyArg_ParseTuple(args, "ff", &kg, &height))
        	return NULL;
	result = bmi(kg, height);
	return Py_BuildValue("f", result);
}

static PyObject * pyPonderal(PyObject *self, PyObject *args) {
	double kg;
	double height;
	double result;
	if (!PyArg_ParseTuple(args, "ff", &kg, &height))
        	return NULL;
	result = ponderal(kg, height);
	return Py_BuildValue("f", result);
}

static PyMethodDef IndicesMethods[] = {
	{"bmi", pyBmi, METH_VARARGS, "Estimate body composition using body mass index formula"},
	{"ponderal", pyPonderal, METH_VARARGS, "Estimate body composition using Ponderal index formula"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initindices(void)
{
    (void) Py_InitModule("indices", IndicesMethods);
}
