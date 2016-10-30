#include <Python.h>
#include "rmr.h"

/*
	Revised Harris-Benedict BMR Equations
	return calories/day
*/
static PyObject * pyRevisedHbMale(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;
	result = revisedHbMale(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyRevisedHbFemale(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;
	result = revisedHbFemale(weight, height, age);
	return Py_BuildValue("d", result);
}


/*
	Mifflin St Jeor
	returns calories/day
*/
static PyObject * pyMsjMale(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;
	result = msjMale(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyMsjFemale(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;
	result = msjFemale(weight, height, age);
	return Py_BuildValue("d", result);
}

/*
	Katch-McArdle
	return calories/day
*/
static PyObject * pyKma(PyObject *self, PyObject *args) {
	double lbm;
	double result;
	if (!PyArg_ParseTuple(args, "d", &lbm))
        	return NULL;
	result = kma(lbm);
	return Py_BuildValue("d", result);
}

/*
	Cunningham
	return calories/day
*/
static PyObject * pyCunningham(PyObject *self, PyObject *args) {
	double lbm;
	double result;
	if (!PyArg_ParseTuple(args, "d", &lbm))
        	return NULL;
	result = cunningham(lbm);
	return Py_BuildValue("d", result);
}


static PyMethodDef RMRMethods[] = {
	{"revisedHbMale", pyRevisedHbMale, METH_VARARGS, "Calculate resting metabolic rate in men using Harris-Benecit BMR equation. Returns calories/day."},
	{"revisedHbFemale", pyRevisedHbFemale, METH_VARARGS, "Calculate resting metabolic rate in women using Harris-Benecit BMR equation. Returns calories/day."},

	{"msjMale", pyMsjMale, METH_VARARGS, "Calculate resting metabolic rate in men using Mifflin St Jeor formula. Returns calories/day."},
	{"msjFemale", pyMsjFemale, METH_VARARGS, "Calculate resting metabolic rate in women using Mifflin St Jeor formula. Returns calories/day."},

	{"kma", pyKma, METH_VARARGS, "Calculate resting metabolic rate using Katch-McArdle formula. Returns calories/day."},
	{"cunningham", pyCunningham, METH_VARARGS, "Calculate resting metabolic rate using Cunningham formula. Returns calories/day."},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initrmr(void)
{
    (void) Py_InitModule("rmr", RMRMethods);
}
