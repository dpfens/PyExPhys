from math import log, pow


class Riegel(object):
    __slots__ = ('d1', 't1')
    """
    A class for making predictions based on the Riegel model for predicting endurance performances between 3.5 minutes and 230 minutes. Riegel's analysis involved walking, running, and swimming.
    The model can accept any unit for time (t1 & t2) and distance (d1 and d2), so long as the units are consistent.

    The following class attributes are multipliers taken from Riegel's Athletics Records and Human Endurance publication.  These attributes can be used as multipliers for difference sports:

    Attributes:
        RUNNING_MEN (float):  Multiplier for Adult males, running
        RUNNING_MEN_40 (float):  Multiplier for Adult males in their 40s, running
        RUNNING_MEN_50 (float):  Multiplier for Adult males in their 50s, running
        RUNNING_MEN_60 (float):  Multiplier for Adult males in their 60s, running
        RUNNING_MEN_70 (float):  Multiplier for Adult males in their 70s, running
        RUNNING_WOMEN (float):  Multiplier for Adult females, running

        SWIMMING_MEN (float):  Multiplier for Adult males, swimming
        SWIMMING_WOMEN (float):  Multiplier for Adult females, swimming

        NORDIC_MEN (float):  Multiplier for Adult males, Noroic skiing
        WALKING_MEN (float):  Multiplier for Adult males, Walking
        ROLLER_SKATING_MEN (float):  Multiplier for Adult males, roller skating
        CYCLING_MEN (float):  Multiplier for Adult males, cycling
        SPEED_SKATING_MEN (float):  Multiplier for Adult males, speed skating

    Riegel, P. S. (August 1977). "Time Predicting". Runner's World Magazine. Riegel, Peter S. (May\u2014June 1981). "Athletic Records and Human Endurance". American Scientist. 69: 285\u2014290.
    """
    RUNNING_MEN = 1.07732
    RUNNING_MEN_40 = 1.05352
    RUNNING_MEN_50 = 1.05374
    RUNNING_MEN_60 = 1.05603
    RUNNING_MEN_70 = 1.06370
    RUNNING_WOMEN = 1.08283

    SWIMMING_MEN = 1.02977
    SWIMMING_WOMEN = 1.03256

    NORDIC_MEN = 1.01421
    WALKING_MEN = 1.05379
    ROLLER_SKATING_MEN = 1.13709
    CYCLING_MEN = 1.04834
    SPEED_SKATING_MEN = 1.06017

    def __init__(self, d1, t1):
        """
        args:
            d1 (float):  Distance traversed in a previous performance
            t1 (float):  Time spent travelling distance (d1) in a previous performance
        """
        self.d1 = d1
        self.t1 = t1

    def distance(self, t2, multiplier=1.06):
        """
        Predict the distance traversed in a given period of time (t2) based on the time (t1) and distance (d2) used in the class constructor

        args:
            t2 (float): Time (in same units as t1) spent travelling
            multiplier (float, optional):  The multiplier for the mode of transportation

        Returns:
            float:  The estimated distance traversed in the same units as d1
        """
        if t2 <= 0:
            raise ValueError('t2(%s) must be > 0' % t2)
        return self.d1 * (pow(t2, 1 / multiplier) / pow(self.t1, 1 / multiplier))

    def time(self, d2, multiplier=1.06):
        """
        Predict the distance traversed in a given period of time (t2) based on the time (t1) and distance (d2) used in the class constructor

        args:
            d2 (float): Distance (in same units as d1) travelled
            multiplier (float, optional):  The multiplier for the mode of transportation

        Returns:
            float:  The estimated time to travel the given distance (in the same units as t1)
        """
        if d2 <= 0:
            raise ValueError('d2(%s) must be > 0' % d2)
        d2 = float(d2)
        return self.t1 * pow((d2 / self.d1), multiplier)


class Cameron:
    """
    A class for making predictions based on the Cameron model for predicting endurance performances between 400m and 50 miles. The model is based on non-linear regression model from top times in the U.S. and in the world in 1998.

    Note: While distance values in the initial regression model were required to be in miles, this implementation takes meters(m) as the input unit for distance.
    """
    __slots__ = ('d1', 't1')

    def __init__(self, d1, t1):
        """
        args:
            d1 (float): distance ran in meters
            t1 (float): seconds taken to travel d1
        """
        self.d1 = d1
        self.t1 = t1

    def __f__(self, x):
        return 13.49681 - 0.048865 * x + 2.438936 / pow(x, 0.7905)

    def time(self, d2):
        """
        Predict the time to travel a given distance (d2) based on the time (t1) and distance (d2) used in the class constructor.

        args:
            d2 (float): Distance to predict a time for, given in meters

        Returns:
            float: time in seconds
        """
        d1_miles = self.d1 / 1609.34
        d2_miles = d2 / 1609.34
        if d2 <= 0:
            return 0
        return (self.t1 / d1_miles) * (self.__f__(d1_miles) / self.__f__(d2_miles)) * d2_miles


class VV:
    """
    A class for making predictions using the Vickers & Vertosick model for predicting endurance performances at the marathon distance in recreational runners. The Vickers & Vertosick model uses average weekly training mileage and previous race times to calculate a predicted time.
    """

    def __init__(self, d1, t1):
        """
        args:
            d1 (float): distance of performance, given in meters
            t1 (float): time for performance, given in seconds
        """
        self.d1 = d1
        self.t1 = t1

    def adj_timer(self, d1, t1):
        return d1 / (d1 / t1)

    def riegel_velocity(self, distance, multiplier=1.06):
        adj_timer = self.adj_timer(self.d1, self.t1)
        return distance / (adj_timer * pow(distance / self.d1, multiplier))

    def time(self, mileage, d2=42195.0):
        """
        The single-race model for calculating a predicted time for a given distance. Defaults to the marathon if a distance is not provided.

        args:
            mileage (float): average weekly mileage, given in miles
            d2 (float): distance to predict a time for,given in meters

        Returns:
            float: predicted time for d2, given in seconds
        """
        riegel_velocity = self.riegel_velocity(d2)
        velocity = 0.16018617 + (0.83076202 * riegel_velocity) + (0.6423826 * (mileage / 10))
        minutes = (d2 / 60) / velocity
        seconds = minutes * 60
        return seconds

    def time2(self, mileage, d2, t2, distance=42195.0):
        """
        The two-race model for calculating a predicted time for a given distance. Defaults to the marathon if a distance is not provided.

        args:
            mileage (float): average weekly mileage, given in miles
            d2 (float): distance for a second performance, given in meters
            t2 (float): time for d2, given in seconds
            distance (float): distance to predict for, given in meters

        Returns:
            float: predicted time for distance, given in seconds
        """
        adj_timer_r1 = self.adj_timer(self.d1, self.t1)
        adj_timer_r2 = self.adj_timer(d2, t2)
        k_r2_r1 = log(adj_timer_r2 / adj_timer_r1) / log(d2 / self.d1)
        k_marathon = 1.4510756 + (-0.23797948 * k_r2_r1) + (-0.01410023 * (mileage / 10))
        seconds = (adj_timer_r2 * pow(distance / d2, k_marathon))
        return seconds
