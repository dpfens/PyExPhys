#include <stdio.h>
#include <math.h>

/*
Swain Equation for converting %HRmax to %VO2Max
hrPercentage is the percentage of maximum heart rate
returns percentage of VO2Max as decimal
*/
double percentVO2Max(double hrPercentage) {
  double convertedPercentage = hrPercentage * 100;
  double formulaResult = (convertedPercentage - 37.182) / 0.6463;
  return formulaResult / 100;
}


/*
calculate velocity at VO2Max
vO2Max in mL/(kg•min)
returns speed in km/h
*/
double vVo2Max(double vO2Max) {
  return vO2Max/3.5;
}

/*
  @param {Number} percentHR in decimal form
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} speed in km/h
*/
double hrSpeed(double percentHR, double vO2Max) {
  double vO2MaxPercent = percentVO2Max(percentHR);
  double vO2Speed =vVo2Max(vO2Max);
  return vO2MaxPercent * vO2Speed;
}

/*
  @param {Number} percentHR in decimal form
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
double hrPace(double percentHR, double vO2Max) {
  double kph = hrSpeed(percentHR, vO2Max);
  // convert kph to min/km
  return kph/60;
}

/*
  Easy / Long (E/L) pace
  @description 60-79% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
double elPace(double vO2Max) {
  return hrPace(0.7, vO2Max);
}


/*
  Marathon (M) pace
  @description 80-85% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
double mPace(double vO2Max) {
  return hrPace(0.825, vO2Max);
}

/*
  Threshold (T) pace
  @description 82-88% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
double tPace(double vO2Max) {
  return hrPace(0.85, vO2Max);
}

/*
  Interval (I) pace
  @description 97-100% of HRmax,used for recovery runs, warm-up, cool-down and long runs.
  @param {Number} vO2Max in mL/(kg•min)
  @returns {Number} pace in min/mile
*/
double iPace(double vO2Max) {
  return hrPace(1, vO2Max);
}
