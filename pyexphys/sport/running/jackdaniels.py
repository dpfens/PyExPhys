from math import exp


def percent_vo2(hr_percentage):
    """
    Converts a maximum heart rate percentage into a percentage of VO2Max based using the Swain conversion formula

    SWAIN, D. et al. (1994) Target heart rates for the development of cardiorespiratory fitness. Medicine & Science in Sports & Exercise, 26(1), p. 112-116

    args:
        hr_percentage (float): percentage of maximum heart rate

    Returns:
        float: estimated conversion to percentage of VO2Max
    """
    converted_percentage = hr_percentage * 100
    formula_result = (converted_percentage - 37.182) / 0.6463
    return formula_result / 100


def percent_hrmax(vo2max_percentage):
    """
    Converts a VO2Max percentage into a maximum heart rate percentage using the Swain conversion formula

    SWAIN, D. et al. (1994) Target heart rates for the development of cardiorespiratory fitness. Medicine & Science in Sports & Exercise, 26(1), p. 112-116

    args:
        vo2max_percentage (float): percentage of VO2Max

    Returns:
        (float): estimated percentage of maximum heart rate
    """
    converted_percentage = vo2max_percentage * 100
    formula_result = (0.6463 * converted_percentage) + 37.182
    return formula_result / 100


def vvo2max(vo2max):
    """
    Calculates velocity (kilometers/hour) at a specified VO2Max (mL/(kg*min))

    args:
        vo2max (float): VO2Max, given in mL/(kg * min)

    Returns:
        float: kilometers / hour
    """
    return vo2max / 3.5


def velocity(vo2):
    """
    A regression equation relating VO2 with running velocity. Used in conjuction with the "vO2" equation to create the Jack Daniel's VDOT tables. Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.

    J., Daniels, and J. Daniels. Conditioning for Distance Running: The Scientific Aspects. New York: John Wiley and Sons., n.d. Print.

    args:
        vo2 (float): VO2, given in mL/kg/minute

    Returns:
        float: velocity, in meters/minute
    """
    return 29.54 + 5.000663 * vo2 - 0.007546 * pow(vo2, 2)


def vo2(velocity):
    """
    a regression equation relating VO2 with running velocity. Used in conjuction with the "velocity" equation to create the Jack Daniel's VDOT tables. Initially retrieved from "Oxygen Power: Performance Tables for Distance Runners" by Jack Daniels.


    Conditioning for Distance Running - the Scientific Aspects, 1978

    args:
        velocity (float): given in meters/second

    Returns:
        float: vO2, given in mL/kg/minute
    """
    return - 4.60 + 0.182258 * velocity + 0.000104 * pow(velocity, 2)


def vo2_percentage(time):
    """
    Describes the percent of an individual's aerobic capacity the individual is capable of working at for a given duration.

    Daniels, Jack, and Jimmy Gilbert. Oxygen Power: Performance Tables for Distance Runners. Tempe, AZ: J. Daniels, J. Gilbert, 1979. Print. J., Daniels, and J. Daniels. Conditioning for Distance Running: The Scientific Aspects. New York: John Wiley and Sons., n.d. Print.

    args:
        time (float): time spent running, given in minutes

    Returns:
        float: VO2 percentage
    """
    return 0.8 + pow(0.1894393, - 0.012778 * time) + exp(-0.1932605 * time)


def hr_speed(percent_hr, vo2max):
    """
    Calculates velocity (kilometers/hour) at a given heart rate percentage (in decimal form) at a given VO2Max (in mL/(kg*min)

    args:
        percent_hr (float): percentage of maximum heart rate
        vo2max (float): VO2Max, given in mL/(kg * min)

    Returns:
        float: pace, given in km/hour
    """
    vo2max_percent = percent_vo2(percent_hr)
    vo2_speed = vvo2max(vo2max)
    return vo2max_percent * vo2_speed


def hr_pace(percent_hr, vo2max):
    """
    Calculates the pace (min/km) at given heart rate percentage (in decimal form) at a given VO2Max(in mL/(kg*min))

    args:
        percent_hr (float): percentage of maximum heart rate
        vo2max (float): VO2Max, given in mL/(kg * min)

    Returns:
        float: pace, given in min/km
    """
    kph = hr_speed(percent_hr, vo2max)
    return 60 / kph


class Pace(object):
    __slots__ = ('vo2max',)

    def __init__(self, vo2max):
        self.vo2max = vo2max

    def percent(self, percentage):
        return hr_pace(percentage, self.vo2max)

    def easy(self):
        """
        Calculates the *Easy / Long (E/L) pace*(min/km) range for a given VO2Max(in mL/(kg*min). 60-79% of HRmax,used for recovery runs, warm-up, cool-down and long runs.

        Jack Daniels. "Determining your current level of fitness". Retrieved 29 December 2008.

        Returns:
            tuple: min and max paces, given in min/km
        """
        paces = (hr_pace(0.6, self.vo2max), hr_pace(0.79, self.vo2max))
        return paces

    def marathon(self):
        """
        Calculates the Marathon (M) pace(min/km) range for a given VO2Max(in mL/(kg*min). 80-85% of HRmax, primarily aimed towards runners training for the marathon.

        Jack Daniels. "Determining your current level of fitness". Retrieved 29 December 2008.

        Returns:
            tuple: min and max paces, given in min/km
        """
        paces = (hr_pace(0.8, self.vo2max), hr_pace(0.85, self.vo2max))
        return paces

    def threshold(self):
        """
        Calculates the Threshold (T) pace(min/km) range for a given VO2Max(in mL/(kg*min). 82-88% of HRmax, this intensity is aimed to raise the lactate threshold.

        Jack Daniels. "Determining your current level of fitness". Retrieved 29 December 2008.

        Returns:
            tuple: min and max paces, given in min/km
        """
        paces = (hr_pace(0.82, self.vo2max), hr_pace(0.88, self.vo2max))
        return paces

    def interval(self):
        """
        Calculates the Interval (I) pace(min/km) range for a given VO2Max( mL/(kg*min). 97-100% of HRmax, this intensity stresses the VO2max to raise the maximum oxygen uptake capacity

        Jack Daniels. "Determining your current level of fitness". Retrieved 29 December 2008.

        Returns:
            tuple: min and max paces, given in min/km
        """
        paces = (hr_pace(0.97, self.vo2max), hr_pace(1, self.vo2max))
        return paces
