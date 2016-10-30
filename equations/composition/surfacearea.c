#include <Python.h>
#include "surfacearea.h"

static PyObject * pyBoyd(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = boyd(height, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyCosteff(PyObject *self, PyObject *args) {
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "d", &weight))
        	return NULL;

        result = costeff(weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyDubois(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = dubois(height, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyFujimoto(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = fujimoto(height, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyGehangeorge(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = gehangeorge(height, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyHaycock(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = haycock(height, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyMosteller(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = mosteller(height, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyShuterAslani(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = shuterAslani(height, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyTahahira(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &weight))
        	return NULL;

        result = tahahira(height, weight);
	return Py_BuildValue("d", result);
}


static PyMethodDef SurfaceAreaMethods[] = {
	{"boyd",  pyBoyd, METH_VARARGS, "Estimate body surface area using Boyd formula"},
	{"costeff",  pyCosteff, METH_VARARGS, "Estimate body surface area using Costeff formula"},
	{"dubois",  pyDubois, METH_VARARGS, "Estimate body surface area using DuBois formula"},
	{"fujimoto",  pyFujimoto, METH_VARARGS, "Estimate body surface area using Fujimoto formula"},
	{"gehangeorge",  pyGehangeorge, METH_VARARGS, "Estimate body surface area using Gehan-George formula"},
	{"haycock",  pyHaycock, METH_VARARGS, "Estimate body surface area using Haycock formula"},
	{"mosteller",  pyMosteller, METH_VARARGS, "Estimate body surface area using Mosteller formula"},
	{"shuterAslani",  pyShuterAslani, METH_VARARGS, "Estimate body surface area using Shuter-Aslani formula"},
	{"tahahira",  pyTahahira, METH_VARARGS, "Estimate body surface area using Tahahira formula"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initsurfacearea(void)
{
	(void) Py_InitModule("surfacearea", SurfaceAreaMethods);
}
