#include <Python.h>
#include "jackdaniels.h"

/*
@description a regression equation relating VO2 with running velocity. Used in conjuction with the "vO2" equation to create the Jack Daniel's VDOT tables.  Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.
Conditioning for Distance Running - the Scientific Aspects, 1978
@param {Number} VO2 in mL/kg/minute
@returns {Number} velocity in meters/minute
*/
static PyObject * pyVelocity(PyObject *self, PyObject *args) {
	double vO2;
	double result;
	if (!PyArg_ParseTuple(args, "d", &vO2))
        	return NULL;
	result = velocity(vO2);
	return Py_BuildValue("d", result);
}

/*
@description a regression equation relating VO2 with running velocity. Used in conjuction with the "velocity" equation to create the Jack Daniel's VDOT tables.  Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.
Conditioning for Distance Running - the Scientific Aspects, 1978
@param {Number} velocity in meters/minute
@returns {Number} VO2 in mL/kg/minute
*/
static PyObject * pyVO2(PyObject *self, PyObject *args) {
	double velocity;
	double result;
	if (!PyArg_ParseTuple(args, "d", &velocity))
        	return NULL;
	result = vO2(velocity);
	return Py_BuildValue("d", result);
}

/*
@description describes the percent of an individual's aerobic capacity the individual is capable of working at for how long.  Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.
Conditioning for Distance Running - the Scientific Aspects, 1978
@param {Number} time spent running in minutes
@returns {Number} VO2 percentage in decimal form
*/
static PyObject * pyVO2Percentage(PyObject *self, PyObject *args) {
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "d", &time))
        	return NULL;
	result = vO2Percentage(time);
	return Py_BuildValue("d", result);
}

static PyMethodDef JackDanielsMethods[] = {
  {"velocity", pyVelocity, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"vO2", pyVO2, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{"vO2Percentage", pyVO2Percentage, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
  {NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initjackdaniels(void)
{
    (void) Py_InitModule("jackdaniels", JackDanielsMethods);
}
