#include <stdio.h>
#include <math.h>


/*
Raxter et al. (2006) noted a discrepancy between the average soft tissue correction
factor of Fully’s 1956 sample (10.5 cm) and their own (12.4 cm). They devised new
equations to correct for this soft tissue factor discrepancy, as well as for the gradual
effects of age on stature.
*/
double stature_universal(double age, double skeletal_height) {
	return 1.009 * skeletal_height -0.0426 * age + 12.1;
}


/*
Formulas obtained from https://digital.library.txstate.edu/bitstream/handle/10877/4055/fulltext.pdf
Regression Formulae Using the Femur (Trotter and Gleser 1952, 1958)
*/

double stature_american_white_male(double femur) {
	return 2.32 * femur + 65.53;
}

double stature_american_white_female(double femur) {
	return 2.47 * femur + 54.10;
}

double stature_american_black_male(double femur) {
	return 2.10 * femur + 72.22;
}

double stature_american_black_female(double femur) {
	return 2.28 * femur + 59.76;
}
