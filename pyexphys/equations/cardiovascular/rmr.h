#include <stdio.h>
#include <math.h>

/*
	Revised Harris-Benedict BMR Equations
	return calories/day
*/
double revisedHbMale(double weight, double height, double age) {
	return (88.4 + 13.4 * weight) + (4.8 * height) - (5.68 * age);
}

double revisedHbFemale(double weight, double height, double age) {
	return (447.6 + 9.25 * weight ) + (3.10 * height) - (4.33 * age);
}


/*
	Mifflin St Jeor
	returns calories/day
*/
double msjMale(double weight, double height, double age) {
	return (9.99 * weight + 6.25 * height - 4.92 * age + 5);
}

double msjFemale(double weight, double height, double age) {
	return (9.99 * weight + 6.25 * height - 4.92 * age - 151);
}

/*
	Katch-McArdle
	return calories/day
*/
double kma(double lbm) {
	return 370 + (21.6 * lbm);
}

/*
	Cunningham
	return calories/day
*/
double cunningham(double lbm) {
	return 500 + (22 * lbm);
}
