#include <Python.h>
#include "rm.h"


/*
1-RM Formula
Brzycki Formula
*/
static PyObject * pyBrzycki(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = brzycki(reps, weight);
	return Py_BuildValue("d", result);
}


/*
1-RM Formula
Epley Formula
*/
static PyObject * pyEpley(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = epley(reps, weight);
	return Py_BuildValue("d", result);
}

/*
1-RM Formula
Lander Formula
*/
static PyObject * pyLander(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = lander(reps, weight);
	return Py_BuildValue("d", result);
}


/*
1-RM Formula
Lombardi Formula
*/
static PyObject * pyLombardi(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = lombardi(reps, weight);
	return Py_BuildValue("d", result);
}


/*
1-RM Formula
Mayhew Formula
*/
static PyObject * pyMayhew(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = mayhew(reps, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyMayhewFootball(PyObject *self, PyObject *args) {
	double reps;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps))
        	return NULL;

        result = mayhewFootball(reps);
	return Py_BuildValue("d", result);
}


/*
1-RM Formula
O'Connor Formula
*/
static PyObject * pyOconnor(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = oconnor(reps, weight);
	return Py_BuildValue("d", result);
}


/*
1-RM Formula
Wathen Formula
*/
static PyObject * pyWathen(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = wathen(reps, weight);
	return Py_BuildValue("d", result);
}


/*
1-RM Formula
Based on number of repetitions to fatigue in one set
reps must not exceed 10
weight is the weight lifted in lb
*/
static PyObject * pyFatigueRepMap(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = fatigueRepMap(reps, weight);
	return Py_BuildValue("d", result);
}

/*
Based on the number of repetitions to fatigue obtained in two submaximal sets so long as number of reps is under 10
weight1 and weight2 must be of same unit (kg or lb)
*/
static PyObject * pyTwoSetMax(PyObject *self, PyObject *args) {
	double rep1;
	double weight1;
	double rep2;
	double weight2;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &rep1, &weight1, &rep2, &weight2))
        	return NULL;

        result = twoSetMax(rep1, weight1, rep2, weight2);
	return Py_BuildValue("d", result);
}

/*
Relative Strength
rm is 1-Rep Maximum
weight is the body mass of the individual
rm and weight must be of the same unit (kg or lbs)
*/
static PyObject * pyRelativeStrength(PyObject *self, PyObject *args) {
	double rm;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &rm, &weight))
        	return NULL;

        result = relativeStrength(rm, weight);
	return Py_BuildValue("d", result);
}


/*
gender-specific 1-RM Formula for Younger adults (22 - 36 years old)
Kim, Mayhew, and Peterson (2002)
return value in kg
*/
static PyObject * pyYmcaUpperBodyRepMaxMale(PyObject *self, PyObject *args) {
	double reps;
	double result;
	if (!PyArg_ParseTuple(args, "d", &reps))
        	return NULL;

        result = ymcaUpperBodyRepMaxMale(reps);
	return Py_BuildValue("d", result);
}

/*
gender-specific 1-RM Formula for Younger adults (22 - 36 years old)
Kim, Mayhew, and Peterson (2002)
return value in kg
*/
static PyObject * pyYmcaUpperBodyRepMaxFemale(PyObject *self, PyObject *args) {
	double reps;
	double result;
	if (!PyArg_ParseTuple(args, "d", &reps))
        	return NULL;

        result = ymcaUpperBodyRepMaxFemale(reps);
	return Py_BuildValue("d", result);
}


/*
Middle Age (40-50 years old) 1-RM
Kuramoto & Payne (1995)
*/
static PyObject * pyFemaleMiddleAgeRepMax(PyObject *self, PyObject *args) {
	double age;
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &age, &reps, &weight))
        	return NULL;

        result = femaleMiddleAgeRepMax(age, reps, weight);
	return Py_BuildValue("d", result);
}


/*
Older adult (60-70 years old) 1-RM
Kuramoto & Payne (1995)
*/
static PyObject * pyFemaleOlderRepMax(PyObject *self, PyObject *args) {
	double age;
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &age, &reps, &weight))
        	return NULL;

        result = femaleOlderRepMax(age, reps, weight);
	return Py_BuildValue("d", result);
}

static PyObject * pyFemaleHipRepMax(PyObject *self, PyObject *args) {
	double reps;
	double weight;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &reps, &weight))
        	return NULL;

        result = femaleHipRepMax(reps, weight);
	return Py_BuildValue("d", result);
}


static PyMethodDef RMMethods[] = {
	{"brzycki", pyBrzycki, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set"},
	{"epley", pyEpley, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set."},
	{"lander", pyLander, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set"},
	{"lombardi", pyLombardi, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set"},
	{"mayhew", pyMayhew, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set"},
	{"mayhewFootball", pyMayhewFootball, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set"},

	{"oconnor", pyOconnor, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set"},
	{"wathen", pyWathen, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set"},
	{"fatigue_rep_map", pyFatigueRepMap, METH_VARARGS, "Estimate 1-rep-max based on number of repetitions to fatigue in one set. Reps must not exceed 10"},
	{"two_set_max", pyTwoSetMax, METH_VARARGS, "Estimate 1-rep-max based on the number of repetitions to fatigue obtained in two submaximal sets. Number of reps is under 10"},

	{"relative_strength", pyRelativeStrength, METH_VARARGS, "Estimate relative strength"},

	{"ymca_upper_body_rep_max_male", pyYmcaUpperBodyRepMaxMale, METH_VARARGS, "Estimate 1-rep-max. For use in younger adult men (22 - 36 years old)"},
	{"ymca_upper_body_rep_max_female", pyYmcaUpperBodyRepMaxFemale, METH_VARARGS, "Estimate 1-rep-max. For use in younger adult women (22 - 36 years old)"},

	{"female_middle_age_rep_max", pyFemaleMiddleAgeRepMax, METH_VARARGS, "Estimate 1-rep-max. For use in middle-aged women (40-50 years old)"},
	{"female_older_rep_max", pyFemaleOlderRepMax, METH_VARARGS, "Estimate 1-rep-max. For use in older adult women (60-70 years old)"},
	{"female_hip_rep_max", pyFemaleHipRepMax, METH_VARARGS, "Estimate 1-rep-max. For use in adult women"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC initrm(void)
{
    (void) Py_InitModule("rm", RMMethods);
}
