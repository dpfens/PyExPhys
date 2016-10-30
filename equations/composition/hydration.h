#include <math.h>

/*
@param {Double} weight in kg
@returns {Double} L/day
*/
double dailyNeeds(double weight) {
  return 0.033 * weight;
}
