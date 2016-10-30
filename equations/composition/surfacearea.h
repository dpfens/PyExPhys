#include <stdio.h>
#include <math.h>

/*
@param {Number} height in cm
@param {Number} weight in grams
@returns {Number} surface area in meters^2
*/
double boyd(double height, double weight) {
    return 0.03330 * pow(weight,(0.7285-0.0188*log(weight)))*pow(height,0.3);
}

/*
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double costeff(double weight) {
    return (4*weight+7)/(90+weight);
}

/*
@param {Number} height in cm
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double dubois(double height, double weight) {
    return 0.0087184 * pow(weight,0.425) * pow(height,0.725);
}

/*
@param {Number} height in cm
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double fujimoto(double height, double weight) {
    return 0.008883 * pow(weight, 0.444) * pow(height, 0.663);
}

/*
@param {Number} height in cm
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double gehangeorge(double height, double weight) {
    return 0.0235 * pow(weight, 0.51456) * pow(height, 0.42246);
}

/*
@param {Number} height in cm
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double haycock(double height, double weight) {
    return 0.024265 * pow(weight, 0.5378) * pow(height, 0.3964);
}

/*
@param {Number} height in m
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double mosteller(double height, double weight) {
    return sqrt(weight*height)/60;
}

/*
@param {Number} height in cm
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double shuterAslani(double height, double weight) {
  return 0.00949 * pow(weight, 0.441) * pow(height, 0.655);
}

/*
@param {Number} height in cm
@param {Number} weight in kg
@returns {Number} surface area in meters^2
*/
double tahahira(double height, double weight) {
    return 0.007241 * pow(weight, 0.425) * pow(height,0.725);
}
