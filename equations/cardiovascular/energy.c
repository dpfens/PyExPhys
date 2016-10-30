#include <Python.h>
#include "energy.h"

static PyObject * py_carbohydrate(PyObject *self, PyObject *args) {
	double percentVO2;
	double result;
	if (!PyArg_ParseTuple(args, "d", &percentVO2))
        	return NULL;
	result = carbohydrate(percentVO2);
	return Py_BuildValue("d", result);
}

static PyObject * py_fat(PyObject *self, PyObject *args) {
  double percentVO2;
	double result;
	if (!PyArg_ParseTuple(args, "d", &percentVO2))
        	return NULL;
	result = fat(percentVO2);
	return Py_BuildValue("d", result);
}

static PyMethodDef EnergyMethods[] = {
	{"carbohydrate", py_carbohydrate, METH_VARARGS, "Percentage of energy drawn from carbohydrate at a given VO2Percentage"},
	{"fat", py_fat, METH_VARARGS, "Percentage of energy drawn from fat at a given VO2Percentage"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initenergy(void)
{
	(void) Py_InitModule("energy", EnergyMethods);
}
