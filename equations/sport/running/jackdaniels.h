#include <stdio.h>
#include <math.h>

/*
@description a regression equation relating VO2 with running velocity. Used in conjuction with the "vO2" equation to create the Jack Daniel's VDOT tables.  Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.
Conditioning for Distance Running - the Scientific Aspects, 1978
@param {Number} VO2 in mL/kg/minute
@returns {Number} velocity in meters/minute
*/
double velocity(double vO2) {
  return 29.54 + 5.000663*vO2 - 0.007546 * pow(vO2, 2);
}

/*
@description a regression equation relating VO2 with running velocity. Used in conjuction with the "velocity" equation to create the Jack Daniel's VDOT tables.  Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.
Conditioning for Distance Running - the Scientific Aspects, 1978
@param {Number} velocity in meters/minute
@returns {Number} VO2 in mL/kg/minute
*/
double vO2(double velocity)  {
  return -4.60 + 0.182258 * velocity + 0.000104 * pow(velocity, 2);
}
/*
@description describes the percent of an individual's aerobic capacity the individual is capable of working at for how long.  Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.
Conditioning for Distance Running - the Scientific Aspects, 1978
@param {Number} time spent running in minutes
@returns {Number} VO2 percentage in decimal form
*/
double vO2Percentage(double time)  {
  return 0.8 + pow(0.1894393, -0.012778*time)+ pow(M_E, -0.1932605*time);
}
