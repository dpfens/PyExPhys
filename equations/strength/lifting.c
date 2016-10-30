#include <Python.h>
#include "lifting.h"


/*
@param {Number} weight lifted in kg
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
static PyObject * pyOCarroll(PyObject *self, PyObject *args) {
	double bodyWeight;
	double weightLifted;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &bodyWeight, &weightLifted))
        	return NULL;

        result = oCarroll(bodyWeight, weightLifted);
	return Py_BuildValue("d", result);
}


/*
@description For use in non-power lifts. To compare the performances of lifters of different bodymass, simply substitute each lifter's bodymass in the relevant equations above to calculate the Total (or lift) expected for a top world class lifter. Then divide each lifter's actual Total by this value to obtain the percentage of the world class lift achieved by each lifter. See: http://dziepak.freeiz.com/training/formulas.htm
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
static PyObject * pySiffWeightLiftingMale(PyObject *self, PyObject *args) {
	double bodyWeight;
	double result;
	if (!PyArg_ParseTuple(args, "d", &bodyWeight))
        	return NULL;

        result = siffWeightLiftingMale(bodyWeight);
	return Py_BuildValue("d", result);
}

/*
@description For use in non-power lifts. To compare the performances of lifters of different bodymass, simply substitute each lifter's bodymass in the relevant equations above to calculate the Total (or lift) expected for a top world class lifter. Then divide each lifter's actual Total by this value to obtain the percentage of the world class lift achieved by each lifter. See: http://dziepak.freeiz.com/training/formulas.htm
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
static PyObject * pySiffWeightLiftingFemale(PyObject *self, PyObject *args) {
	double bodyWeight;
	double result;
	if (!PyArg_ParseTuple(args, "d", &bodyWeight))
        	return NULL;

        result = siffWeightLiftingFemale(bodyWeight);
	return Py_BuildValue("d", result);
}


/*
@description For use in power lifts by males. To compare the performances of lifters of different bodymass, simply substitute each lifter's bodymass in the relevant equations above to calculate the Total (or lift) expected for a top world class lifter. Then divide each lifter's actual Total by this value to obtain the percentage of the world class lift achieved by each lifter. See: http://dziepak.freeiz.com/training/formulas.htm
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
static PyObject * pySiffPowerLiftingMale(PyObject *self, PyObject *args) {
	double bodyWeight;
	double result;
	if (!PyArg_ParseTuple(args, "d", &bodyWeight))
        	return NULL;

        result = siffPowerLiftingMale(bodyWeight);
	return Py_BuildValue("d", result);
}


/*
	@description See: https://en.wikipedia.org/wiki/Sinclair_Coefficients
	@param {Number} obtainedTotal weight in kg
	@returns {Number} sinclair coefficient
*/
static PyObject * pySinclairMale(PyObject *self, PyObject *args) {
	double body_weight;
	double obtained_total;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &body_weight, &obtained_total))
        	return NULL;

        result = sinclairMale(body_weight, obtained_total);
	return Py_BuildValue("d", result);
}

/*
	@description See: https://en.wikipedia.org/wiki/Sinclair_Coefficients
	@param {Number} obtainedTotal weight in kg
	@returns {Number} sinclair coefficient
*/
static PyObject * pySinclairFemale(PyObject *self, PyObject *args) {
	double body_weight;
	double obtained_total;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &body_weight, &obtained_total))
        	return NULL;

        result = sinclairFemale(body_weight, obtained_total);
	return Py_BuildValue("d", result);
}

/*
	@description See: https://en.wikipedia.org/wiki/Wilks_Coefficient
	@param {Number} body mass in kg
	@param {Number} weightLifted in kg
	@returns {Number} wilks coefficient
*/
static PyObject * pyWilksMale(PyObject *self, PyObject *args) {
	double body_weight;
	double weight_lifted;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &body_weight, &weight_lifted))
        	return NULL;

        result = wilksMale(body_weight, weight_lifted);
	return Py_BuildValue("d", result);
}


/*
	@description See: https://en.wikipedia.org/wiki/Wilks_Coefficient
	@param {Number} body mass in kg
	@param {Number} weightLifted in kg
	@returns {Number} wilks coefficient
*/
static PyObject * pyWilksFemale(PyObject *self, PyObject *args) {
	double body_weight;
	double weight_lifted;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &body_weight, &weight_lifted))
        	return NULL;

        result = wilksFemale(body_weight, weight_lifted);
	return Py_BuildValue("d", result);
}


static PyMethodDef LiftingMethods[] = {
	{"oCarroll", pyOCarroll, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"siffWeightLiftingMale", pySiffWeightLiftingMale, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"siffWeightLiftingFemale", pySiffWeightLiftingFemale, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"siffPowerLiftingMale", pySiffPowerLiftingMale, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"sinclairMale", pySinclairMale, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"sinclairFemale", pySinclairFemale, METH_VARARGS, "Compare different weight classes in olympic weightlifting."},
	{"wilksMale", pyWilksMale, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{"wilksFemale", pyWilksFemale, METH_VARARGS, "Measure the strength of a powerlifter against other powerlifters despite the different weights of the lifters"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initlifting(void)
{
    (void) Py_InitModule("lifting", LiftingMethods);
}
