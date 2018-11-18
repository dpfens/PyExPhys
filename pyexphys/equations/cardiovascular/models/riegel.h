#include <stdio.h>
#include <math.h>

/*
  Riegel Running Model
  @description t2 = t1 * (d2/d1) ^ 1.06
  @static
  @param {Number} t1 = time
  @param {Number} d1 = old distance
  @param {Number} d2 = new distance
  d1 & d2 must be in the same unit
  @returns {Number} t2 = estimated time to travel d2 in same unit as t1
*/
double predict_time(double t1, double d1, double d2) {
  if(t1 <= 0 || d1 <= 0 || d2 <= 0) {
    return 0;
  }
  return t1 * pow( (d2/d1), 1.06 );
}

/*
  Derived from the Riegel Running Model
  @static
  @description d2 = d1*t2^(50/53)/t1^(50/53)
  @param {Number} t1 = time
  @param {Number} d1 = old distance
  @param {Number} t2 = new time
  d1 & d2 must be in the same unit
  @returns {Number} d2 = estimated distance travelled in t2 in same unit as d1
*/
double predict_distance(double t1, double d1, double t2) {
  if(t1 <= 0 || d1 <= 0 || t2 <= 0) {
    return 0;
  }
  return d1*pow(t2, 50/53)/pow(t1, 50/53);
}
