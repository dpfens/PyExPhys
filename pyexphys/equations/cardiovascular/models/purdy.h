#include <stdio.h>
#include <math.h>

/*
The Purdy point system is calculated from a table of running performances
compiled in 1936 called the Portuguese scoring Tables. The table lists
distance and velocity from 40 meters to 100,000 meters. These velocity
measures are assumed to be maximum possible velocity in a straight line.
These performances are arbitrarily given a Purdy point of 950.
World record times in 1970 have about 1035 Purdy points.
Times are calculated from the table (t=d/v) by linear interpolation.
Additionally, a time factor for startup and running on a curve of a track
is also added.  This "standard Calculated" time is used to generate
the points given some performace time at the same distance.
          P = A(Ts/Tp - B)
  where P - is purdy points
        Ts - Standard time from tables + time factor
        Tp - Performance time to be compared
        A, B - the scaling factors.

  However A and B have to change for different distances.
   A sliding scale for A and B was found by comparing velocity
  at 3 miles and 100 meters at 950 and 1035 pt. performances.
       Purdy comes up with:
                   k = 0.0654 - 0.00258V
                   A = 85/k
                   B = 1-950/A
         where V is the avg. velocity of Tp
*/
float purdy1(double d,float tsec)
{
	double b1=11.15895;
	double b2=4.304605;
	double b3=0.5234627;
	double b4=4.031560;
	double b5=2.316157;
	double r1=3.796158e-2;
	double r2=1.646772e-3;
	double r3=4.107670e-4;
	double r4=7.068099e-6;
	double r5=5.220990e-9;
	double v,twsec;
	double a,b,k;
	float p;

	/* calculate world record velocity running curve*/
	v = -b1*exp(-r1*d) + b2*exp(-r2*d) + b3*exp(-r3*d) +
                b4*exp(-r4*d) + b5*exp(-r5*d) ;

	/* calc time */
	twsec = d/v;
	/* calc fake purdy points */
	k = 0.0654 - 0.00258*v;
	a = 85/k;
	b = 1-1035/a;
	p = a*(twsec/tsec - b);    /* calc the purdy points */
	return p;
}

/*******************************************************/
/* calc the fraction of time from track curves
   that slows down the time from the tables */
float frac(float d)
{
	int laps,partlap,meters;
	float tmeters;
	if (d <110) return 0;
	else
	{
		laps = d/400;
		meters = d - laps*400;
		if (meters <= 50)
			partlap = 0;
		else if(meters <= 150)
			partlap = meters - 50;
		else if (meters <=250)
			partlap = 100;
		else if (meters <=350)
			partlap = 100 + (meters - 250);
		else if (meters <=400)
			partlap = 200;
		tmeters= laps*200 + partlap;
		return (tmeters/d);
	}
}
/****************************************************************/
/* calculate the famous purdy points */
float purdy(double dist,float tsec)
{
	/*
	portugese running table, distance, speed
	Table was from World Record times up to 1936
	They are arbitrarily given a Purdy point of 950
	*/

	double ptable[]= {40.0,11.000, 50.0,10.9960, 60.0,10.9830, 70.0,10.9620,
        80.0,10.934, 90.0,10.9000,100.0,10.8600,110.0,10.8150,
        120.0,10.765,130.0,10.7110,140.0,10.6540,150.0,10.5940,
        160.0,10.531,170.0,10.4650,180.0,10.3960,200.0,10.2500,
        220.0,10.096,240.0, 9.9350,260.0, 9.7710,280.0, 9.6100,
        300.0, 9.455,320.0, 9.3070,340.0, 9.1660,360.0, 9.0320,
        380.0, 8.905,400.0, 8.7850,450.0, 8.5130,500.0, 8.2790,
        550.0, 8.083,600.0, 7.9210,700.0, 7.6690,800.0, 7.4960,
        900.0,7.32000, 1000.0,7.18933, 1200.0,6.98066, 1500.0,6.75319,
        2000.0,6.50015, 2500.0,6.33424, 3000.0,6.21913, 3500.0,6.13510,
        4000.0,6.07040, 4500.0,6.01822, 5000.0,5.97432, 6000.0,5.90181,
        7000.0,5.84156, 8000.0,5.78889, 9000.0,5.74211,10000.0,5.70050,
       12000.0,5.62944,15000.0,5.54300,20000.0,5.43785,25000.0,5.35842,
       30000.0,5.29298,35000.0,5.23538,40000.0,5.18263,50000.0,5.08615,
        60000.0,4.99762,80000.0,4.83617,100000.0,4.68988,
                                  -1.0,0.0 };
	double c1=0.20;
	double c2=0.08;
	double c3=0.0065;
	double v,d3,t3,d1,t1,t950,t;
	double a,b,k,d=0.1;
	float p;
	int i;
	/* get time from port. table */
	/* find dist in table */
	for (i=0; dist > d && d>0;i+=2)
		d=ptable[i];
		if (d<1) return 0;    /* cant find distance*/
		i+=-2;
		d3=ptable[i];        /* get distance */
		t3= d3/ptable[i+1];    /* get time */
		d1=ptable[i-2];
		t1=d1/ptable[i-1];
	/* use linear interpolation to get time of 950 pt. performance*/
	t = t1 + (t3-t1)*(dist-d1)/(d3-d1);
	v = dist/t;
	/* now add the slow down from start and curves */
	t950 = t +c1+c2*v +c3*frac(dist)*v*v;
	/* calc purdy points */
	k = 0.0654 - 0.00258*v;
	a = 85/k;
	b = 1-950/a;
	p = a*(t950/tsec - b);        /* here it is */
	return p;
}

/*
@description used updated table values (uses a cruve instead)
@param {Double} distance in meters
@param {Double} time in seconds
@returns {Double} points
*/
double purdyLS(double distance, double seconds) {
  double b1 = 11.15895;
  double b2 = 4.304605;
  double b3 = 0.5234627;
  double b4 = 4.031560;
  double b5 = 2.316157;
  double r1 = 3.796158e-2;
  double r2 = 1.646772e-3;
  double r3 = 4.107670e-4;
  double r4 = 7.068099e-6;
  double r5 = 5.220990e-9;
  double v, twsec;
  double a, b, k;
  double points;

  /* Calculate world record velocity from running curve */
  v = -b1 * exp(-r1 * distance) + b2
  * pow(M_E, -r2 * distance) + b3
  * pow(M_E, -r3 * distance) + b4
  * pow(M_E, -r4 * distance) + b5
  * pow(M_E, -r5 * distance);

  /* Calculate world record time */
  twsec = distance / v;

  /* Calculate least squares Purdy Points */
  k = 0.0654 - 0.00258 * v;
  a = 85 / k;
  b = 1 - 1035 / a;
  points = a * (twsec / seconds - b);
  return points;
}
