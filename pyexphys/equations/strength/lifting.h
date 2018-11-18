#include <stdio.h>
#include <math.h>

/*
@param {Number} weight lifted in kg
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
double oCarroll(double bodyWeight, double weightLifted) {
	return weightLifted/pow(bodyWeight-35, 1/3);
}

/*
@description For use in non-power lifts. To compare the performances of lifters of different bodymass, simply substitute each lifter's bodymass in the relevant equations above to calculate the Total (or lift) expected for a top world class lifter. Then divide each lifter's actual Total by this value to obtain the percentage of the world class lift achieved by each lifter.
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
double siffWeightLiftingMale(double bodyWeight) {
	double a = 512.245;
	double b = 146230;
	double c = 1.605;
	return a-b*pow(bodyWeight, -c);
}

/*
@description For use in non-power lifts. To compare the performances of lifters of different bodymass, simply substitute each lifter's bodymass in the relevant equations above to calculate the Total (or lift) expected for a top world class lifter. Then divide each lifter's actual Total by this value to obtain the percentage of the world class lift achieved by each lifter.
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
double siffWeightLiftingFemale(double bodyWeight) {
	double a = 943.063;
	double b = 0.05142 ;
	double c = 257.314;
	return c-a*pow(M_E, -b*bodyWeight);
}

/*
@description For use in power lifts by men  To compare the performances of lifters of different bodymass, simply substitute each lifter's bodymass in the relevant equations above to calculate the Total (or lift) expected for a top world class lifter. Then divide each lifter's actual Total by this value to obtain the percentage of the world class lift achieved by each lifter.
@param {Number} weight in kg
@return {Number} adjusted for weight of lifter
*/
double siffPowerLiftingMale(double bodyWeight) {
	double a = 1270.4;
	double b = 172970;
	double c = 1.3925;
	return a-b*pow(bodyWeight, -c);
}

/*
	@param {Number} obtainedTotal weight in kg
	@returns {Number} sinclair coefficient
*/
double sinclairMale(double body_weight, double obtained_total) {
	double coefficient_a = 0.794358141;
	double coefficient_b =  174.393;
	if(body_weight >= coefficient_b) {
		return 1.0;
	}
	double exponent = pow(  coefficient_a * log10(body_weight/coefficient_b), 2 );
	return pow(10,  exponent);
}

/*
	@param {Number} obtainedTotal weight in kg
	@returns {Number} sinclair coefficient
*/
double sinclairFemale(double body_weight, double obtained_total) {
	double coefficient_a = 0.897260740;
	double coefficient_b = 148.026;
	if(body_weight >= coefficient_b) {
		return 1.0;
	}
	double exponent = pow(  coefficient_a * log10(body_weight/coefficient_b), 2 );
	return pow(10,  exponent);
}

/*
	@param {Number} body mass in kg
	@param {Number} weightLifted in kg
	@returns {Number} wilks coefficient
*/
double wilksMale(double body_weight, double weight_lifted) {
	double coefficient;
	double a = -216.0475144;
	double b = 16.2606339;
	double c = -0.002388645;
	double d = -0.00113732;
	double e = 7.01863E-06;
	double f = -1.291E-08;
	coefficient = 500/(a + b*body_weight + c * pow(body_weight, 2) + d * pow(body_weight, 3) + e * pow(body_weight, 4) + f * pow(body_weight, 5) );
	return coefficient * weight_lifted;
}

/*
	@param {Number} body mass in kg
	@param {Number} weightLifted in kg
	@returns {Number} wilks coefficient
*/
double wilksFemale(double body_weight, double weight_lifted) {
	double coefficient;
	double a = 594.31747775582;
	double b = -27.23842536447;
	double c = 0.82112226871;
	double d = -0.00930733913;
	double e = 4.731582E-05;
	double f = -9.054E-08;
	coefficient = 500/(a + b*body_weight + c * pow(body_weight, 2) + d * pow(body_weight, 3) + e * pow(body_weight, 4) + f * pow(body_weight, 5) );
	return coefficient * weight_lifted;
}
