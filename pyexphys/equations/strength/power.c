#include <Python.h>
#include "power.h"

/*
@descripion used to estimate peak power from vertical jump height.
Useful for differentiating between two athletes with similar vertical jump heights
Cross-validation against jumps from a force plate showed that the Lewis formula underestimated mean and peak power by up to 70%
@param {Number} body mass (kg)
@param {Number} jump height (meters)
@returns {Number} power (watts)
*/
static PyObject * pyLewis(PyObject *self, PyObject *args) {
	double weight;
	double jumpHeight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &jumpHeight))
        	return NULL;

        result = lewis(weight, jumpHeight);
	return Py_BuildValue("d", result);
}

/*
Harman et al. formula for peak power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
static PyObject * pyPeakPowerHarman(PyObject *self, PyObject *args) {
	double weight;
	double jumpHeight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &jumpHeight))
        	return NULL;

        result = peakPowerHarman(weight, jumpHeight);
	return Py_BuildValue("d", result);
}

/*
Harman et al. formula for mean power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
static PyObject * pyMeanPowerHarman(PyObject *self, PyObject *args) {
	double weight;
	double jumpHeight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &jumpHeight))
        	return NULL;

        result = meanPowerHarman(weight, jumpHeight);
	return Py_BuildValue("d", result);
}


/*
Johnson and Bahamonde formula for peak power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} body height (centimeters)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
static PyObject * pyPeakPowerJB(PyObject *self, PyObject *args) {
	double weight;
  double height;
	double jumpHeight;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &jumpHeight))
        	return NULL;

        result = peakPowerJB(weight, height, jumpHeight);
	return Py_BuildValue("d", result);
}


/*
Johnson and Bahamonde formula for mean power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} body height (centimeters)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
static PyObject * pyMeanPowerJB(PyObject *self, PyObject *args) {
	double weight;
  double height;
	double jumpHeight;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &jumpHeight))
        	return NULL;

        result = meanPowerJB(weight, height, jumpHeight);
	return Py_BuildValue("d", result);
}

/*
Sayers et al. formula for mean power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
static PyObject * pyPeakPowerSayer(PyObject *self, PyObject *args) {
	double weight;
	double jumpHeight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &jumpHeight))
        	return NULL;

        result = peakPowerSayer(weight, jumpHeight);
	return Py_BuildValue("d", result);
}

/*
Margaria-Kalamen Test
@description measures power by assessing
the athlete’s ability to ascend stairs as rapidly as possible.
It has been used, albeit sparingly, to assess an athlete since its inception in the 1960s
@param {Number} body mass (kg)
@param {Number} vertical height (meters)
@returns {Number} power (watts)
*/
static PyObject * pyPowerMK(PyObject *self, PyObject *args) {
	double weight;
	double verticalHeight;
  double time;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &verticalHeight, &time))
        	return NULL;

        result = powerMK(weight, jumpHeight, time);
	return Py_BuildValue("d", result);
}

static PyMethodDef PowerMethods[] = {
  {"lewis", pyLewis, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"peakPowerHarman", pyPeakPowerHarman, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{"meanPowerHarman", pyMeanPowerHarman, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{"peakPowerJB", pyPeakPowerJB, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"meanPowerJB", pyMeanPowerJB, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"peakPowerSayer", pyPeakPowerSayer, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{"powerMK", pyPowerMK, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initpower(void)
{
    (void) Py_InitModule("power", PowerMethods);
}
