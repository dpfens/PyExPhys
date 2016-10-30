#include <stdio.h>
#include <math.h>

/*
Fat Free Mass (FFM)
height in cm
weight in kg
resistance, reactance in ohms
*/

/*
White boys and girls, 8-15 years
Lohman(1992)
*/
double ffm_child(double height, double weight, double resistance, double reactance) {
    return (0.62*(pow(height,2)/resistance)) + (0.21*weight) + (0.1*reactance) + 4.2; 
}

/*
White boys and girls, 10-19 years
Houtkooper e al. (1992)
*/
double ffm_adolescent(double height, double weight, double resistance, double reactance) {
    return (0.61*(pow(height,2)/resistance)) + (0.25*weight) + 1.31;
}

/*
American Indian, black, Hispanic, and White Men
%BF < .20 Segal et al. (1988)
*/
double ffm_adult_male_lean(double height, double weight, double age, double resistance, double reactance) {
    return (0.00066360*pow(height,2)) - (0.02117 * resistance) + (0.62854*weight) - (0.12380 * age) + 9.33285;
}


/*
American Indian, black, Hispanic, and White Women
%BF < .30 Segal et al. (1988)
*/

double ffm_adult_female_lean(double height, double weight, double resistance, double reactance) {
    return (0.000646*pow(height,2)) - (0.014 * resistance) + (0.421*weight) + 10.4;
}


/*
American Indian, black, Hispanic, and White Men
%BF > .20 Segal et al. (1988)
*/
double ffm_adult_male_obese(double height, double weight, double age, double resistance, double reactance) {
    return (0.00088580*pow(height,2)) - (0.02999 * resistance) + (0.42688*weight) - (0.07002 * age) + 14.52435;
}

/*
American Indian, black, Hispanic, and White Women
%BF > .30 Segal et al. (1988)
*/
double ffm_adult_female_obese(double height, double weight, double age, double resistance, double reactance) {
    return (0.00091186*pow(height,2)) - (0.1466 * resistance) + (0.29990*weight) - (0.07012 * age) + 9.37938;
}

/*
Male athletes 19-40 years
Oppliger et al. (1991)
*/
double ffm_adult_male_athlete(double height, double weight, double resistance, double reactance) {
    return (0.186*(pow(height,2)/resistance)) + (0.701*weight) + 1.949;
}

/*
Female athletes 18-27 years
Fornetti et al. (1999)
*/
double ffm_adult_female_athlete(double height, double weight, double resistance, double reactance) {
    return (0.282*height) + (0.415*weight) - (0.037*resistance) + (0.096*reactance) - 9.734;
}
