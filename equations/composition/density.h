#include <stdio.h>
#include <math.h>


/*
Body Density
*/

double dbAtTLCNS(double bd) {
	return 0.5829 * bd + 0.4059;
}

double skinfoldDbChildMale(double sum) {
    return (0.735*sum) + 1.0;
}

double skinfoldDbChildFemale(double sum) {
    return (0.610*sum) + 5.1;
}

double skinfoldDbBlackHispanicMale(double age, double sum) {
	return 1.112 - (0.00043499*sum) + (0.00000055*pow(sum, 2)) - (0.00028826*age);
}

double skinfoldDbBlackHispanicFemale(double age, double sum) {
	return 1.0970 - (0.00046971*sum) + (0.00000056*pow(sum, 2)) - (0.00012828*age);
}


double skinfoldDbWhiteMale(double age, double sum) {
	return  1.10938 - (0.0008267*sum) + (0.0000016*pow(sum, 2)) - (0.0002574*age);
}

double skinfoldDbWhiteFemaleAnorexic(double age, double sum) {
	return 1.0994921 - (0.0009929*sum) + (0.0000023*pow(sum, 2)) - (0.00001392*age);
}


double skinfoldDbAthleteMale(double age, double sum) {
	return 1.112 - (0.00043499*sum) + (0.00000055*pow(sum, 2)) - (0.00028826*age) ;
}

double skinfoldDbAthleteFemale(double age, double sum) {
	return 1.096095 - (0.0006952*sum) + (0.0000011*pow(sum, 2)) - (0.0000714*age);
}


double skinfoldDbCollegiateAthleteBlackMale(double sum) {
	return 8.997 + (0.2468*sum) - (6.343 * 1) - (1.998);
}

double skinfoldDbCollegiateAthleteBlackFemale(double sum) {
	return  8.997 + (0.2468*sum) - (1.998);
}


double skinfoldDbCollegiateAthleteWhiteMale(double sum) {
	return 8.997 + (0.2468*sum) - (6.343 * 1);
}

double skinfoldDbCollegiateAthleteWhiteFemale(double sum) {
	return 8.997 + (0.2468*sum);
}

/*
Body Volume
uww = underwater weight
rb = residual volume in mL
gv = volume of air in gastrointestinal tract(default: 100mL)
*/

double bodyVol(double weight, double uww, double rv, double gv) {
    double waterDensity = 1;
    return ((weight - uww)/ waterDensity) - (rv - gv);
}

/*
Body fat percentage
Population-specific Formulas for converting Body Density (Db) to Percent Body Fat (%BF)
*/

double brozekBf(double bd) {
    return (4.570/bd)-4.142;
}

double siri(double bd) {
    return (4.95/bd)-4.50;
}

double childMaleBmiToBf(double weight, double height, double age) {
    double bmi = (weight/pow(height/100, 2));
    return ((1.51*bmi) - (0.70*age) - (3.6) + 1.4) / 100;
}

double childFemaleBmiToBf(double weight, double height, double age) {
    double bmi = (weight/pow(height/100, 2));
    return  ((1.51*bmi) - (0.70*age) + 1.4) / 100;
}

double adultMaleBmiToBf(double weight, double height, double age) {
    double bmi = (weight/pow(height/100, 2));
    return ((1.20*bmi) - (0.23*age) - (10.8) - 5.4) / 100;
}

double adultFemaleBmiToBf(double weight, double height, double age) {
    double bmi = (weight/pow(height/100, 2));
    return ((1.20*bmi) - (0.23*age) - 5.4) / 100;
}

/*
@param {Number} weight in lb
@param {Number} waist in inches
@returns percent body fat
*/
double waistBFMale(double weight, double waist) {
	double weightLb = weight * 2.2;
	return 100*(-98.42 + 4.15*waist - 0.082*weightLb)/weightLb;
}
/*
@param {Number} weight in lb
@param {Number} waist in inches
@returns percent body fat
*/
double waistBFFemale(double weight, double waist) {
	double weightLb = weight * 2.2;
	return 100*(-76.76 + 4.15*waist - 0.082*weightLb)/weightLb;
}
