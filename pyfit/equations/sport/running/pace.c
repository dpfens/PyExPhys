#include <Python.h>
#include "pace.h"

/*
calculate velocity at VO2Max
vO2Max in mL/(kg•min)
returns speed in km/h
*/
static PyObject * pyVVo2Max(PyObject *self, PyObject *args) {
	double vO2Max;
	double result;
	if (!PyArg_ParseTuple(args, "d", &vO2Max))
        	return NULL;
	result = vVo2Max(vO2Max);
	return Py_BuildValue("d", result);
}

/*
  @param {Number} percentHR in decimal form
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} speed in km/h
*/
static PyObject * pyHrSpeed(PyObject *self, PyObject *args) {
	double percentHR;
  double vO2Max;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &percentHR, &vO2Max))
        	return NULL;
	result = hrSpeed(percentHR, vO2Max);
	return Py_BuildValue("d", result);
}

/*
  @param {Number} percentHR in decimal form
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
static PyObject * pyHrPace(PyObject *self, PyObject *args) {
	double percentHR;
  double vO2Max;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &percentHR, &vO2Max))
        	return NULL;
	result = hrPace(percentHR, vO2Max);
	return Py_BuildValue("d", result);
}

/*
  Easy / Long (E/L) pace
  @description 60-79% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
static PyObject * pyElPace(PyObject *self, PyObject *args) {
  double vO2Max;
	double result;
	if (!PyArg_ParseTuple(args, "d", &vO2Max))
        	return NULL;
	result = elPace(vO2Max);
	return Py_BuildValue("d", result);
}


/*
  Marathon (M) pace
  @description 80-85% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
static PyObject * pyMPace(PyObject *self, PyObject *args) {
  double vO2Max;
	double result;
	if (!PyArg_ParseTuple(args, "d", &vO2Max))
        	return NULL;
	result = mPace(vO2Max);
	return Py_BuildValue("d", result);
}

/*
  Threshold (T) pace
  @description 82-88% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
static PyObject * pyTPace(PyObject *self, PyObject *args) {
  double vO2Max;
	double result;
	if (!PyArg_ParseTuple(args, "d", &vO2Max))
        	return NULL;
	result = tPace(vO2Max);
	return Py_BuildValue("d", result);
}

/*
  Interval (I) pace
  @description 97-100% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
static PyObject * pyIPace(PyObject *self, PyObject *args) {
  double vO2Max;
	double result;
	if (!PyArg_ParseTuple(args, "d", &vO2Max))
        	return NULL;
	result = iPace(vO2Max);
	return Py_BuildValue("d", result);
}

static PyMethodDef PaceMethods[] = {
  {"vVo2Max", pyVVo2Max, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
  {"hrSpeed", pyHrSpeed, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
  {"hrPace", pyHrPace, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
  {"elPace", pyElPace, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
  {"mPace", pyMPace, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"tPace", pyTPace, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{"iPace", pyIPace, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
  {NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initpace(void)
{
    (void) Py_InitModule("pace", PaceMethods);
}
