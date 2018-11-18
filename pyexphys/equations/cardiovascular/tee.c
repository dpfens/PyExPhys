#include <Python.h>
#include "tee.h"

/*
All equations take
weight in kg
height in meters
age in years
*/


static PyObject * pyChildMaleSedentaryTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
		return NULL;

        result = childMaleSedentaryTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildFemaleSedentaryTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childFemaleSedentaryTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildMaleLowTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childMaleLowTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildFemaleLowTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childFemaleLowTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildMaleActiveTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childMaleActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildFemaleActiveTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childFemaleActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildMaleVeryActiveTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childMaleVeryActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildFemaleVeryActiveTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childFemaleVeryActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}




static PyObject * pyAdultMaleSedentaryTee(PyObject *self, PyObject *args) {
        double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultMaleSedentaryTee(weight, height, age);
	return Py_BuildValue("d", result);
}


static PyObject * pyAdultFemaleSedentaryTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

	result = adultFemaleSedentaryTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultMaleLowTee(PyObject *self, PyObject *args) {
        double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultMaleLowTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultFemaleLowTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultFemaleLowTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultMaleActiveTee(PyObject *self, PyObject *args) {
        double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultMaleActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultFemaleActiveTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultFemaleActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultMaleVeryActiveTee(PyObject *self, PyObject *args) {
        double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultMaleVeryActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultFemaleVeryActiveTee(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultFemaleVeryActiveTee(weight, height, age);
	return Py_BuildValue("d", result);
}



static PyMethodDef TEEMethods[] = {
	{"childMaleSedentaryTee", pyChildMaleSedentaryTee, METH_VARARGS, "Estimate total energy expenditure in sedentary male children"},
	{"childFemaleSedentaryTee", pyChildFemaleSedentaryTee, METH_VARARGS, "Estimate total energy expenditure in sedentary female children"},
	{"childMaleLowTee", pyChildMaleLowTee, METH_VARARGS, "Estimate total energy expenditure in low-activity male children"},
	{"childFemaleLowTee", pyChildFemaleLowTee, METH_VARARGS, "Estimate total energy expenditure in low-activity female children"},
	{"childMaleActiveTee", pyChildMaleActiveTee, METH_VARARGS, "Estimate total energy expenditure in active male children"},
	{"childFemaleActiveTee", pyChildFemaleActiveTee, METH_VARARGS, "Estimate total energy expenditure in active female children"},
	{"childMaleVeryActiveTee", pyChildMaleVeryActiveTee, METH_VARARGS, "Estimate total energy expenditure in very active male children"},
	{"childFemaleVeryActiveTee", pyChildFemaleVeryActiveTee, METH_VARARGS, "Estimate total energy expenditure in very active female children"},

	{"adultMaleSedentaryTee", pyAdultMaleSedentaryTee, METH_VARARGS, "Estimate total energy expenditure in sedentary male adults"},
	{"adultFemaleSedentaryTee", pyAdultFemaleSedentaryTee, METH_VARARGS, "Estimate total energy expenditure in sedentary female adults"},

	{"adultMaleLowTee", pyAdultMaleLowTee, METH_VARARGS, "Estimate total energy expenditure in low-activity male adults"},
	{"adultFemaleLowTee", pyAdultFemaleLowTee, METH_VARARGS, "Estimate total energy expenditure in low-activity female adults"},

	{"adultMaleActiveTee", pyAdultMaleActiveTee, METH_VARARGS, "Estimate total energy expenditure in active male adults"},
	{"adultFemaleActiveTee", pyAdultFemaleActiveTee, METH_VARARGS, "Estimate total energy expenditure in active female adults"},

	{"adultMaleVeryActiveTee", pyAdultMaleVeryActiveTee, METH_VARARGS, "Estimate total energy expenditure in very active male adults"},
	{"adultFemaleVeryActiveTee", pyAdultFemaleVeryActiveTee, METH_VARARGS, "Estimate total energy expenditure in very active female adults"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC inittee(void)
{
    (void) Py_InitModule("tee", TEEMethods);
}
