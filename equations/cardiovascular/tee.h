#include <stdio.h>
#include <math.h>

/*
All equations take
weight in kg
height in meters
age in years
*/


double childMaleSedentaryTee(double weight, double height, double age) {
	return 88.5 - (61.9 * age) + 1*((26.7*weight)+(903*height));
}

double childFemaleSedentaryTee(double weight, double height, double age) {
    return 135.3 - (30.8 * age) + 1*((10*weight)+(934*height));
}

double childMaleLowTee(double weight, double height, double age) {
	return 88.5 - (61.9 * age) + 1.13*((26.7*weight)+(903*height));
}

double childFemaleLowTee(double weight, double height, double age) {
    return 135.3 - (30.8 * age) + 1.16*((10*weight)+(934*height));
}

double childMaleActiveTee(double weight, double height, double age) {
	return 88.5 - (61.9 * age) + 1.26*((26.7*weight)+(903*height));
}

double childFemaleActiveTee(double weight, double height, double age) {
    return 135.3 - (30.8 * age) + 1.31*((10*weight)+(934*height));
}

double childMaleVeryActiveTee(double weight, double height, double age) {
	return 88.5 - (61.9 * age) + 1.42*((26.7* weight)+(903* height));
}

double childFemaleVeryActiveTee(double weight, double height, double age) {
    return 135.3 - (30.8 * age) + 1.56*((10*weight)+(934*height));
}



double adultMaleSedentaryTee(double weight, double height, double age) {
        return 662 - (9.53 * age) + 1*((15.9 * weight) + (540 * height));
}

double adultFemaleSedentaryTee(double weight, double height, double age) {
    return 354 - (6.91 * age) + 1*((9.36*weight)+(726*height));
}

double adultMaleLowTee(double weight, double height, double age) {
        return 662 - (9.53 * age) + 1.11*((15.9*weight)+(540*height));
}

double adultFemaleLowTee(double weight, double height, double age) {
   return 662 - (9.53 * age) + 1.12*((15.9*weight)+(540*height));
}

double adultMaleActiveTee(double weight, double height, double age) {
        return 662 - (9.53 * age) + 1.25*((15.9*weight)+(540*height)) ;
}

double adultFemaleActiveTee(double weight, double height, double age) {
    return 662 - (9.53 * age) + 1.27*((15.9*weight)+(540*height));
}

double adultMaleVeryActiveTee(double weight, double height, double age) {
        return 662 - (9.53 * age) + 1.48*((15.9*weight)+(540*height));
}

double adultFemaleVeryActiveTee(double weight, double height, double age) {
    return 662 - (9.53 * age) + 1.45*((15.9*weight)+(540*height));
}
