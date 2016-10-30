from libc.math import exp, pow

cpdef float velocity(float vO2):
    return 29.54 + 5.000663*vO2 - 0.007546 * pow(vO2, 2)

cpdef float vO2(float velocity):
    return -4.60 + 0.182258 * velocity + 0.000104 * pow(velocity, 2)

cpdef float vO2Percentage(float time):
    return 0.8 + pow(0.1894393, -0.012778*time)+ exp(-0.1932605*time)
