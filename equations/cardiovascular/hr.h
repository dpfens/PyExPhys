#include <stdio.h>
#include <math.h>

/*
For use with older adults
*/
double hr_max(double age) {
	return 208.0 - (0.7 * age);
}

/*
Fox(1971)
@description Recommended for use with older adults
@params {Number} age in years
@returns {Number} max heart rate in bpm
*/
double maxFox(double age) {
	return 208.0 - (0.7 * age);
}

/*
Gellish (2007)
@description For use on men and women participants in an adult fitness program with broad range of age and fitness levels
@see http://www.myfitnesspal.com/blog/mmmaddox/view/american-college-of-sports-medicine-american-heart-association-training-recommendations-254928
@params {Number} age in years
@returns {Number} max heart rate in bpm
*/
double maxGellish(double age) {
	return 207 - (0.7 * age);
}

/*
Astrand (1952)
@description For use on men and women ages 4 to 34 yr
@params {Number} age in years
@returns {Number} max heart rate in bpm
*/
double maxAstrand(double age) {
	return 216.6-(0.84*age);
}

/*
Tanaka (2001)
@description For use on healthy men and women
@params {Number} age in years
@returns {Number} max heart rate in bpm
*/
double maxTanaka(double age) {
	return 208-(0.7*age);
}

/*
Gulati (2010)
@description For use on asymptomatic middle aged women referred for stress testing
@params {Number} age in years
@returns {Number} max heart rate in bpm
*/
double maxGulati(double age) {
	return 206-(0.88*age);
}

double mean_arterial_pressure(double diastolic_bp, double systolic_bp) {
	return ( (2*diastolic_bp) + systolic_bp) / 3;
}

/*
Target heart rate
ACSM (2010) recommendation using 40% to 85% Heart Rate Reserve (HRR) for intensity

intensity as a relative exercise intensity (10% = 0.10)
rest is resting heart rate in BPM
max is maximum heart rate in BPM
*/
double target_hr(double intensity, int rest, int max) {
	return (double) intensity * (max - rest) + rest;
}

/*
Residual Volume formulas
*/
double rv_berglund(double height, double age) {
	return (0.0115*age) + (0.019* height) - 2.24;
}

double rv_boren(double weight, double height, double age) {
	return (0.022*age) + (0.0198*height) - (0.015*weight) - 1.54;
}

double rv_goldman(double height, double age) {
	return (0.017*age) + (0.027*height) - 3.477;
}

double rv_obrien_female(double height, double age, double bsa) {
	return (0.03*age) + (0.0387*height) - (0.73*bsa) - 4.78;
}

/*
	Wicks et al.
	http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3841054/
	@param {Number} max_hr = highest measured HR during activity
	@param {Number} resting_hr = resting HR (absolute)
*/
double mets_estimator(double max_hr, double resting_hr) {
	double hr_index = max_hr/resting_hr;
	return 6.0 * hr_index - 5;
}
