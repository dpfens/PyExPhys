#include <stdio.h>
#include <math.h>

/*
  Cameron Running Model
  @description Works well for:
    post-1945 records at the 800m through the 10000m;
    from 1964 onward for the marathon
  @param {double} t1 = time in seconds
  @param {double} d1 = distance in miles
  @param {double} d2 = distance in miles
  @returns {double} t2 = estimated time to travel d2 in seconds
*/
double predictTime(double t1, double d1, double d2) {
  if(t1 <= 0 || d1 <= 0 || d2 <= 0) {
    return 0;
  }
  double a = 13.49681 - 0.048865*d1 + 2.438936/pow(d1,0.7905);
  double b = 13.49681 - 0.048865*d2 + 2.438936/pow(d2,0.7905);
  return (t1/d1) * (a/b) * d2;
}
