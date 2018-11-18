"""
The cardiac module is a collection of heart-related equations used in health assessments, and calculating heart rate training zones.
"""
from math import pow, sqrt


class HREstimator(object):
    """
    Estimator classes for predicting maximum heart rate (HRMax) based on age. All of these classes implement the Estimator interface. To change the equation for predicting HRMax, developers can swap out the estimator class rather than changing their application logic.
    """
    def __init__(self):
        pass

    def predict(self, age):
        raise NotImplementedError("The prediction method is not implemented")

    def age(self, hr):
        raise NotImplementedError("The age method is not implemented")


class Astrand(HREstimator):
    """
    The Astrand equation for estimating maximum heart rate (HRMax). For use on men and women ages 4 to 34 yr

    `Astrand (1952) <http://www.dtic.mil/dtic/tr/fulltext/u2/a062385.pdf>`_
    """

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 216.6 - (0.84 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 216.6) / -0.84


class HF(HREstimator):
    """
    The Haskell & Fox equation for estimating maximum heart rate (HRMax). Recommended for use with older adults. `Fox (1971) <https://en.wikipedia.org/wiki/Heart_rate#Haskell_and_Fox>`__
    """

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 220 - age

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return 220 - hr


class Gellish(HREstimator):
    """
    The Gellish equation for estimating maximum heart rate (HRMax). For use on men and women participants in an adult fitness program with broad range of age and fitness levels

    Gellish (2007)

    Farazdaghi GR, Wohlfart B (November 2001). "Reference values for the physical work capacity on a bicycle ergometer for women between 20 and 80 years of age". `site <https://dx.doi.org/10.1046%2Fj.1365-2281.2001.00373.x>`__ Clin Physiol. 21 (6): 682\u20147. doi:10.1046/j.1365-2281.2001.00373.x. PMID 11722475.

    Wohlfart B, Farazdaghi GR (May 2003). "Reference values for the physical work capacity on a bicycle ergometer for men -- a comparison with a previous study on women". `site <https://dx.doi.org/10.1046%2Fj.1475-097X.2003.00491.x>`__ Clin Physiol Funct Imaging. 23 (3): 166\u201470. doi:10.1046/j.1475-097X.2003.00491.x. PMID 12752560.
    """

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 207 - (0.7 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 207.0) / -0.7


class Gulati(HREstimator):
    """
    The Gulati equation for estimating maximum heart rate (HRMax). For use on asymptomatic middle aged women referred for stress testing

    Gulati (2010)

    Gulati M, Shaw LJ, Thisted RA, Black HR, Bairey Merz CN, Arnsdorf MF (2010). "Heart rate response to exercise stress testing in asymptomatic women: the st. James women take heart project". Circulation. 122 (2): 130\u20147. doi:10.1161/CIRCULATIONAHA.110.939249. PMID 20585008.
    """

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 206 - (0.88 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 206.0) / -0.88


class LM(HREstimator):
    """
    Nes, B. M., et al. "Age-predicted maximal heart rate in healthy subjects: The HUNT Fitness Study." *Scandinavian journal of medicine & science in sports* 23.6 (2013): 697-704
    """

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 206.3 - (0.711 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 206.3) / -0.711


class Miller(HREstimator):

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 217 - (0.85 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 217) / -0.85


class Nes(HREstimator):

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 211 - (0.64 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 211) / -0.64


class OaklandL(HREstimator):

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 206.9 - (0.67 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 206.9) / -0.67


class OaklandNL1(HREstimator):

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 191.5 - (0.002 * pow(age, 2))

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return 5 * sqrt(3830 - 20 * hr)


class OaklandNL2(HREstimator):

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 163 + (1.16 * age) - (0.018 * pow(age, 2))

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (-10. / 9) * (sqrt(8176 - 45 * hr) - 29)


class RL(HREstimator):
    """
    Robergs R, Landwehr R (2002). "The Surprising History of the 'HRmax=220-age' Equation" (`PDF <http://www.asep.org/asep/asep/Robergs2.pdf>`__). Journal of Exercise Physiology. 5 (2): 1\u201410.

    """

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 205.8 - (0.685 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 205.8) / -0.685


class TMS(HREstimator):
    """
    The Tanaka equation for estimating maximum heart rate (HRMax). For use on healthy men and women

    Tanaka H, Monahan KD, Seals DR (January 2001). "Age-predicted maximal heart rate revisited". `site <https://www.ncbi.nlm.nih.gov/pubmed/11153730>`__ J. Am. Coll. Cardiol. 37 (1): 153\u20146. doi:10.1016/S0735-1097(00)01054-8. PMID 11153730.
    """

    def predict(self, age):
        """
        args:
            age (float): given in years
        Returns:
            float: max heart rate, given in beats/minute
        """
        return 208 - (0.7 * age)

    def age(self, hr):
        """
        args:
            hr (float): max heart rate, given in beats/minute
        Returns:
            float: age, given in years
        """
        return (hr - 208) / -0.7


def mean_arterial_pressure(diastolic_bp, systolic_bp):
    """
    The Karvonen Method for target heart rate (THR) - using a range of 50% to 85% intensity. The formula is used to calculate heart rate for exercise at a percentage training intensity.

    args:
        intensity (float): given as a decimal between 0 and 1
        rest (float): resting heart rate, given in beats/minute
        maximum (float): maximum heart rate, given in beats/minute

    Returns:
        float: heart rate for exercise at the given intensity, given in beats/minute
    """
    return ((2 * diastolic_bp) + systolic_bp) / 3


def karvonen(intensity, rest, maximum):
    """
    The Karvonen Method for target heart rate (THR) - using a range of 50% to 85% intensity. The formula is used to calculate heart rate for exercise at a percentage training intensity.

    args:
        intensity (float): given as a decimal between 0 and 1
        rest (float): resting heart rate, given in beats/minute
        maximum (float): maximum heart rate, given in beats/minute

    Returns:
        float: heart rate for exercise at the given intensity, given in beats/minute
    """
    return intensity * (maximum - rest) + rest


def zoladz(hrMax, adjuster):
    """
    Zoladz Method for target heart rate (THR) - derives exercise zones by subtracting values from HRmax. Results are +/- 5 bpm
    - Zone 1 Adjuster (easy exercise) = 50 bpm
    - Zone 2 Adjuster = 40 bpm
    - Zone 3 Adjuster = 30 bpm
    - Zone 4 Adjuster = 20 bpm
    - Zone 5 Adjuster (extremely tough exercise) = 10 bpm
    """
    return hrMax - adjuster
