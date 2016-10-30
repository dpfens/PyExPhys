#include <stdio.h>
#include <math.h>


double vo2_reserve(double max, double rest) {
	return max - rest;
}

double twelve_min_vo2(double distance) {
	return 0.0268 * distance - 11.3;
}

double mile_steady_jog_vo2(double weight, double time, double hr) {
	return 100.5 - 0.1636 * weight - 1.438 * time - 0.1928 * hr;
}

double leg_ergometry(double mass, double work) {
	return 1.8 * work/mass + 3.5;
}

double arm_ergometry(double mass, double work) {
	return 3.0 * work/mass;
}

double stepping_vo2(double height, double frequency) {
	return (frequency * 0.2) + (frequency * height * 1.8 * 1.33);
}

double stairmaster_mets(double setting) {
	return 0.556 + 7.45 * setting;
}


/*
Fox (1973) single stage cycle ergometer
single workload (900kgm/min or 150W) for 5 minutes
measure workload after 5 minutes
*/
double fox_ergometry_vo2max(double hr5) {
	return 6300.0 - ( 19.26 * hr5 );
}

/*
Single Stage Treadmill Walk VO2max
Ebbeling and colleagues (1991)
used for low-risk adults 20-59 years old
speed in mph
heart rate (hr) in bpm
*/
double treadmill_walk_vo2max_male(double age, double speed, double hr) {
	return 15.1+(21.8*speed)-(0.327*hr)-(0.263*age)+( 0.00504*(hr*age) )+(5.48*1.0);
}

/*
Single Stage Treadmill Walk VO2max
Ebbeling and colleagues (1991)
used for low-risk adults 20-59 years old
speed in mph
heart rate (hr) in bpm
*/
double treadmill_walk_vo2max_female(double age, double speed, double hr) {
	return 15.1+(21.8*speed)-(0.327*hr)-(0.263*age)+( 0.00504*(hr*age) )+(5.48*0.0);
}


/*
1 Mile Walk Test
Kline et al. (1987)
for gender field, 1 for male, 0 for female
time in minutes
*/
double mile_walk_vo2_male( double weight, double age, double time, double hr) {
	return 132.853 - 0.0769*weight - 0.3877*age + 6.315*1.0 - 3.2649*time - 0.1565*hr;
}

/*
1 Mile Walk Test
Kline et al. (1987)
for gender field, 1 for male, 0 for female
time in minutes
*/
double mile_walk_vo2_female(double weight, double age,  double time, double hr) {
	return 132.853 - 0.0769*weight - 0.3877*age + 6.315*0.0 - 3.2649*time - 0.1565*hr;
}

/*
1.5 mile run/walk
George et al. (1993)    
time in minutes
*/
double mile_half_vo2_george_male(double weight, double time) {
	return 88.02 - (0.1656*weight) - (2.76*time) + (3.716*1.0);
}

/*
1.5 mile run/walk
George et al. (1993)    
time in minutes
*/
double mile_half_vo2_george_female(double weight, double time) {
	return 88.02 - (0.1656*weight) - (2.76*time) + (3.716*0.0);
}

/*
# 1.5 mile run/walk
Larson et al (2002)
time in minutes
*/
double mile_half_vo2_larson_male(double weight, double time, double hr) {
	return 100.16 + (7.30*1.0) - (0.164*weight) - (1.273 * time) - (0.1563 * hr);
}

/*
# 1.5 mile run/walk
Larson et al (2002)
time in minutes
*/
double mile_half_vo2_larson_female(double weight, double time, double hr) {
	return 100.16 + (7.30*0.0) - (0.164*weight) - (1.273 * time) - (0.1563 * hr);
}

/*
Astrand Step Test
Marley and Linnerud (1976)
*/
double step_test_astrand(double weight, double hr) {
	return 3.744*((weight+5)/(hr-62));
}


/*
Queen's College Step Test
McArdle et al. (1972)
*/
double step_test_queenscollege(double hr) {
	return 111.33 - (0.42 * hr);
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
double treadmill_jogging_vo2max_male(double weight, double speed, double hr) {
	return 54.07-(0.1938*weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*1.0);
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
double treadmill_jogging_vo2max_female(double weight, double speed, double hr) {
	return 54.07-(0.1938*weight)-(4.47*speed)+( 0.01453*hr ) +(7.062*0.0);
}


/*
Treadmill VO2 Max (Single Stage Models)
Client must reach steady state (130 < heart rate < 150)
*/
double treadmill_submax_vo2_male_single_stage(double sm1, double hr1, double hrmax) {
	return sm1*( (hrmax-61) / (hr1-61) );
}

/*
Treadmill VO2 Max (Single Stage Models)
Client must reach steady state (130 < heart rate < 150)
*/
double treadmill_submax_vo2_female_single_stage(double sm1, double hr1, double hrmax) {
	return sm1*( (hrmax-72) / (hr1-72) );
}

/*
Treadmill VO2 Max (MultiStage Model)
Client must reach steady state (115 < heart rate < 155)
Universal to all genders
*/
double treadmill_submax_vo2_multi_stage(double sm1, double hr1, double sm2, double hr2, double hrmax) {
	double b = (sm2-sm1)/(hr2-hr1);
	return sm2+b*(hrmax-hr2);
}

/*
1.0 mile run/walk (8-17 years old)
Cureton et al. (1995)
for gender field, 1 for male, 0 for female
use with children bwtween 8 and 17 years old
time in minutes
*/
double mile_vo2_child(double weight, double height, double age, double time) {
	double bmi = (weight/pow(height/100, 2));
	return 108.94 - (8.41 * time) + 0.34 * pow(time,2) + 0.21*(age) - (0.84*bmi);
}


/*
Active & Sedentary Men
Pollock et al. (1976)
SEE = 2.50 (mL/kg/min)
*/
double vo2max_balke_male(double time) {
	return 1.444 * time + 14.99;
}

/*
Balke Protocol
Active & Sedentary Women
Pollock et al. (1982)
SEE = 2.20 (mL/kg/min)
*/
double vo2max_balke_female(double time) {
	return 1.38 * time + 5.22;
}

/*
Naughton Protocol
Male cardiac patients
Foster et a. (1983)
SEE = 2.60 (mL/kg/min)
*/
double vo2max_naughton_male(double time) {
	return (1.61*time) +3.60;
}

double vo2max_bruce_male(double time, double time2, double time3) {
	return 14.76 - 1.379*time + 0.451*time2 - 0.012*time3;
}

/*
Bruce Protocol
Active & Sedentary Women
Pollock et al. (1982)
SEE = 2.70 (mL/kg/min)
*/
double vo2max_bruce_female(double time) {
	return 4.38 * time - 3.90;
}

/*
Bruce Protocol
Cardiac patients and Elderly Persons
McConnell and Clark (1987)
SEE = 4.9 (mL/kg/min)
*/
double vo2max_elderlycardiac(double time) {
	return (2.282*time) + 8.545;
}

/*
20m Shuttle Run Test
Leger et al. (1988)
Children 8-19 years old)
*/
double shuttle_run_vo2(double age, double speed) {
	return 31.025 + (3.238*speed) - (3.248*age) + 0.1536*(age*speed);
}

/*
Daniels Gilbert Equation for VO2max
Daniels and Gilbert devised an equation for approximating VO₂ max based on tabulated race results data.
velocity in meters/minute
time in minutes
*/
double gilbert_daniels(double velocity, double time) {
	double numerator = 0.000104*pow(velocity,2)+0.182258* velocity-4.6;
	double denominator = 0.2989558*pow(M_E, -0.1932605*time)+0.1894393*pow(M_E,-0.012778*time)+0.8;
	return numerator/denominator;
}
