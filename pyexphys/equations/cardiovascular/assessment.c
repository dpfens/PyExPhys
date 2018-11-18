#include <Python.h>
#include "assessment.h"

static PyObject * py_vo2_reserve(PyObject *self, PyObject *args) {
	double max;
	double rest;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &max, &rest))
        	return NULL;
	result = vo2_reserve(max, rest);
	return Py_BuildValue("d", result);
}

static PyObject * py_twelve_min_vo2(PyObject *self, PyObject *args) {
	double distance;
	double result;
	if (!PyArg_ParseTuple(args, "d", &distance))
        	return NULL;
	result = twelve_min_vo2(distance);
	return Py_BuildValue("d", result);
}

static PyObject * py_mile_steady_jog_vo2(PyObject *self, PyObject *args) {
	double weight;
	double time;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &time, &hr))
        	return NULL;
	result = mile_steady_jog_vo2(weight, time, hr);
	return Py_BuildValue("d", result);
}

static PyObject * py_leg_ergometry(PyObject *self, PyObject *args) {
	double mass;
	double work;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &mass, &work))
        	return NULL;
	result = leg_ergometry(mass, work);
	return Py_BuildValue("d", result);
}

static PyObject * py_arm_ergometry(PyObject *self, PyObject *args) {
	double mass;
	double work;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &mass, &work))
        	return NULL;
	result = arm_ergometry(mass, work);
	return Py_BuildValue("d", result);
}

static PyObject * py_stepping_vo2(PyObject *self, PyObject *args) {
	double height;
	double frequency;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &height, &frequency))
        	return NULL;
	result = stepping_vo2(height, frequency);
	return Py_BuildValue("d", result);
}

static PyObject * py_stairmaster_mets(PyObject *self, PyObject *args) {
	double setting;
	double result;
	if (!PyArg_ParseTuple(args, "d", &setting))
        	return NULL;
	result = stairmaster_mets(setting);
	return Py_BuildValue("d", result);
}


/*
Fox (1973) single stage cycle ergometer
single workload (900kgm/min or 150W) for 5 minutes
measure workload after 5 minutes
*/
static PyObject * py_fox_ergometry_vo2max(PyObject *self, PyObject *args) {
	double hr5;
	double result;
	if (!PyArg_ParseTuple(args, "d", &hr5))
        	return NULL;
	result = fox_ergometry_vo2max(hr5);
	return Py_BuildValue("d", result);
}

/*
Single Stage Treadmill Walk VO2max
Ebbeling and colleagues (1991)
used for low-risk adults 20-59 years old
speed in mph
heart rate (hr) in bpm
*/
static PyObject * py_treadmill_walk_vo2max_male(PyObject *self, PyObject *args) {
	double age;
	double speed;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &age, &speed, &hr))
        	return NULL;
	result = treadmill_walk_vo2max_male(age, speed, hr);
	return Py_BuildValue("d", result);
}

/*
Single Stage Treadmill Walk VO2max
Ebbeling and colleagues (1991)
used for low-risk adults 20-59 years old
speed in mph
heart rate (hr) in bpm
*/
static PyObject * py_treadmill_walk_vo2max_female(PyObject *self, PyObject *args) {
	double age;
	double speed;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &age, &speed, &hr))
        	return NULL;
	result = treadmill_walk_vo2max_female(age, speed, hr);
	return Py_BuildValue("d", result);
}


/*
1 Mile Walk Test
Kline et al. (1987)
for gender field, 1 for male, 0 for female
time in minutes
*/
static PyObject * py_mile_walk_vo2_male(PyObject *self, PyObject *args) {
	double weight;
	double age;
	double speed;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &weight, &age, &speed, &hr))
        	return NULL;
	result = mile_walk_vo2_male(weight, age, speed, hr);
	return Py_BuildValue("d", result);
}

/*
1 Mile Walk Test
Kline et al. (1987)
for gender field, 1 for male, 0 for female
time in minutes
*/
static PyObject * py_mile_walk_vo2_female(PyObject *self, PyObject *args) {
	double weight;
	double age;
	double speed;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &weight, &age, &speed, &hr))
        	return NULL;
	result = mile_walk_vo2_female(weight, age, speed, hr);
	return Py_BuildValue("d", result);
}

/*
1.5 mile run/walk
George et al. (1993)    
time in minutes
*/
static PyObject * py_mile_half_vo2_george_male(PyObject *self, PyObject *args) {
	double weight;
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &time))
        	return NULL;
	result = mile_half_vo2_george_male(weight, time);
	return Py_BuildValue("d", result);
}

/*
1.5 mile run/walk
George et al. (1993)    
time in minutes
*/
static PyObject * py_mile_half_vo2_george_female(PyObject *self, PyObject *args) {
	double weight;
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &time))
        	return NULL;
	result = mile_half_vo2_george_female(weight, time);
	return Py_BuildValue("d", result);
}

/*
# 1.5 mile run/walk
Larson et al (2002)
time in minutes
*/
static PyObject * py_mile_half_vo2_larson_male(PyObject *self, PyObject *args) {
	double weight;
	double time;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &time, &hr))
        	return NULL;
	result = mile_half_vo2_larson_male(weight, time, hr);
	return Py_BuildValue("d", result);
}

/*
# 1.5 mile run/walk
Larson et al (2002)
time in minutes
*/
static PyObject * py_mile_half_vo2_larson_female(PyObject *self, PyObject *args) {
	double weight;
	double time;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &time, &hr))
        	return NULL;
	result = mile_half_vo2_larson_female(weight, time, hr);
	return Py_BuildValue("d", result);
}

/*
Astrand Step Test
Marley and Linnerud (1976)
*/
static PyObject * py_step_test_astrand(PyObject *self, PyObject *args) {
	double weight;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &weight, &hr))
        	return NULL;
	result = step_test_astrand(weight, hr);
	return Py_BuildValue("d", result);
}


/*
Queen's College Step Test
McArdle et al. (1972)
*/
static PyObject * py_step_test_queenscollege(PyObject *self, PyObject *args) {
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "d", &hr))
        	return NULL;
	result = step_test_queenscollege(hr);
	return Py_BuildValue("d", result);
}


/*
Single Stage Treadmill Jog VO2max
George et al. (1993)
used for younger adults (18 - 28 years old)
4.3 mph < speed < 7.5 mph for men
client should jog at speed for 3 minutes
hr < 180 bpm
body weight in kg
speed in mph
hr in in bpm
*/
static PyObject * py_treadmill_jogging_vo2max_male(PyObject *self, PyObject *args) {
	double weight;
	double speed;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &speed, &hr))
        	return NULL;
	result = treadmill_jogging_vo2max_male(weight, speed, hr);
	return Py_BuildValue("d", result);
}

/*
Single Stage Treadmill Jog VO2max
George et al. (1993)
used for younger adults (18 - 28 years old)
4.5mph < speed < 6.5 mph for women
client should jog at speed for 3 minutes
hr < 180 bpm
body weight in kg
speed in mph
hr in in bpm
*/
static PyObject * py_treadmill_jogging_vo2max_female(PyObject *self, PyObject *args) {
	double weight;
	double speed;
	double hr;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &weight, &speed, &hr))
        	return NULL;
	result = treadmill_jogging_vo2max_female(weight, speed, hr);
	return Py_BuildValue("d", result);
}


/*
Treadmill VO2 Max (Single Stage Models)
Client must reach steady state (130 < heart rate < 150)
*/
static PyObject * py_treadmill_submax_vo2_male_single_stage(PyObject *self, PyObject *args) {
	double sm1;
	double hr1;
	double hrmax;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &sm1, &hr1, &hrmax))
        	return NULL;
	result = treadmill_submax_vo2_male_single_stage(sm1, hr1, hrmax);
	return Py_BuildValue("d", result);
}

/*
Treadmill VO2 Max (Single Stage Models)
Client must reach steady state (130 < heart rate < 150)
*/
static PyObject * py_treadmill_submax_vo2_female_single_stage(PyObject *self, PyObject *args) {
	double sm1;
	double hr1;
	double hrmax;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &sm1, &hr1, &hrmax))
        	return NULL;
	result = treadmill_submax_vo2_female_single_stage(sm1, hr1, hrmax);
	return Py_BuildValue("d", result);
}

/*
Treadmill VO2 Max (MultiStage Model)
Client must reach steady state (115 < heart rate < 155)
Universal to all genders
*/
static PyObject * py_treadmill_submax_vo2_multi_stage(PyObject *self, PyObject *args) {
	double sm1;
	double hr1;
	double sm2;
	double hr2;
	double hrmax;
	double result;
	if (!PyArg_ParseTuple(args, "ddddd", &sm1, &hr1, &sm2, &hr2, &hrmax))
        	return NULL;
	result = treadmill_submax_vo2_multi_stage(sm1, hr1, sm2, hr2, hrmax);
	return Py_BuildValue("d", result);
}

/*
1.0 mile run/walk (8-17 years old)
Cureton et al. (1995)
for gender field, 1 for male, 0 for female
use with children bwtween 8 and 17 years old
time in minutes
*/
static PyObject * py_mile_vo2_child(PyObject *self, PyObject *args) {
	double weight;
	double height;
	double age;
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "dddd", &weight, &height, &age, &time))
        	return NULL;
	result = mile_vo2_child(weight, height, age, time);
	return Py_BuildValue("d", result);
}


/*
Active & Sedentary Men
Pollock et al. (1976)
SEE = 2.50 (mL/kg/min)
*/
static PyObject * py_vo2max_balke_male(PyObject *self, PyObject *args) {
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "d", &time))
        	return NULL;
	result = vo2max_balke_male(time);
	return Py_BuildValue("d", result);
}

/*
Balke Protocol
Active & Sedentary Women
Pollock et al. (1982)
SEE = 2.20 (mL/kg/min)
*/
static PyObject * py_vo2max_balke_female(PyObject *self, PyObject *args) {
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "d", &time))
        	return NULL;
	result = vo2max_balke_female(time);
	return Py_BuildValue("d", result);
}

/*
Naughton Protocol
Male cardiac patients
Foster et a. (1983)
SEE = 2.60 (mL/kg/min)
*/
static PyObject * py_vo2max_naughton_male(PyObject *self, PyObject *args) {
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "d", &time))
        	return NULL;
	result = vo2max_naughton_male(time);
	return Py_BuildValue("d", result);
}

static PyObject * py_vo2max_bruce_male(PyObject *self, PyObject *args) {
	double time;
	double time2;
	double time3;
	double result;
	if (!PyArg_ParseTuple(args, "ddd", &time, &time2, &time3))
        	return NULL;
	result = vo2max_bruce_male(time, time2, time3);
	return Py_BuildValue("d", result);
}

/*
Bruce Protocol
Active & Sedentary Women
Pollock et al. (1982)
SEE = 2.70 (mL/kg/min)
*/
static PyObject * py_vo2max_bruce_female(PyObject *self, PyObject *args) {
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "d", &time))
        	return NULL;
	result = vo2max_bruce_female(time);
	return Py_BuildValue("d", result);
}

/*
Bruce Protocol
Cardiac patients and Elderly Persons
McConnell and Clark (1987)
SEE = 4.9 (mL/kg/min)
*/
static PyObject * py_vo2max_elderlycardiac(PyObject *self, PyObject *args) {
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "d", &time))
        	return NULL;
	result = vo2max_elderlycardiac(time);
	return Py_BuildValue("d", result);
}

/*
20m Shuttle Run Test
Leger et al. (1988)
Children 8-19 years old)
*/
static PyObject * py_shuttle_run_vo2(PyObject *self, PyObject *args) {
	double age;
	double speed;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &age, &speed))
        	return NULL;
	result = shuttle_run_vo2(age,speed);
	return Py_BuildValue("d", result);
}


/*
Daniels Gilbert Equation for VO2max
Daniels and Gilbert devised an equation for approximating VO₂ max based on tabulated race results data.
velocity in meters/minute
time in minutes
*/
static PyObject * py_gilbert_daniels(PyObject *self, PyObject *args) {
	double velocity;
	double time;
	double result;
	if (!PyArg_ParseTuple(args, "dd", &velocity, &time))
        	return NULL;
	result = gilbert_daniels(velocity, time);
	return Py_BuildValue("d", result);
}


static PyMethodDef AssessmentMethods[] = {
	{"vo2_reserve", py_vo2_reserve, METH_VARARGS, "Estimate VO2 reserve"},
	{"twelve_min_vo2", py_twelve_min_vo2, METH_VARARGS, "Estimate VO2 based on the 12-minute VO2 test"},
	{"mile_steady_jog_vo2", py_mile_steady_jog_vo2, METH_VARARGS, "Estimate VO2 based on the mile steady jog test"},
	{"leg_ergometry", py_leg_ergometry, METH_VARARGS, "Calculate Leg Ergometry"},
	{"arm_ergometry", py_arm_ergometry, METH_VARARGS, "Calculate Arm Ergometry"},
	{"stepping_vo2", py_stepping_vo2, METH_VARARGS, "Estimate VO2 using step test"},
	{"stairmaster_mets", py_stairmaster_mets, METH_VARARGS, "Calculate METs based on setting on StairMaster"}, 
	{"fox_ergometry_vo2max", py_fox_ergometry_vo2max, METH_VARARGS, "Estimate VO2 Max using Fox Ergometry method"},
	{"treadmill_walk_vo2max_male", py_treadmill_walk_vo2max_male, METH_VARARGS, "Estimate VO2Max based on the Single Stage Treadmill Walk VO2max test used on low-risk 20-59 year old men"},
	{"treadmill_walk_vo2max_female", py_treadmill_walk_vo2max_female, METH_VARARGS, "Estimate VO2Max based on the Single Stage Treadmill Walk VO2max test used on low-risk 20-59 year old women"},
	{"mile_walk_vo2_male", py_mile_walk_vo2_male, METH_VARARGS, "Estimate VO2 using 1 Mile Walk Test in men"},
	{"mile_walk_vo2_female", py_mile_walk_vo2_female, METH_VARARGS, "Estimate VO2 using 1 Mile Walk Test in women"},
	{"mile_half_vo2_george_male", py_mile_half_vo2_george_male, METH_VARARGS, "Estimate VO2 using 1.5 Mile Walk Test in women."},
	{"mile_half_vo2_george_female", py_mile_half_vo2_george_female, METH_VARARGS, "Estimate VO2 using 1.5 Mile Walk Test in women"},
	{"mile_half_vo2_larson_male", py_mile_half_vo2_larson_male, METH_VARARGS, "Estimate VO2 using 1.5 Mile Walk Test in men"},
	{"mile_half_vo2_larson_female", py_mile_half_vo2_larson_female, METH_VARARGS, "Estimate VO2 using 1.5 Mile Walk Test in women"},
	{"step_test_astrand", py_step_test_astrand, METH_VARARGS, "Estimate VO2 using Astrand Step Test."},
	{"step_test_queenscollege", py_step_test_queenscollege, METH_VARARGS, "Estimate VO2 using Queen's College Step Test"},
	{"treadmill_jogging_vo2max_male", py_treadmill_jogging_vo2max_male, METH_VARARGS, "Estimate VO2 using Single Stage Treadmill Jog in younger men (18 - 28 years old)."},
	{"treadmill_jogging_vo2max_female", py_treadmill_jogging_vo2max_female, METH_VARARGS, "Estimate VO2 using Single Stage Treadmill Jog in younger women (18 - 28 years old)."},

	{"treadmill_submax_vo2_male_single_stage", py_treadmill_submax_vo2_male_single_stage, METH_VARARGS, "Estimate VO2 using Submax Single Stage Treadmill Jog.  Men must reach steady state (130 < heart rate < 150)"},
	{"treadmill_submax_vo2_female_single_stage", py_treadmill_submax_vo2_female_single_stage, METH_VARARGS, "Estimate VO2 using Submax Single Stage Treadmill Jog.  Women must reach steady state (130 < heart rate < 150)"},
	{"treadmill_submax_vo2_multi_stage", py_treadmill_submax_vo2_multi_stage, METH_VARARGS, "Estimate VO2 using Submax Multi-stage Treadmill Jog.  Client must reach steady state (115 < heart rate < 155). Universal to all genders"},
	{"mile_vo2_child", py_mile_vo2_child, METH_VARARGS, "Estimate VO2  in children using 1.0 mile run/walk (8-17 years old)"},
	{"vo2max_balke_male", py_vo2max_balke_male, METH_VARARGS, "Estimate VO2 using Balke Protocol.  For use in active & sedentary men"},
	{"vo2max_balke_female", py_vo2max_balke_female, METH_VARARGS, "Estimate VO2 using Balke Protocol.  For use in active & sedentary women"},
	{"vo2max_naughton_male", py_vo2max_naughton_male, METH_VARARGS, "Estimate VO2 using Naughton Protocol.  For use in male cardiac patients"},
	{"vo2max_bruce_male", py_vo2max_bruce_male, METH_VARARGS, "Estimate VO2 using Bruce Protocol.  For use in active & sedentary men"},
	{"vo2max_bruce_female", py_vo2max_bruce_female, METH_VARARGS, "Estimate VO2 using Bruce Protocol.  For use in active & sedentary women"},
	{"vo2max_elderlycardiac", py_vo2max_elderlycardiac, METH_VARARGS, "Estimate VO2 using Bruce Protocol.  For use in cardiac patients and elderly persons"},
	{"shuttle_run_vo2", py_shuttle_run_vo2, METH_VARARGS, "Estimate VO2 using 20m Shuttle Run Test. For use in children 8-19 years old"},
	{"gilbert_daniels", py_gilbert_daniels, METH_VARARGS, "Estimate VO2max based on tabulated race results data"},
	{NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initassessment(void)
{
	(void) Py_InitModule("assessment", AssessmentMethods);
}
