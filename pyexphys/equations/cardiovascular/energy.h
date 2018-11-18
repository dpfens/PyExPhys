#include <stdio.h>
#include <math.h>

/*
@description obtained from http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000960
@param {Number} percentVO2 being exercised at
@returns {Number} percentage carbohydrate contribute to energy when exercising at a given percent of VO2Max
*/
double carbohydrate(double percentVO2) {
  return 0.565973 * pow(percentVO2,2)+0.376443 * percentVO2-0.000295601;
}

/*
@description obtained from http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000960
@param {Number} percentVO2 being exercised at
@returns {Number} percentage fat contribute to energy when exercising at a given percent of VO2Max
*/
double fat(double percentVO2) {
  return -0.565973 * pow(percentVO2,2)-.376443 * percentVO2+1.0003;
}
