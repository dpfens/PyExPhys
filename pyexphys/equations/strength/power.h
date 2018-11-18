#include <stdio.h>
#include <math.h>


/*
@descripion used to estimate peak power from vertical jump height.
Useful for differentiating between two athletes with similar vertical jump heights
Cross-validation against jumps from a force plate showed that the Lewis formula underestimated mean and peak power by up to 70%
@param {Number} body mass (kg)
@param {Number} jump height (meters)
@returns {Number} power (watts)
*/
double lewis(double weight, double jumpHeight) {
  return sqrt(4.9 * weight) * sqrt(jumpHeight) * 9.81;
}

/*
Harman et al. formula for peak power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
double peakPowerHarman(double weight, double jumpHeight) {
  return 61.9*jumpHeight + 36*weight + 1822;
}

/*
Harman et al. formula for mean power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
double meanPowerHarman(double weight, double double jumpHeight) {
  return 21.1 *jumpHeight + 2.3*weight + 1393;
}

/*
Johnson and Bahamonde formula for peak power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} body height (centimeters)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
double peakPowerJB(double weight, double height, double jumpHeight) {
  double height_cm = height * 100;
  return 78.6*jumpHeight +60.3*weight + 15.3*height_cm + 1308;
}

/*
Johnson and Bahamonde formula for mean power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} body height (centimeters)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
double meanPowerJB(double weight, double height, double jumpHeight) {
  double height_cm = height * 100;
  return 43.8*jumpHeight + 32.7*weight - 16.8*height_cm + 431;
}

/*
Sayers et al. formula for mean power in a vertical jump
@description
@param {Number} body mass (kg)
@param {Number} jump height (centimeters)
@returns {Number} power (watts)
*/
double peakPowerSayer(double weight, double jumpHeight) {
  return 60.7*jumpHeight + 45.3*weight - 2055;
}

/*
Margaria-Kalamen Test
@description measures power by assessing
the athlete’s ability to ascend stairs as rapidly as possible.
It has been used, albeit sparingly, to assess an athlete since its inception in the 1960s
@param {Number} body mass (kg)
@param {Number} vertical height (meters)
@returns {Number} power (watts)
*/
double powerMK(double weight, double verticalHeight, double time) {
  return (weight * (verticalHeight/time)) * 9.81;
}
