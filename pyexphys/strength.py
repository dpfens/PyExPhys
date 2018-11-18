"""
The strength module contains equations for estimating strength in weightlifting exercises, estimating 1-repetition maximum values, and metrics for comparing weightlifting performances across weight classes, and genders.
"""
from math import pow, exp, log10, sqrt
from enums import Gender


class Compare(object):
    __slots__ = ('gender', 'weight')

    def __init__(self, gender, weight):
        """
        args:
            gender (pyexphys.enums.Gender): The gender of an individual
            weight (float): Body weight, given in kilograms
        """
        self.gender = gender
        self.weight = weight

    def ocarroll(self, weight_lifted):
        """
        Normalizes a weightlifting performance by body weight

        args:
            weight_lifted (float): The amount of weight lifted , given in kilograms

        Returns:
            float: normalized weightlifting performance
        """
        return weight_lifted / pow(self.weight - 35, 1 / 3)

    def siff_weight(self):
        """
        The *Siff Bodymass Adjustment* formula for normalizing weightlifting amount based on body weight

        http://tsampa.org/training/scripts/siff/ http://dziepak.freeiz.com/training/formulas.htm Siff, Mel C. & Verkhoshansky "Supertraining" 1998, Ch 3.3.
        """
        a = 512.245
        b = 146230
        c = 1.605
        if self.gender == Gender.Female:
            a = 943.063
            b = 0.05142
            c = 257.314
            return c - a * exp(-b * self.weight)
        return a - b * pow(self.weight, -c)

    def siff_power(self):
        """
        http://dziepak.freeiz.com/training/formulas.htm Siff, Mel C. & Verkhoshansky "Supertraining" 1998, Ch 3.3.
        """
        a = 512.245
        b = 172970
        c = 1.3925
        if self.gender == Gender.Female:
            return 0
        return a - b * pow(self.weight, -c)

    def siff(self, power=False):
        """
        A shortcut formula for using the siffWeight method or the siffPower method

        http://dziepak.freeiz.com/training/formulas.htm Siff, Mel C. & Verkhoshansky "Supertraining" 1998, Ch 3.3.
        """
        if power:
            return self.siff_power()
        return self.siff_weight()

    def sinclair(self, obtained_total):
        """
        The Sinclair Coefficients for comparing performances across weight classes in Olympic weightlifting. The formula can also be used to compare male and female performances.

        - no bias for men's or women's benchpress and total
        - a favorable bias toward intermediate weight class lifters in the women's squat with no bias for men's squat
        - a linear unfavorable bias toward heavier men and women in the deadlift

        Validation of the Wilks power-lifting formula http://europepmc.org/abstract/med/10613442
        https://en.wikipedia.org/wiki/Sinclair_Coefficients
        """
        coefficient_a = 0.794358141
        coefficient_b = 174.393
        if self.gender == Gender.Female:
            coefficient_a = 0.897260740
            coefficient_b = 148.026
        if self.weight > coefficient_b:
            return 1
        exponent = pow(coefficient_a * log10(self.weight / coefficient_b), 2)
        multiplier = pow(10, exponent)
        return multiplier * obtained_total

    def wilks(self, weight_lifted):
        """
        The Wilks Coefficient to measure the strength of a powerlifters while normalizing for the body mass of the lifters. This formula is considered to be the sucessor of the O'Carroll and Schwartz formulas. The formula was written by Robert Wilks,the CEO of Powerlifting Australia.
        """
        a = -216.0475144
        b = 16.2606339
        c = -0.002388645
        d = -0.00113732
        e = 7.01863E-06
        f = -1.291E-08

        if self.gender == Gender.Female:
            a = 594.31747775582
            b = -27.23842536447
            c = 0.82112226871
            d = -0.00930733913
            e = 4.731582E-05
            f = -9.054E-08
        coefficient = 500 / (a + b * self.weight + c * pow(self.weight, 2) + d * pow(self.weight, 3) + e * pow(self.weight, 4) + f * pow(self.weight, 5))
        return coefficient * weight_lifted


class Jump(object):

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bosco(self, duration, jump_count, total_flight_time):
        """
        The *Bosco repeated vertical jump test* for average power measurement in Watts:

        Bosco C, Luhtanen P, Komi PV (1983) A simple method for measurement of mechanical power in jumping. European Journal of Applied Physiology 50:273-282.

        args:
            duration (float): test duration, given in seconds
            jump_count (int): number of jumps, given in integers
            flight_time (float): time in the air, given in seconds

        Returns:
            float: Power, given in Watts
        """
        return (total_flight_time * duration * pow(9.81, 2)) / (4 * jump_count * (duration - total_flight_time))

    def lewis(self, jump_reach_score):
        """
        The Lewis formula for estimating average power in Watts. Jump reach score is measured in meters (m).

        FOX, E.L. and MATHEWS, D.K. (1974) The interval training: conditioning for sports and general fitness. Philadelphia PA: Saunders. p. 257-258

        args:
            jump_reach_score (float): score, given in meters

        Returns:
            float: estimate of average power, given in Watts
        """
        return sqrt(4.9 * self.weight) * sqrt(jump_reach_score) * 9.81

    def harman(self, vertical_jump_height, peak=False):
        """
        The *Harman formula* for peak and average power. The original equation uses centimeters for the jump height, but this function is written for meters (m).

        HARMAN, E.A. et al. (1991) Estimation of Human Power Output From Vertical Jump. Journal of Applied Sport Science Research, 5(3), p. 116-120

        args:
            vertical_jump_height (float): height jumped, given in meters
            peak (bool): Determines if desired output should be average power, or peak power

        Returns:
            float: power, given in Watts
        """
        vertical_jump_height_cm = vertical_jump_height * 100
        if peak:
            return 61.9 * vertical_jump_height_cm + 36 * self.weight + 1822
        return 21.1 * vertical_jump_height_cm + 2.3 * self.weight + 1393

    def jb(self, vertical_jump_height, peak=False):
        """
        The *Johnson & Bahamonde test* for the calculation of peak and average power.

        JOHSON, D. L. and Bahamonde, R. (1996) Power Output Estimate in University Athletes. Journal of strength and Conditioning Research, 10(3), p. 161-166

        args:
            vertical_jump_height (float): vertical jump height, given in meters

        Returns:
            float: power output, given in Watts
        """
        body_height_cm = self.height * 100
        vertical_jump_height_cm = vertical_jump_height * 100
        if peak:
            return 78.6 * vertical_jump_height_cm + 60.3 * self.weight + 15.3 * body_height_cm + 1308
        return 43.8 * vertical_jump_height_cm + 32.7 * self.weight - 16.8 * body_height_cm + 431

    def sayer(self, vertical_jump_height):
        """
        The *sayers formula* estimates peak power output.

        SAYERS, S. et al. (1999) Cross-validation of three jump power equations. Med Sci Sports Exerc, 31, p. 572

        args:
            vertical_jump_height (float): vertical jump height, given in meters

        Returns:
            float: peak power output, given in Watts
        """
        vertical_jump_height_cm = vertical_jump_height * 100
        return 60.7 * vertical_jump_height_cm + 45.3 * self.weight - 2055

    def mk(self, vertical_jump_height, time):
        """
        The *Margaria-Kalamen power test* measures peak power in the vertical jump.

        args:
            vertical_jump_height (float): Vertical jump height, given in meters
            time (float): Time, given in seconds
        """
        return (self.weight * (vertical_jump_height / time)) * 9.81


class RMEstimator:
    """
    For predicting 1 repetition maximum(1-RM), a number of estimator classes are provided that each use a different equation for predicting 1-RM. Each of these classes are subclasses of RMEstimator and implement the same interface. Developers can change the equation for predicting 1-RM by changing the estimator class in their application rather than changing their application logic. Each class can be constructed by providing the reps parameter and can use the predict method, with a weight argument to return the 1-RM value (in kg).
    """

    def __init__(self, reps):
        """
        args:
            reps (int): repetitions performed
        """
        self.reps = reps

    def predict(self, weight):
        raise NotImplementedError("The prediction method is not implemented")


class Abadie(RMEstimator):
    """
    Studied population was 30 college aged females. Performs best when repetitions range from 5 to 10
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return 7.24 + (1.05 * weight)

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return (4./105)*(25 * rm - 181)


class Baechle(RMEstimator):
    """
    BAECHLE, T.R. and EARLE, R.W. and WATHEN, D. (2000) Resistance training. In: BAECHLE, T.R. and EARLE, R.W., eds. Essentials of Strength Training and Conditioning. 2nd ed. Champaign, IL: Human Kinetics, p. 395-425
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return weight * (1 +(0.033 * self.reps))

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return (1000 * rm)/(33 * self.reps + 1000)


class Brzycki(RMEstimator):
    """
    The *Brzycki formula* for estimating a 1-Repetition Maximum (1-RM). For repetitions less than 10, the Brzycki formula returns slightly higher estimated 1-RM than the Epley formula. The two formulas are identical at 10 repetitions.
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return weight /(1.0278 -(0.0278 * self.reps))

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return (1.0278 -(0.0278 * self.reps))

    def twoSet(self, weight, rep2, weight2):
        """
        The *Brzycki Two Set Max formula* is a 1-RM prediction equation based on the number of repetitions to fatigue obtained two submaximal sets.

        Brzycki, M. 2000. Assessing strength. Fitness Management 16(7): 34-37

        args:
            weight (float): weight lifted, given in kilograms
            rep2 (int):  Repetitions in second submaximal set
            weight2 (float): weight lifted in second submaximal set, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return ((weight - weight2)/(rep2 - self.reps)) * (self.reps - 1) + weight


class Epley(RMEstimator):
    """
    The *Epley formula* for estimating a 1-Repetition Maximum (1-RM). For repetitions less than 10, the Epley formula returns slightly lower estimated 1-RM than the Brzycki formula. The two formulas are identical at 10 repetitions.

    EPLEY, B. (1985) Poundage Chart. Boyd Epley Workout. Lincoln, NE: Body Enterprises.
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return (weight * self.reps * 0.033) + weight


class Landers(RMEstimator):
    """
    LANDERS, J. (1985) Maximums Based on Reps. National Strength and Conditioning Association Journal. 6: 60-61.
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return weight /(1.013 - (0.0267123 * self.reps))

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return rm *(1.013 - (0.0267123 * self.reps))

    def percent(self):
        """
        Returns:
            float: percentage of 1-RM
        """
        value = 101.3 - (2.67123 * self.reps)
        return value / 100


class Lombardi(RMEstimator):
    """
    For use with less than 11 repetitions

    LeSuer, Dale A.; McCormick, James H.; Mayhew, Jerry L.; Wasserstein, Ronald L.; Arnold, Michael D. (November 1997). "The Accuracy of Prediction Equations for Estimating 1-RM Performance in the Bench Press, Squat, and Deadlift". Journal of Strength and Conditioning Research. 11 (4): 211\u2014213. doi:10.1519/00124278-199711000-00001
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return weight * pow(self.reps, 0.10)

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return rm / pow(self.reps, 0.10)


class Mayhew(RMEstimator):
    """
    For use with less than 15 repetitions. Studied population was 434 (185 college men, 251 college women)

    LeSuer, Dale A.; McCormick, James H.; Mayhew, Jerry L.; Wasserstein, Ronald L.; Arnold, Michael D. (November 1997). "The Accuracy of Prediction Equations for Estimating 1-RM Performance in the Bench Press, Squat, and Deadlift". Journal of Strength and Conditioning Research. 11 (4): 211\u2014213. doi:10.1519/00124278-199711000-00001
    """

    def football(self):
        """
        Estimating the maximal 1-RM using results from the NFL-225 Bench Press Test

        Mayhew, J.L., Ball, T.E., Arnold, M.D., and Bowen, J.C. 1992. Relative muscular endurance performance as a predictor of bench press strength in college men and women. Journal of Applied Sport Science Research 6: 200-206

        Mayhew, Jerry L., John S. Ware, Michael G. Bemben, Bill Wilt, Tom E. Ward, Bill Farris, Joe Juraszek, and John P. Slovak. "The NFL-225 Test as a Measure of Bench Press Strength in College Football Players." Journal of Strength and Conditioning Research 13.2 (1999): 130-34. Web.

        Returns:
            float: 1-RM, given in kilograms
        """
        return 226.7 + 7.1 *(self.reps)

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return (100 * weight)/(52.2 + 41.9 * exp(-0.055 * self.reps))

    def percent(self):
        """
        Returns:
            float: percentage of 1-RM
        """
        value = 52.2 + 41.9 * exp(-0.055 * self.reps)
        return value / 100

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        http://www.unm.edu/~rrobergs/478RMStrengthPrediction.pdf

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return (rm * (52.2 + 41.9 * exp(-0.055 * self.reps)))/100


class McGlothin(RMEstimator):
    """
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return (100 * weight)/(101.3 - 2.67123 * self.reps)

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        LeSuer, Dale A.; McCormick, James H.; Mayhew, Jerry L.; Wasserstein, Ronald L.; Arnold, Michael D. (November 1997). "The Accuracy of Prediction Equations for Estimating 1-RM Performance in the Bench Press, Squat, and Deadlift". Journal of Strength and Conditioning Research. 11 (4): 211\u2014213. doi:10.1519/00124278-199711000-00001

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return (rm * (101.3 - 2.67123 * self.reps))/100


class OConnor(RMEstimator):

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return weight * (1 + 0.025 * self.reps)

    def percent(self, weight):
        """
        LeSuer, Dale A.; McCormick, James H.; Mayhew, Jerry L.; Wasserstein, Ronald L.; Arnold, Michael D. (November 1997). "The Accuracy of Prediction Equations for Estimating 1-RM Performance in the Bench Press, Squat, and Deadlift". Journal of Strength and Conditioning Research. 11 (4): 211\u2014213. doi:10.1519/00124278-199711000-00001
        """
        return (0.025 * (weight * self.reps) + weight)

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        http://www.unm.edu/~rrobergs/478RMStrengthPrediction.pdf

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return (40. * rm) / (self.reps + 40)


class ReynoldsCP(RMEstimator):
    """
    The *Reynolds formula* for the Chest Press exercise. Weight parameter is the 5 rep maximum (5-RM) in kg.
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return (1.1307 * weight) + 0.6998


class ReynoldsLP(RMEstimator):
    """
    The Reynolds formula for the Leg Press exercise. Weight parameter is the 5 rep maximum (5-RM) in kg.
    """

    def predict(self, weight):
        """
        http://www.unm.edu/~rrobergs/478RMStrengthPrediction.pdf

        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return (1.09703 * weight) + 14.2546


class Wathan(RMEstimator):
    """
    The *Wathan equation* for predicted the 1 repetition maximum (1-RM). The Wathan equation most closely estimates 1-RM for all upper body exercises, the leg press, and dorsiflexion exercises, and can be used to determine resistance training intensities for older adults.

    LeSuer, Dale A.; McCormick, James H.; Mayhew, Jerry L.; Wasserstein, Ronald L.; Arnold, Michael D. (November 1997). "The Accuracy of Prediction Equations for Estimating 1-RM Performance in the Bench Press, Squat, and Deadlift". Journal of Strength and Conditioning Research. 11 (4): 211\u2014213. doi:10.1519/00124278-199711000-00001
    """

    def predict(self, weight):
        """
        args:
            weight (float): weight lifted, given in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return (100 * weight) / (48.8 + (53.8 * exp(-0.075 * self.reps)))

    def weight(self, rm):
        """
        Estimates the weight lifted for the number of reps based on the 1-RM argument

        args:
            rm (float): 1-RM, given in kilograms

        Returns:
            float: weight lifted, given in kilograms
        """
        return (rm * (48.8 + (53.8 * exp(-0.075 * self.reps)))) / 100


class RM(object):
    __slots__ = ('gender', 'age')

    def __init__(self, gender, age):
        """
        args:
            gender (pyexphys.enums.Gender): gender of person
            age (float): age, given in years
        """
        self.gender = gender
        self.age = age

    def ymca_upper_body(self, reps):
        """
        The 1 repetition maximum (1-RM) equation for estimating upper body strength from the YMCA bench press test in young men and women (22-36 years old)

        For men: Total Bar weight = 80lb (36.3kg) Standard Error of Estimation = 17.6lb (8.0kg)

        For women: Total Bar weight = 35lb (15.8kg) Standard Error of Estimation = 7lb (3.2kg)

        Kim, Paul S., Jerry L. Mayhew, and D. Fred Peterson. "A Modified YMCA Bench Press Test as a Predictor of 1 Repetition Maximum Bench Press Strength." J Strength Cond Res The Journal of Strength and Conditioning Research 16.3 (2002): 440. NCBI. Web. 5 Nov. 2016. <https://www.ncbi.nlm.nih.gov/pubmed/12173960>.
        """
        if self.gender == Gender.Female:
            return (0.31 * reps) + 19.2
        return (1.55 * reps) + 37.9

    def female_middle_age(self, reps, weight):
        """
        A submaximal endurance test for middle-aged women. The participant completes as many repetitions as possible using a weight equivalent to 45% of her mass. For use with women ages 40-50 years old.

        Standard Error of Estimation = 4lb (1.85kg)

        Kuramoto, Anna K., and V. Gregory Payne. "Predicting Muscular Strength in Women: A Preliminary Study." Research Quarterly for Exercise and Sport 66.2 (1995): 168-72. NCBI. Web. 5 Nov. 2016. <https://www.ncbi.nlm.nih.gov/pubmed/12173960>.
        """
        return (1.06 * weight) + (0.58 * reps) - (0.20 * self.age) - 3.41

    def female_older(self, reps, weight):
        """
        A submaximal endurance test for older women. The participant completes as many repetitions as possible using a weight equivalent to 45% of her mass. For use with women ages 60-70 years old.

        Standard Error of Estimation = 4.5lb (2.04kg)

        Kuramoto, Anna K., and V. Gregory Payne. "Predicting Muscular Strength in Women: A Preliminary Study." Research Quarterly for Exercise and Sport 66.2 (1995): 168-72. NCBI. Web. 5 Nov. 2016. <https://www.ncbi.nlm.nih.gov/pubmed/12173960>.

        args:
            repetitions (int): number of repetitions
            weight (float): weight lifted in kilograms

        Returns:
            float: 1-RM, given in kilograms
        """
        return (0.92 * weight) + (0.79 * reps) - (0.20 * self.age) - 3.73


def relative(weight, rm):
    """
    args:
        weight (float): weight lifted, given in kilograms
        rm (float): 1-RM, given in kilograms
    """
    return rm / weight
