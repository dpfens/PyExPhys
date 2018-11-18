#include <Python.h>
#include "stature.h"

static PyObject * py_stature_universal(PyObject *self, PyObject *args) {
	double age;
	double skeletal_height;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &skeletal_height))
        	return NULL;
	result = stature_universal(age, skeletal_height);
	return Py_BuildValue("d", result);	
}

/*
femur measured in cm
*/
static PyObject * py_stature_american_white_male(PyObject *self, PyObject *args) {
	double femur;
	double result;
	if (!PyArg_ParseTuple(args, "d", &femur))
        	return NULL;
	result = stature_american_white_male(femur);
	return Py_BuildValue("d", result);	
}

/*
femur measured in cm
*/
static PyObject * py_stature_american_white_female(PyObject *self, PyObject *args) {
	double femur;
	double result;
	if (!PyArg_ParseTuple(args, "d", &femur))
        	return NULL;
	result = stature_american_white_female(femur);
	return Py_BuildValue("d", result);	
}

/*
femur measured in cm
*/
static PyObject * py_stature_american_black_male(PyObject *self, PyObject *args) {
	double femur;
	double result;
	if (!PyArg_ParseTuple(args, "d", &femur))
        	return NULL;
	result = stature_american_white_male(femur);
	return Py_BuildValue("d", result);	
}

/*
femur measured in cm
*/
static PyObject * py_stature_american_black_female(PyObject *self, PyObject *args) {
	double femur;
	double result;
	if (!PyArg_ParseTuple(args, "d", &femur))
        	return NULL;
	result = stature_american_white_female(femur);
	return Py_BuildValue("d", result);	
}




static PyMethodDef StatureMethods[] = {
	{"stature_universal", py_stature_universal, METH_VARARGS, "Estimate stature in inidivuals with a known height (in cm)"},
	{"stature_american_white_male", py_stature_american_white_male, METH_VARARGS, "Estimate stature in white American men based on femur length"},
	{"stature_american_white_female", py_stature_american_white_female, METH_VARARGS, "Estimate stature in white American women based on femur length"},
	{"stature_american_black_male", py_stature_american_black_male, METH_VARARGS, "Estimate stature in black American men based on femur length"},
	{"stature_american_black_female", py_stature_american_black_female, METH_VARARGS, "Estimate stature in black American women based on femur length"},
};

PyMODINIT_FUNC initstature(void)
{
    (void) Py_InitModule("stature", StatureMethods);
}
