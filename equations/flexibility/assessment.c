#include <Python.h>

static PyMethodDef AssessmentMethods[] = {
	{},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initassessment(void)
{
	(void) Py_InitModule("assessment", AssessmentMethods);
}
