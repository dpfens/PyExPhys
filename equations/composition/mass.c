#include <Python.h>
#include "mass.h"

/*
Fat Free Mass (FFM)
height in cm
weight in kg
resistance, reactance in ohms
*/

/*
White boys and girls, 8-15 years
Lohman(1992)
*/
static PyObject * py_ffm_child(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &height, &weight, &resistance, &reactance))
        	return NULL;
	result = ffm_child(height, weight, resistance, reactance);
	return Py_BuildValue("d", result);	
}

/*
White boys and girls, 10-19 years
Houtkooper e al. (1992)
*/
static PyObject * py_ffm_adolescent(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &height, &weight, &resistance, &reactance))
        	return NULL;
	result = ffm_adolescent(height, weight, resistance, reactance);
	return Py_BuildValue("d", result);
}

/*
American Indian, black, Hispanic, and White Men
%BF < .20 Segal et al. (1988)
*/
static PyObject * py_ffm_adult_male_lean(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double age;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &height, &weight, &age, &resistance, &reactance))
        	return NULL;
	result = ffm_adult_male_lean(height, weight, age, resistance, reactance);
	return Py_BuildValue("d", result);
}


/*
American Indian, black, Hispanic, and White Women
%BF < .30 Segal et al. (1988)
*/

static PyObject * py_ffm_adult_female_lean(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &height, &weight, &resistance, &reactance))
        	return NULL;
	result = ffm_adult_female_lean(height, weight, resistance, reactance);
	return Py_BuildValue("d", result);
}


/*
American Indian, black, Hispanic, and White Men
%BF > .20 Segal et al. (1988)
*/
static PyObject * py_ffm_adult_male_obese(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double age;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "ddddd", &height, &weight, &age, &resistance, &reactance))
        	return NULL;
	result = ffm_adult_male_obese(height, weight, age, resistance, reactance);
	return Py_BuildValue("d", result);
}

/*
American Indian, black, Hispanic, and White Women
%BF > .30 Segal et al. (1988)
*/
static PyObject * py_ffm_adult_female_obese(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double age;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "ddddd", &height, &weight, &age, &resistance, &reactance))
        	return NULL;
	result = ffm_adult_female_obese(height, weight, age, resistance, reactance);
	return Py_BuildValue("d", result);
}

/*
Male athletes 19-40 years
Oppliger et al. (1991)
*/
static PyObject * py_ffm_adult_male_athlete(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &height, &weight, &resistance, &reactance))
        	return NULL;
	result = ffm_adult_female_athlete(height, weight, resistance, reactance);
	return Py_BuildValue("d", result);
}

/*
Female athletes 18-27 years
Fornetti et al. (1999)
*/
static PyObject * py_ffm_adult_female_athlete(PyObject *self, PyObject *args) {
	double height;
	double weight;
	double resistance;
	double reactance;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &height, &weight, &resistance, &reactance))
        	return NULL;
	result = ffm_adult_female_athlete(height, weight, resistance, reactance);
	return Py_BuildValue("d", result);
}


static PyMethodDef MassMethods[] = {
	{"ffm_child", py_ffm_child, METH_VARARGS, "Estimate fat-free mass in white boys and girls, 8-15 years old"},
	{"ffm_adolescent", py_ffm_adolescent, METH_VARARGS, "Estimate fat-free mass in white boys and girls, 10-19 years"},
	{"ffm_adult_male_lean", py_ffm_adult_male_lean, METH_VARARGS, "Estimate fat-free mass in lean American Indian, black, Hispanic, and White men"},
	{"ffm_adult_female_lean", py_ffm_adult_female_lean, METH_VARARGS, "Estimate fat-free mass in lean American Indian, black, Hispanic, and White women"},

	{"ffm_adult_male_obese", py_ffm_adult_male_obese, METH_VARARGS, "Estimate fat-free mass in obese American Indian, black, Hispanic, and White men"},
	{"ffm_adult_female_obese", py_ffm_adult_female_obese, METH_VARARGS, "Estimate fat-free mass in obese American Indian, black, Hispanic, and White women"},

	{"ffm_adult_male_athlete", py_ffm_adult_male_athlete, METH_VARARGS, "Estimate fat-free mass in male athletes 19-40 years"},
	{"ffm_adult_female_athlete", py_ffm_adult_female_athlete, METH_VARARGS, "Estimate fat-free mass in female athletes 18-27 years"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initmass(void)
{
    (void) Py_InitModule("mass", MassMethods);
}
