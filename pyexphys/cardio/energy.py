"""
The energy module calculates the energy requirements of the human body to maintain stability. These values, such as Basal Metabolic Rate (BMR), Estimated Energy Requirement (EER) are used in estimating the required kilocalories (kcal) required by the human body based on activity level. This value is important in developing lifestyle-based nutrition plans.
"""
from pyexphys.enums import PAL, Gender


class BMREstimator(object):
    """
    A class for estimating the basal metabolic rate of children, adults, and older adults over a given time period.
    """
    __slots__ = ('gender', )

    def __init__(self, gender):
        """
        args:
            gender (pyexphys.enums.Gender): Gender of the individual
        """
        self.gender = gender

    def predict(self, age, weight, height):
        raise NotImplementedError("The prediction method is not implemented")


class HB(BMREstimator):
    """
    The original Harris-Benedict Equation for basal metabolic rate.

    Harris J, Benedict F (1918). "*A Biometric Study of Human Basal Metabolism*". PNAS. 4 (12): 370\u20143. Bibcode:1918PNAS....4..370H. doi:10.1073/pnas.4.12.370. PMC 1091498Freely accessible. PMID 16576330. `Article <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1091498/>`__ `PDF <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1091498/pdf/pnas01945-0018.pdf>`__
    """

    def predict(self, age, weight, height):
        """
        args:
            age (float): age, given in years
            weight (float): body weight, given in kilograms
            height (float): body height, given in meters

        Returns:
            float: basal metabolic rate, given as kilocalories/day
        """
        if self.gender == Gender.Female:
            return (9.5634 * weight) + (1.8496 * height) - (4.6756 * age) + 655.0955
        return (13.7516 * weight) + (5.0033 * height) - (6.7550 * age) + 66.4730


class RevisedHB(BMREstimator):
    """
    The Revised Harris-Benedict Equation for basal metabolic rate (BMR). Accurately estimates the REE of normal-weight, overweight, and obese individuals but overestimate REE in underweight individuals.

    Roza, Allan M; Shizgal, Harry M (1984). "*The Harris Benedict equation reevaluated: resting energy requirements and the body cell mass*". The American Journal of Clinical Nutrition. 40: 168\u2014182.
    """

    def predict(self, age, weight, height):
        """
        args:
            age (float): age, given in years
            weight (float): body weight, given in kilograms
            height (float): body height, given in meters

        Returns:
            float: basal metabolic rate, given as kilocalories/day
        """
        if self.gender == Gender.Female:
            return (9.247 * weight) + (3.098 * height) - (4.330 * age) + 447.593
        return (13.397 * weight) + (4.799 * height) - (5.677 * age) + 88.362


class MSJ(BMREstimator):
    """
    The Mifflin St. Jeor Equation for basal metabolic rate (BMR). The American Dietetic Association (2003) recommends using this equation over Harris-Benedict to estimate RMR in healthy individuals.

    Mifflin, MD; St Jeor, ST; Hill, LA; Scott, BJ; Daugherty, SA; Koh, YO (1990). "*A new predictive equation for resting energy expenditure in healthy individuals*". The American Journal of Clinical Nutrition. 51 (2): 241\u20147. PMID 2305711.
    """

    def predict(self, age, weight, height):
        """
        args:
            age (float): age, given in years
            weight (float): body weight, given in kilograms
            height (float): body height, given in meters

        Returns:
            float: basal metabolic rate, given as kilocalories/day
        """
        if self.gender == Gender.Female:
            return (9.99 * weight + 6.25 * height - 4.92 * age - 161)
        return (9.99 * weight + 6.25 * height - 4.92 * age + 5)


class RMR(object):
    __slots = ('gender', 'age', 'weight', 'height')

    def __init__(self, gender, age, weight, height):
        """
        args:
            gender (pyexphys.enums.Gender): The gender of an individual
            age (float): The age of a person, given in years
            weight (float): Body weight, given in kilograms
            height (float): Body height, given in meters
        """
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    def quick(self):
        """
        A quick estimate of resting metabolic rate (RMR) based on body mass


        """
        if self.gender == Gender.Female:
            return self.weight * 22
        return self.weight * 24.2

    def bsa(self, bsa):
        """
        Estimate resting metabolic rate based on body surface area (BSA)

        Note: every decade after age 40, RMR decreases by 2-5% (Sharkey and Gaskill, 2007), which is not applied in the formula due to high variation.
        """
        if self.gender == Gender.Female:
            return bsa * 840
        return bsa * 912


def kma(lbm):
    """
    The Katch-McArdle Formula for resting daily energy expenditure (RDEE). This formula takes lean body mass/fat-free mass (in kilograms) as the only argument.

    McArdle, W (2006). Essentials of Exercise Physiology. Lippincott Williams & Wilkins. p. 266. ISBN 9780495014836.
    """
    return 370 + (21.6 * lbm)


def cunningham(lbm):
    """
    The Cunningham equation for resting metabolic rate (RMR). This formula is similar to Katch-McArdle, but provides a slightly higher estimate.

    """
    return 500 + (22 * lbm)


class TEEEstimator(object):
    """
    A class for estimating the total energy expenditure (TEE) in individuals of varying levels of physical activity.
    """
    __slots__ = ('gender', 'pal')

    def __init__(self, gender, pal):
        """
        args:
            gender (pyexphys.enums.Gender): The gender of an individual
            pal (pyexphys.enums.PAL): The physical activity level of an individual
        """
        self.gender = gender
        self.pal = pal

    def predict(self, age, weight, height):
        raise NotImplementedError("The prediction method is not implemented")

    def fromActivity(self, weight, mets):
        """
        Humphrey R, The Exercise Caloric Challenge, Clinical Applications, ACSM\u0027s Health & Fitness Journal, March/April 2006, Vol. 10, No. 2 pp.40-41

        args:
            weight (float): body weight, given in kilograms
            mets (float): METs, given in kcal/kg/hour

        Returns:
            float: kcal/min
        """
        return (mets * 3.5 * weight)/200


class ChildTEE(TEEEstimator):
    __slots__ = ('gender', 'pal')

    def predict(self, age, weight, height):
        """
        args:
            age (float): The age of a person, given in years
            weight (float): Body weight, given in kilograms
            height (float): Body height, given in meters

        returns:
            float: total energy expenditure, given in kilocalories/day
        """
        if self.pal == PAL.Sedentary and self.gender == Gender.Male:
            return 88.5 - (61.9 * age) + 1 * ((26.7 * weight) + (903 * height))
        elif self.pal == PAL.Sedentary and self.gender == Gender.Female:
            return 135.3 - (30.8 * age) + 1 * ((10 * weight) + (934 * height))
        elif self.pal == PAL.Low and self.gender == Gender.Male:
            return 88.5 - (61.9 * age) + 1.13 * ((26.7 * weight) + (903 * height))
        elif self.pal == PAL.Low and self.gender == Gender.Female:
            return 135.3 - (30.8 * age) + 1.16 * ((10 * weight) + (934 * height))
        elif self.pal == PAL.Active and self.gender == Gender.Male:
            return 88.5 - (61.9 * age) + 1.26 * ((26.7 * weight) + (903 * height))
        elif self.pal == PAL.Active and self.gender == Gender.Female:
            return 135.3 - (30.8 * age) + 1.31 * ((10 * weight) + (934 * height))
        elif self.pal == PAL.VeryActive and self.gender == Gender.Male:
            return 88.5 - (61.9 * age) + 1.42 * ((26.7 * weight) + (903 * height))
        elif self.pal == PAL.VeryActive and self.gender == Gender.Female:
            return 135.3 - (30.8 * age) + 1.56 * ((10 * weight) + (934 * height))
        return 0


class AdultTEE(TEEEstimator):
    __slots__ = ('gender', 'pal')

    def predict(self, age, weight, height):
        """
        args:
            age (float): The age of a person, given in years
            weight (float): Body weight, given in kilograms
            height (float): Body height, given in meters

        returns:
            float: total energy expenditure, given in kilocalories/day
        """
        if self.pal == PAL.Sedentary and self.gender == Gender.Male:
            return 662 - (9.53 * age) + 1 * ((15.9 * weight) + (540 * height))
        elif self.pal == PAL.Sedentary and self.gender == Gender.Female:
            return 354 - (6.91 * age) + 1 * ((9.36 * weight) + (726 * height))
        elif self.pal == PAL.Low and self.gender == Gender.Male:
            return 662 - (9.53 * age) + 1.11 * ((15.9 * weight) + (540 * height))
        elif self.pal == PAL.Low and self.gender == Gender.Female:
            return 662 - (9.53 * age) + 1.12 * ((15.9 * weight) + (540 * height))
        elif self.pal == PAL.Active and self.gender == Gender.Male:
            return 662 - (9.53 * age) + 1.25 * ((15.9 * weight) + (540 * height))
        elif self.pal == PAL.Active and self.gender == Gender.Female:
            return 662 - (9.53 * age) + 1.27 * ((15.9 * weight) + (540 * height))
        elif self.pal == PAL.VeryActive and self.gender == Gender.Male:
            return 662 - (9.53 * age) + 1.48 * ((15.9 * weight) + (540 * height))
        elif self.pal == PAL.VeryActive and self.gender == Gender.Female:
            return 662 - (9.53 * age) + 1.45 * ((15.9 * weight) + (540 * height))
        return 0


class Terrain:
    """
    Formulas for calculating energy expenditure
    """
    __slots__ = ('weight', 'speed', 'load')

    def __init__(self, weight, speed, load):
        self.weight = weight
        self.speed = speed
        self.load = load

    def pandolf(self, terrain, slope):
        """
        The Pandolf, Givoni, and Goldman formula for calculating energy expenditure. Funded by the United States Army Research Institute of Environmental Medicine.

        Pandolf K.B., Givoni B., Goldman R.F. Predicting energy expenditure with loads while standing or walking very slowly. J Appl Physiol 43: 577\u2014581, 1977

        args:
            terrain (int)
            slope (float): slope of the terrain, given as a percentage

        Returns:
            float: metabolic rate, given in Watts
        """
        total_weight = self.weight + self.load
        part_1 = (1.5 * self.weight) + 2.0 * (total_weight) * pow(self.load/self.weight, 2)
        part_2 = terrain * total_weight * (1.5 * pow(self.speed, 2) + 0.25 * self.speed * slope)
        return part_1 + part_2

    def santee(self, terrain, slope):
        """
        The Santee formula for calculating energy expenditure. The formula is an updated version of the Pandolf formula that more accurately takes into account downhill travel. The formula is for use with negative (downhill) slopes.

        Matthew W.T., Santee W.R., Berglund L.G. Solar Load Inputs for USARIEM Thermal Strain Models and the Solar Radiation-Sensitive Components of the WBGT Index (Technical Report T01/13\u2014 01). Natick, MA: U.S. Army Research Institute of Environmental Medicine, 2001.

        args:
            terrain (int)
            slope (float): slope of the terrain, given as a percentage

        Returns:
            float: metabolic rate, given in Watts
        """
        total_weight = self.weight + self.load
        energy = self.speed * slope
        speed_squared = pow(self.speed, 2)

        part1 = 1.5 * self.weight + 2 * pow(self.load/self.weight, 2)
        part2 = terrain * total_weight * (1.5 * speed_squared + 0.35 * energy)
        part3_1 = (energy * total_weight) / 3.5
        part3_2 = (total_weight * pow(slope + 6, 2)) / self.weight
        part3_3 = 25 - speed_squared
        return part1 + part2 - terrain * (part3_1 - part3_2 + part3_3)
