#include <Python.h>
#include "hr.h"


static PyObject * py_hr_zones(PyObject *self, PyObject *args) {
	PyObject * dict = PyDict_New();
	double max_hr;

	PyObject * low_intensity_dict = PyDict_New();
	double low_intensity_min;
	double low_intensity_max;

	PyObject * weight_control_dict = PyDict_New();
	double weight_control_min;
	double weight_control_max;

	PyObject * aerobic_zone_dict = PyDict_New();
	double aerobic_zone_min;
	double aerobic_zone_max;

	PyObject * anaerobic_zone_dict = PyDict_New();
	double anaerobic_zone_min;
	double anaerobic_zone_max;

	PyObject * redline_dict = PyDict_New();
	double redline_min;
	double redline_max;

	if (!PyArg_ParseTuple(args, "d", &max_hr))
        	return NULL;

	if(!max_hr) { Py_RETURN_NONE; };

	low_intensity_min = 0.5 * max_hr;
	low_intensity_max = 0.6 * max_hr;
	PyDict_SetItemString(low_intensity_dict, "min", Py_BuildValue("d", low_intensity_min) );
	PyDict_SetItemString(low_intensity_dict, "max", Py_BuildValue("d", low_intensity_max) );
	PyDict_SetItemString(dict, "low", low_intensity_dict);

	weight_control_min = low_intensity_max;
	weight_control_max = 0.7 * max_hr;
	PyDict_SetItemString(weight_control_dict, "min", Py_BuildValue("d", weight_control_min) );
	PyDict_SetItemString(weight_control_dict, "max", Py_BuildValue("d", weight_control_max) );
	PyDict_SetItemString(dict, "weight_control", weight_control_dict);

	aerobic_zone_min = weight_control_max;
	aerobic_zone_max = 0.8 * max_hr;
	PyDict_SetItemString(aerobic_zone_dict, "min", Py_BuildValue("d", aerobic_zone_min) );
	PyDict_SetItemString(aerobic_zone_dict, "max", Py_BuildValue("d", aerobic_zone_max) );
	PyDict_SetItemString(dict, "aerobic", aerobic_zone_dict);

	anaerobic_zone_min = aerobic_zone_max;
	anaerobic_zone_max = 0.9 * max_hr;
	PyDict_SetItemString(anaerobic_zone_dict, "min", Py_BuildValue("d", anaerobic_zone_min) );
	PyDict_SetItemString(anaerobic_zone_dict, "max", Py_BuildValue("d", anaerobic_zone_max) );
	PyDict_SetItemString(dict, "anaerobic", anaerobic_zone_dict);

	redline_min = aerobic_zone_max;
	redline_max = max_hr;
	PyDict_SetItemString(redline_dict, "min", Py_BuildValue("d", redline_min) );
	PyDict_SetItemString(redline_dict, "max",Py_BuildValue("d", redline_max) );
	PyDict_SetItemString(dict, "redline", redline_dict);

	return dict;
}

static PyObject * py_hr_max(PyObject *self, PyObject *args) {
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "d", &age))
        	return NULL;
	result = hr_max(age);
	return Py_BuildValue("d", result);
}

static PyObject * py_hr_max_gellish(PyObject *self, PyObject *args) {
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "d", &age))
        	return NULL;
	result = maxGellish(age);
	return Py_BuildValue("d", result);
}


static PyObject * py_mean_arterial_pressure(PyObject *self, PyObject *args) {
	double diastolic_bp;
	double systolic_bp;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &diastolic_bp, &systolic_bp))
		return NULL;
	result = mean_arterial_pressure(diastolic_bp, systolic_bp);
	return Py_BuildValue("d", result);
}

/*
Target heart rate
ACSM (2010) recommendation using 40% to 85% Heart Rate Reserve (HRR) for intensity

intensity as a relative exercise intensity (10% = 0.10)
rest is resting heart rate in BPM
max is maximum heart rate in BPM
*/
static PyObject * py_target_hr(PyObject *self, PyObject *args) {
	double intensity;
	double rest;
	double max;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &intensity, &rest, &max))
        	return NULL;
	result = target_hr(intensity, rest, max);
	return Py_BuildValue("d", result);
}

/*
Residual Volume formulas
*/
static PyObject * py_rv_berglund(PyObject *self, PyObject *args) {
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &age))
        	return NULL;
	result = rv_berglund(height, age);
	return Py_BuildValue("d", result);
}

static PyObject * py_rv_boren(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;
	result = rv_boren(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * py_rv_goldman(PyObject *self, PyObject *args) {
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &height, &age))
        	return NULL;
	result = rv_goldman(height, age);
	return Py_BuildValue("d", result);

}

static PyObject * py_rv_obrien_female(PyObject *self, PyObject *args) {
	double height;
	double age;
	double bsa;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &height, &age, &bsa))
        	return NULL;
	result = rv_obrien_female(height, age, bsa);
	return Py_BuildValue("d", result);
}


static PyMethodDef HRMethods[] = {
	{"hr_zones", py_hr_zones, METH_VARARGS, "Estimate heart rate zones"},
	{"hr_max", py_hr_max, METH_VARARGS, "Estimate heart rate max based on age"},
	{"hr_max_gellish", py_hr_max_gellish, METH_VARARGS, "Estimate heart rate max based on age (Gellish et al. 2007)"},
	{"target_hr", py_target_hr, METH_VARARGS, "Calculate target heart rate"},
	{"mean_arterial_pressure", py_mean_arterial_pressure, METH_VARARGS, "Calculate mean arterial pressure based on diastolic and systolic blood pressures"},
	{"rv_berglund", py_rv_berglund, METH_VARARGS, "Estimate residual volume based on Berglund"},
	{"rv_boren", py_rv_boren, METH_VARARGS, "Estimate residual volume based on Boren"},
	{"rv_goldman", py_rv_goldman, METH_VARARGS, "Estimate residual volume based on Goldman"},
	{"obrien_female", py_rv_obrien_female, METH_VARARGS, "Estimate residual volume in females based on O'Brien"},

	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC inithr(void)
{
	(void) Py_InitModule("hr", HRMethods);
}
