#include <Python.h>
#include "density.h"

/*
Body Density
*/

static PyObject * pyDbAtTLCNS(PyObject *self, PyObject *args) {
	double bd;
	double result;
	if (!PyArg_ParseTuple(args, "d", &bd))
        	return NULL;

        result = dbAtTLCNS(bd);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbChildMale(PyObject *self, PyObject *args) {
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "d", &sum))
        	return NULL;

        result = skinfoldDbChildMale(sum);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbChildFemale(PyObject *self, PyObject *args) {
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "d", &sum))
        	return NULL;

        result = skinfoldDbChildFemale(sum);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbBlackHispanicMale(PyObject *self, PyObject *args) {
	double age;
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &sum))
        	return NULL;

        result = skinfoldDbBlackHispanicMale(age, sum);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbBlackHispanicFemale(PyObject *self, PyObject *args) {
	double age;
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &sum))
        	return NULL;

        result = skinfoldDbBlackHispanicFemale(age, sum);
	return Py_BuildValue("d", result);
}


static PyObject * pySkinfoldDbWhiteMale(PyObject *self, PyObject *args) {
	double age;
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &sum))
        	return NULL;

        result = skinfoldDbWhiteMale(age, sum);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbWhiteFemaleAnorexic(PyObject *self, PyObject *args) {
	double age;
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &sum))
        	return NULL;

        result = skinfoldDbWhiteFemaleAnorexic(age, sum);
	return Py_BuildValue("d", result);
}


static PyObject * pySkinfoldDbAthleteMale(PyObject *self, PyObject *args) {
	double age;
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &sum))
        	return NULL;

        result = skinfoldDbAthleteMale(age, sum);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbAthleteFemale(PyObject *self, PyObject *args) {
	double age;
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &sum))
        	return NULL;

        result = skinfoldDbAthleteFemale(age, sum);
	return Py_BuildValue("d", result);
}


static PyObject * pySkinfoldDbCollegiateAthleteBlackMale(PyObject *self, PyObject *args) {
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "d", &sum))
        	return NULL;

        result = skinfoldDbCollegiateAthleteBlackMale(sum);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbCollegiateAthleteBlackFemale(PyObject *self, PyObject *args) {
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "d", &sum))
        	return NULL;

        result = skinfoldDbCollegiateAthleteBlackFemale(sum);
	return Py_BuildValue("d", result);
}


static PyObject * pySkinfoldDbCollegiateAthleteWhiteMale(PyObject *self, PyObject *args) {
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "d", &sum))
        	return NULL;

        result = skinfoldDbCollegiateAthleteWhiteMale(sum);
	return Py_BuildValue("d", result);
}

static PyObject * pySkinfoldDbCollegiateAthleteWhiteFemale(PyObject *self, PyObject *args) {
	double sum;
	double result;
	if (!PyArg_ParseTuple(args, "d", &sum))
        	return NULL;

        result = skinfoldDbCollegiateAthleteWhiteFemale(sum);
	return Py_BuildValue("d", result);
}

/*
Body Volume
uww = underwater weight
rb = residual volume in mL
gv = volume of air in gastrointestinal tract(default: 100mL)
*/

static PyObject * pyBodyVol(PyObject *self, PyObject *args) {
	double weight;
	double uvw;
	double rv;
	double gv;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &weight, &uvw, &rv, &gv))
        	return NULL;

        result = bodyVol(weight, uvw, rv, gv);
	return Py_BuildValue("d", result);
}

/*
Body fat percentage
Population-specific Formulas for converting Body Density (Db) to Percent Body Fat (%BF)
*/

static PyObject * pyBrozekBf(PyObject *self, PyObject *args) {
	double bd;
	double result;
	if (!PyArg_ParseTuple(args, "d", &bd))
        	return NULL;

        result = brozekBf(bd);
	return Py_BuildValue("d", result);
}

static PyObject * pySiri(PyObject *self, PyObject *args) {
	double bd;
	double result;
	if (!PyArg_ParseTuple(args, "d", &bd))
        	return NULL;

        result = siri(bd);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildMaleBmiToBf(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childMaleBmiToBf(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyChildFemaleBmiToBf(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = childFemaleBmiToBf(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultMaleBmiToBf(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultMaleBmiToBf(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyAdultFemaleBmiToBf(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &height, &age))
        	return NULL;

        result = adultFemaleBmiToBf(weight, height, age);
	return Py_BuildValue("d", result);
}

static PyObject * pyWaistBFMale(PyObject *self, PyObject *args) {
	double weight;
	double waist;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &waist))
        	return NULL;

        result = waistBFMale(weight, waist);
	return Py_BuildValue("d", result);
}

static PyObject * pyWaistBFFemale(PyObject *self, PyObject *args) {
	double weight;
	double waist;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &waist))
        	return NULL;

        result = waistBFFemale(weight, waist);
	return Py_BuildValue("d", result);
}


static PyMethodDef DensityMethods[] = {
	{"dbAtTLCNS", pyDbAtTLCNS, METH_VARARGS, "Body density in total TLCNS."},
	{"skinfoldDbChildMale", pySkinfoldDbChildMale, METH_VARARGS, "Estimate body density using skinfold test. For use with male children"},
	{"skinfoldDbChildFemale", pySkinfoldDbChildFemale, METH_VARARGS, "Estimate body density using skinfold test. For use with female children"},

	{"skinfoldDbBlackHispanicMale", pySkinfoldDbBlackHispanicMale, METH_VARARGS, "Estimate body density using skinfold test. For use with black or hispanic men"},
	{"skinfoldDbBlackHispanicFemale", pySkinfoldDbBlackHispanicFemale, METH_VARARGS, "Estimate body density using skinfold test. For use with black or hispanic women"},

	{"skinfoldDbWhiteMale", pySkinfoldDbWhiteMale, METH_VARARGS, "Estimate body density using skinfold test. For use with white men"},
	{"skinfoldDbWhiteFemaleAnorexic", pySkinfoldDbWhiteFemaleAnorexic, METH_VARARGS, "Estimate body density using skinfold test. For use with white women"},

	{"skinfoldDbAthleteMale", pySkinfoldDbAthleteMale, METH_VARARGS, "Estimate body density using skinfold test. For use with adult male athletes"},
	{"skinfoldDbAthleteFemale", pySkinfoldDbAthleteFemale, METH_VARARGS, "Estimate body density using skinfold test. For use with adult female athletes"},

	{"skinfoldDbCollegiateAthleteBlackMale", pySkinfoldDbCollegiateAthleteBlackMale, METH_VARARGS, "Estimate body density using skinfold test. For use with college-aged black male athletes"},
	{"skinfoldDbCollegiateAthleteBlackFemale", pySkinfoldDbCollegiateAthleteBlackFemale, METH_VARARGS, "Estimate body density using skinfold test. For use with college-aged black female athletes"},

	{"skinfoldDbCollegiateAthleteWhiteMale", pySkinfoldDbCollegiateAthleteWhiteMale, METH_VARARGS, "Estimate body density using skinfold test. For use with college-aged white male athletes"},
	{"skinfoldDbCollegiateAthleteWhiteFemale", pySkinfoldDbCollegiateAthleteWhiteFemale, METH_VARARGS, "Estimate body density using skinfold test. For use with college-aged white female athletes"},

	{"body_vol", pyBodyVol, METH_VARARGS, "Estimate body volume using total body submersion."},
	{"brozekBf", pyBrozekBf, METH_VARARGS, "Estimate body fat percentage using Brozek formula."},
	{"siri", pySiri, METH_VARARGS, "Estimate body fat percentage using Siri formula."},
	{"childMaleBmiToBf", pyChildMaleBmiToBf, METH_VARARGS, "Estimate body fat percentage using conversion formula. For use with male children."},
	{"childFemaleBmiToBf", pyChildFemaleBmiToBf, METH_VARARGS, "Estimate body fat percentage using conversion formula. For use with female children."},

	{"adultMaleBmiToBf", pyAdultMaleBmiToBf, METH_VARARGS, "Estimate body fat percentage using conversion formula. For use with adult males."},
	{"adultFemaleBmiToBf", pyAdultFemaleBmiToBf, METH_VARARGS, "Estimate body fat percentage using conversion formula. For use with adult females."},

	{"waistBFMale", pyWaistBFMale, METH_VARARGS, "Estimate body fat percentage using conversion formula. For use with adult males."},
	{"waistBFFemale", pyWaistBFFemale, METH_VARARGS, "Estimate body fat percentage using conversion formula. For use with adult females."},


	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initdensity(void)
{
    (void) Py_InitModule("density", DensityMethods);
}
