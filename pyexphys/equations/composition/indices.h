#include <stdio.h>
#include <math.h>

/*
BMI
mass in kg
height in cm
*/
float bmi(float kg, float height) {
	float meters = height / 100;
	return kg / (meters * meters);
}

/* Ponderal (Rohrer) Index
mass in kg
height in cm
*/
float ponderal(float kg, float height) {
	return 1000 * pow(kg,1/3)/height;
}
