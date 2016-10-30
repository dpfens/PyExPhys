#include <stdio.h>
#include <math.h>

/*
1-RM Formula
Brzycki Formula
returns a slightly lower estimated maximum than Epley when reps < 10
*/
double brzycki(double reps, double weight) {
    return weight/(1.0278-(0.0278 * reps));
}

/*
1-RM Formula
Epley Formula (1985)
returns a slightly higher estimated maximum than Brzycki when reps < 10
*/
double epley(double reps, double weight) {
    return (weight * reps * 0.033)+weight;
}

/*
1-RM Formula
Lander Formula
*/

double lander(double reps, double weight) {
    return weight/(1.013 - (0.0267123 * reps) );
}

/*
1-RM Formula
Lombardi Formula
*/

double lombardi(double reps, double weight) {
    return weight*pow(reps,0.10);
}

/*
1-RM Formula
Mayhew et al. Formula
*/

double mayhew(double reps, double weight) {
    return (100*weight) / ( (52.2+41.9) * pow(M_E,-0.055*reps) );
}

/*
1-RM Formula
Mayhew et al. Formula used in college football players
@param {Number} reps
@returns {Number} 1RM in lb
*/
double mayhewFootball(double reps) {
    return 226.7 + 7.1*(reps);
}

/*
1-RM Formula
O'Connor et al. Formula
*/

double oconnor(double reps, double weight) {
    return weight * (1+0.025*reps);
}

/*
1-RM Formula
Wathen Formula
*/

double wathen(double reps, double weight) {
    return (100*weight) / (48.8+(53.8*pow(M_E,-0.075 * reps) ) );
}

/*
1-RM Formula
Based on number of repetitions to fatigue in one set
reps must not exceed 10
weight is the weight lifted in lb
*/
double fatigueRepMap(double reps, double weight) {
    return weight / (1.0278 - (reps * 0.0278));
}

/*
Based on the number of repetitions to fatigue obtained in two submaximal sets so long as number of reps is under 10
weight1 and weight2 must be of same unit (kg or lb)
*/
double twoSetMax(double rep1, double weight1, double rep2, double weight2) {
    return ((weight1 - weight2)/(rep2 - rep1)) * (rep1 - 1) + weight1;
}

/*
Relative Strength
rm is 1-Rep Maximum
weight is the body mass of the individual
rm and weight must be of the same unit (kg or lbs)
*/
double relativeStrength(double rm, double weight) {
    return rm / weight;
}


/*
gender-specific 1-RM Formula for Younger adults (22 - 36 years old)
Kim, Mayhew, and Peterson (2002)
return value in kg
*/
double ymcaUpperBodyRepMaxMale(double reps) {
    return (1.55 * reps) + 37.9;
}

/*
gender-specific 1-RM Formula for Younger adults (22 - 36 years old)
Kim, Mayhew, and Peterson (2002)
return value in kg
*/
double ymcaUpperBodyRepMaxFemale(double reps) {
    return (0.31 * reps) + 19.2;
}


/*
Middle Age (40-50 years old) 1-RM
Kuramoto & Payne (1995)
*/
double femaleMiddleAgeRepMax(double age, double reps, double weight) {
    return  (1.06 * weight) + (0.58 * reps) - (0.20 * age) - 3.41;
}


/*
Older adult (60-70 years old) 1-RM
Kuramoto & Payne (1995)
*/
double femaleOlderRepMax(double age, double reps, double weight) {
    return (0.92 * weight) + (0.79 * reps) - (0.20 * age) - 3.73;
}

double femaleHipRepMax(double reps, double weight) {
    return 100 * weight/(48.8+pow(53.8,(-0.075*reps) ));
}
