"""
The respiration module contains formulas for estimating the capacity of the lungs and for estimating the efficiency of the respiration system using VO2/VO2Max. These equations are used in general health assessments, aerobic performance assessments, and in developing training plans for endurance sports.
"""
from math import exp, pow
from pyexphys.enums import Gender


class ResidualVolume(object):
    """
    A class for calculating the residual volume of the lungs for men and women across the lifespan.
    """
    __slots__ = ('gender', 'age', 'weight', 'height')

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

    def normal(self):
        heightCm = self.height * 100
        return 0.0275 * self.age + 0.0189 * heightCm - 2.6139

    def overweight(self):
        heightCm = self.height * 100
        return 0.0277 * self.age + 0.0138 * heightCm - 2.3967

    def berglund(self):
        """
        Berglund, E., Birath, G., Bjure, J., Grimby, G., Kjellmar, I., Sandvist, L., and Soderholm, B. 1963. Spirometric studies in normal subjects. I. Forced expirograms in subjects between 7 and 70 years of age. Acta Medica Scandinavica 173: 185-192.

        Returns:
            float: residual volume, given in liters
        """
        heightCm = self.height * 100
        if self.gender == Gender.Female:
            return 0.007 * self.age + 0.0268 * self.height - 3.42
        return (0.022 * self.age) + (0.0198 * heightCm) - (0.015 * self.weight) - 1.54

    def black(self):
        """
        Standard Error of the Estimate (SEE) = 0.46 Liters

        Black, L.F., Offord, K., and Hyatt, R.E. 1974. Variability in the maximum expiratory flow volume curve in asymptomatic smokers and nonsmokers. *American Review of Respiratory Diseases* 110: 282-292.

        Returns:
            float: residual volume, given in liters
        """
        heightCm = self.height * 100
        return 0.21 * self.age + 0.023 * heightCm - 2.978

    def boren(self):
        """
        Standard Error of the Estimate (SEE) = 0.53

        Boren, H.G., Kory, R.C., and Syner, J.C. 1966. The Veteran's Administration-Army cooperative study of pulmonary functionsL II. The lung volume and its subdivisions in normal men. *American Journal of Medicine* 41: 96-114.

        Returns:
            float: residual volume, given in liters
        """
        heightCm = self.height * 100
        return (0.0115 * self.age) + (0.019 * heightCm) - 2.24

    def goldman(self):
        """
        Goldman, H.I., and Becklake, M.R. 1959. Respiratory function tests: Normal values at medium altitudes and the prediction of normal results. *American Review of Tuberculosis and Respiratory Diseases* 79: 457-467.

        Returns:
            float: residual volume, given in liters
        """
        heightCm = self.height * 100
        if self.gender == Gender.Female:
            return 0.009 * self.age + 0.032 * heightCm - 3.9
        return (0.017 * self.age) + (0.027 * heightCm) - 3.477

    def obrien(self, bsa):
        """
        Standard Error of the Estimate (SEE) = 0.49 Liters

        O'Brien, R.J., and Drizd, T.A. 1983. Roentgenographic determination of total lung capacity: Normal values from a national population survey. *American Review of Respiratory Diseases* 128: 949-952.

        Returns:
            float: residual volume, given in liters
        """
        heightCm = self.height * 100
        return (0.03 * self.age) + (0.0387 * heightCm) - (0.73 * bsa) - 4.78


class VO2(object):
    """
    A class for calculating VO2 and VO2Max
    """
    __slots__ = ('gender', 'age', 'weight', 'height')

    def __init__(self, gender, age, weight, height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    def reserve(self, vo2Max, vo2Rest=3.5):
        """
        *VO2 Reserve* (VO2R) is the difference between resting VO2 and VO2Max. Percent VO2 Reserve (%VO2R) is considered a more accurate metric for establishing relative exercise intensity than %VO2Max in both low-fit individuals and elite athletes.

        Ehrman, Jonathan K. *ACSM's Resource Manual for Guidelines for Exercise Testing and Prescription. 6th ed.* Philadelphia: Wolters Kluwer Health/Lippincott Williams & Wilkins, 2010. Print.

        args:
            vo2Max (float): given in mL/kg*min
            vo2Rest (float): given in mL/kg*min

        Returns:
            float: VO2, given in mL/kg * min
        """
        return vo2Max - vo2Rest

    def target(self, vo2Max, vo2Rest, intensity):
        return intensity * (vo2Max - vo2Rest) + vo2Rest

    def cooper(self, distance):
        """
        The Cooper VO2Max test is a submaximal VO2Max test based on a population of healthy adults. Returns VO2Max in mL/kg*min.

        COOPER, K.H. (1968) A means of assessing maximal oxygen intake. JAMA. 203, p. 135-138

        args:
            distance (float): given in miles

        Returns:
            float: VO2Max, given in mL/kg*min
        """
        return 0.0268 * distance - 11.3

    def walking_gross(self, speed, grade):
        """
        For speeds between 50-100 minter/min (1.9-3.7mph).

        Heyward, Vivian H. "Metabolic Equations for Estimating Gross VO2 (ACSM 2010)." 2010. *Advanced Fitness Assessment and Exercise Prescription. 6th ed.* Champaign, IL: Human Kinetics, 2010. N. pag. Print.

        args:
            speed (float): given in meters/minute
            grade (float): given in decimal form

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return (0.1 * speed) + (1.8 * speed * grade)

    def running_gross(self, speed, grade):
        """
        For speeds greater than 134 meters/min (5.0 mph). If truly jogging (not walking), this equation can be used for speed of 80-134 meters/min (3-5 mph)

        Heyward, Vivian H. "Metabolic Equations for Estimating Gross VO2 (ACSM 2010)." 2010. *Advanced Fitness Assessment and Exercise Prescription. 6th ed.* Champaign, IL: Human Kinetics, 2010. N. pag. Print.

        args:
            speed (float): given in meters/minute
            grade (float): given in decimal form

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return (0.2 * speed) + (0.9 * speed * grade)

    def leg_ergometry_gross(self, mass, work):
        """
        Heyward, Vivian H. "Metabolic Equations for Estimating Gross VO2 (ACSM 2010)." 2010. *Advanced Fitness Assessment and Exercise Prescription. 6th ed.* Champaign, IL: Human Kinetics, 2010. N. pag. Print.

        args:
            mass (float): given in kilograms
            work (float): given in Watts

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return 3.5 + 1.8 * (work / mass)

    def arm_ergometry_gross(self, mass, work):
        """
        Heyward, Vivian H. "Metabolic Equations for Estimating Gross VO2 (ACSM 2010)." 2010. *Advanced Fitness Assessment and Exercise Prescription. 6th ed.* Champaign, IL: Human Kinetics, 2010. N. pag. Print.

        Ehrman, Jonathan K. *ACSM's Resource Manual for Guidelines for Exercise Testing and Prescription. 6th ed.* Philadelphia: Wolters Kluwer Health/Lippincott Williams & Wilkins, 2010. Print.

        args:
            mass (float): given in kilograms
            work (float): given in Watts

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return (3.0 * work / mass)

    def stepping_gross(self, height, frequency):
        """
        Heyward, Vivian H. "Metabolic Equations for Estimating Gross VO2 (ACSM 2010)." 2010. *Advanced Fitness Assessment and Exercise Prescription. 6th ed.* Champaign, IL: Human Kinetics, 2010. N. pag. Print.

        args:
            height (float): height of bench, given in meters
            frequency (float): steps/minute

        Returns:
            float: Gross VO2Max, given in mL/kg/min
        """
        return (0.2 * frequency) + (frequency * self.height * 1.8 * 1.33)

    def usop(self, hrMax, restingHR):
        """
        The Uth\u2014S\u0216rensen\u2014Overgaard\u2014Pedersen estimation is a VO2Max estimate based on measurements of maximum heart rate and minimum heart rate in well-trained men aged 21 to 51. The formula is most reliable when based on actual measurement of maximum heart rate, rather than an age-related estimates.

        The estimation uses the ratio of maximum heart rate (HrMax) to resting heart rate (restingHR) to predict VO2max, and returns VO2Max in mL/kg/minute.

        Uth, Niels; Henrik S\u0216rensen; Kristian Overgaard; Preben K. Pedersen (January 2004). "Estimation of VO2max from the ratio between HRmax and HRrest--the Heart Rate Ratio Method". *Eur J Appl Physiol.* 91 (1): 111\u20145. doi:10.1007/s00421-003-0988-y. PMID 14624296.

        args:
            hrMax (float): maximum heart rate, given in beats/minute
            restingHR (float): given in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return 15.3 * (hrMax / restingHR)

    def fox_ergometry(self, hr5):
        """
        The equation for predicting VO2Max in a population of healthy adults using the sub-maximal Fox test.

        Fox, E. L. 1973. A simple, accurate technique for predicting maximal aerobic power. *Journal of Applied Physiology*, 35: 914 - 16

        args:
            hr5 (float): heart rate after 5 minutes of cycling, given in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return 6300.0 - (19.26 * hr5)

    def ebbeling_treadmill(self, speed, hr):
        """
        A single-stage treadmill walking test developed by Ebbeling and colleagues for estimating VO2max of low-risk, healthy adults 20-59 years.

        Ebbeling, Cara B., Ann Ward, Elaine M. Puleo, Jeffrey Widrick, and James M. Rippe. "Development of a Single-stage Submaximal Treadmill Walking Test." *Medicine & Science in Sports & Exercise* 23.8 (1991): n. pag. NIH. Web. 5 Nov. 2016. https://www.ncbi.nlm.nih.gov/pubmed/1956273.

        args:
            speed (float): given in miles/hour
            hr (float): given in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return 15.1 + (21.8 * speed) - (0.327 * hr) - (0.263 * self.age) + (0.00504 * (hr * self.age)) + (5.48 * 0.0)
        return 15.1 + (21.8 * speed) - (0.327 * hr) - (0.263 * self.age) + (0.00504 * (hr * self.age)) + (5.48 * 1.0)

    def kline(self, time, hrPeak):
        """
        The Kline et al. (1987) formula for the 1-mile walk Rockport Test for VO2Max.

        Kline, Greg M., John P. Porcari, Robert Hintermeister, Patty S. Freedson, Ann Ward, Robert F. Mccarron, Jessica Ross, and James M. Rippe. "Estimation of &OV0312;O2max from a One-mile Track Walk, Gender, dob, and Body Weight." *Medicine & Science in Sports & Exercise* 19.3 (1987): n. pag. Web.

        McSwegin P, Plowman S, Wolff G, Guttenberg G. The validity of a one-mile walk test for high school age individuals. Measurement in Physical Education and Exercise Science 1998;2:47-63.

        George, J. D. et al. VO2max estimation from a submaximal 1-mile track jog for fit college-age individuals. Medicine and Science in Sports and Exercise, 25, 401-406, 1993.

        args:
            time (float): given in minutes
            hrPeak (float): given in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return 132.853 - 0.0769 * self.weight - 0.3877 * self.age + 6.315 * 0.0 - 3.2649 * time - 0.1565 * hrPeak
        return 132.853 - 0.0769 * self.weight - 0.3877 * self.age + 6.315 * 1.0 - 3.2649 * time - 0.1565 * hrPeak

    def larsen(self, time, hr):
        """
        The Larsen VO2Max formula for use in the 1.5 mile run/walk test. For use with young adults (18-29 years old).

        Standard Error of Estimation = 2.5 mL/kgmin TE = 2.68 mL/kg*min

        LARSEN, G. et al. (2002) Prediction of maximum oxygen consumption from walking, jogging, or running. *Research quarterly for exercise and sport*, 73 (1), p. 66-72.

        args:
            time (float): given in minutes
            hr (float): given in beats/minute

        Returns:
            float: VO2Max, given in mL/kg * min
        """
        if self.gender == Gender.Female:
            return 100.16 + (7.30 * 0.0) - (0.164 * self.weight) - (1.273 * time) - (0.1563 * hr)
        return 100.16 + (7.30 * 1.0) - (0.164 * self.weight) - (1.273 * time) - (0.1563 * hr)

    def astrand_step(self, hr):
        """
        The *Astrand Step Test formula* for estimating a participant's VO2Max.

        Marley, W. P., and A. C. Linnerud. "Astrand-ryhming Step Test Norms for College Students." *British Journal of Sports Medicine* 10.2 (1976): 76-79. NIH. Web. 5 Nov. 2016. <http://bjsm.bmj.com/content/10/2/76.long>.

        args:
            hr (float): given in beats/minute

        Returns:
            float: VO2Max, given in L/min
        """
        if self.gender == Gender.Female:
            return 3.750 * ((self.weight + 3) / (hr - 65))
        return 3.744 * ((self.weight + 5) / (hr - 62))

    def qc_step(self, hr):
        """
        The Queen's College Step Test formula for estimating a participant's VO2Max.

        McArdle, W.D., Katch, F.I., Pechar, G.S., Jacobson, L., and Ruck, S. 1972. Reliability and interrelationships between maximal oxygen intake, physical working capacity and step-test scores in college women. Medicine and Science in Sports 4: 182-186.

        args:
            hr (float): given in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return 65.81 - (0.1847 * hr)
        return 111.33 - (0.42 * hr)

    def george_rw(self, time):
        """
        The formula for the George single-stage jogging test formula. For use with the George 1 mile jog test.

        George, J., Vehrs, P., Allsen, P., Fellingham, G., and Fisher, G. 1993. VO2max estimation from a sub-maximal 1-mile track jog for fit college-age individuals. *Medicine & Science in Sports & Exercise* 25: 401-406

        args:
            time (float): given in minutes

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return 88.02 - (0.1656 * self.weight) - (2.76 * time) + (3.716 * 0.0)
        return 88.02 - (0.1656 * self.weight) - (2.76 * time) + (3.716 * 1.0)

    def george_steady(self, time, hr):
        """
        The George formula for the 1 mile steady state jog test. Returns VO2Max in mL/kg/min.

        George, J., Vehrs, P., Allsen, P., Fellingham, G., and Fisher, G. 1993. VO2max estimation from a sub-maximal 1-mile track jog for fit college-age individuals. *Medicine & Science in Sports & Exercise* 25: 401-406

        args:
            speed (float): given in miles/hour
            hr (float): heart rate in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return 100.5 - 0.1636 * self.weight - 1.438 * time - 0.1928 * hr
        return 100.5 - 0.1636 * self.weight - 1.438 * time - 0.1928 * hr + 8.344

    def george_treadmill(self, speed, hr):
        """
        George, J., Vehrs, P., Allsen, P., Fellingham, G., and Fisher, G. 1993. VO2max estimation from a sub-maximal 1-mile track jog for fit college-age individuals. *Medicine & Science in Sports & Exercise* 25: 401-406

        args:
            speed (float): given in miles/hour
            hr (float): heart rate in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return 54.07 - (0.1938 * self.weight) - (4.47 * speed) + (0.01453 * hr) + (7.062 * 0.0)
        return 54.07 - (0.1938 * self.weight) - (4.47 * speed) + (0.01453 * hr) + (7.062 * 1.0)

    def treadmill_submax_single_stage(self, sm1, hr1, hrmax):
        """
        Heyward, Vivian H. "Treadmill Submaximal Exercise Tests: single-stage Model." *Advanced Fitness Assessment and Exercise Prescription. 6th ed.* Champaign, IL: Human Kinetics, 2010. 85. Print.

        args:
            sm1 (float): distance traversed during the test, given in meters
            hr1 (float): heart rate in beats/minute
            hrmax (float): maximal heart rate in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return sm1 * ((hrmax - 72) / (hr1 - 72))
        return sm1 * ((hrmax - 61) / (hr1 - 61))

    def treadmill_submax_vo2_multistage(self, sm1, hr1, sm2, hr2, hrmax):
        """
        Heyward, Vivian H. "Treadmill Submaximal Exercise Tests: Multistage Model." *Advanced Fitness Assessment and Exercise Prescription. 6th ed.* Champaign, IL: Human Kinetics, 2010. 85. Print.

        args:
            sm1 (float): distance traversed during the test, given in meters
            hr1 (float): heart rate in beats/minute
            sm2 (float): distance traversed during the test, given in meters
            hr2 (float): heart rate in beats/minute
            hrmax (float): maximal heart rate in beats/minute

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        b = (sm2 - sm1) / (hr2 - hr1)
        return sm2 + b * (hrmax - hr2)

    def cureton_child(self, time):
        """
        The Cureton formula for estimating VO2Peak in the 1.0 mile run/walk in children (8-17 years old).

        Cureton, K.J., Sloniger, M., O'Bannon, J., Black, D., and McCormack, W. 1995. A generalized equation for prediction of VO2peak from 1-mile run/walk performance. *Medicine & Science in Sports & Exercise* 27: 445-451.

        Note: For evaluating the fitness of younger children (5-7 years old), the 0.5 mile run/walk test is recommended.

        Rikli, Roberta E., Clayre Petray, and Ted A. Baumgartner. "The Reliability of Distance Run Tests for Children in Grades K-4." *Research Quarterly for Exercise and Sport* 63.3 (1992): 270-76. NCBI. Web. 10 Nov. 2016. <https://www.ncbi.nlm.nih.gov/pubmed/1513957>.

        args:
            distance (float): distance traversed during the test, given in meters

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        bmi = (self.weight / pow(self.height / 100, 2))
        return 108.94 - (8.41 * time) + 0.34 * 108.94 - (8.41 * time) + 0.34 * pow(time, 2) + 0.21 * self.age - (0.84 * bmi)

    def balke(self, time):
        """
        Balke and Ware (1959) exercise test protocols.

        Source (Men) Pollock, M.L., Bohannon, R.L., Cooper, K.H., Ayres, J.J., Ward, A., White, S.R., and Linnerud, A.C. 1976 A comparative analysis of four protocols for maximal treadmill strss testing. *American Heart Journal* 92: 39-46.

        Source (Women) POLLOCK et al. (1982) Comparative analysis of physiologic responses to three different maximal graded exercise test protocols in healthy women. *American Heart Journal*, 103 (3), p. 363-373

        args:
            distance (float): distance traversed during the test, given in meters

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        if self.gender == Gender.Female:
            return 1.38 * time + 5.22
        return 1.444 * time + 14.99

    def balke_15min_run(self, distance):
        """
        The Balke formula for the 15 min run test for VO2Max.

        args:
            distance (float): distance traversed during the test, given in meters

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return 0.0178 * distance + 9.6

    def bruce_male(self, time, time2, time3):
        """
        The Bruce protocol equation for use with active and sedentary men. The Bruce protocol is used for estimating VO2Max based on treadmill exercise.

        Standard Error of Estimate: 3.35 mL/kg/min

        Note: For use with the standard Bruce protocol, not the Modified Bruce protocol

        FOSTER et al. (1984) Generalized equations for predicting functional capacity from treadmill performance. *American Heart Journal*, 107 (6), p. 1229-1234

        args:
            time (float): given in minutes
            time2 (float): given in minutes
            time3 (float): given in minutes

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return 14.76 - 1.379 * time + 0.451 * time2 - 0.012 * time3

    def bruce_female(self, time):
        """
        The Bruce protocol equation for use with active and sedentary women. The Bruce protocol is used for estimating VO2Max based on multi-stage treadmill exercise. The protocol increases the workload by changing both speed and grade of the treadmill.

        Note: For use with the standard Bruce protocol, not the Modified Bruce protocol

        Standard Error of Estimate: 2.7 mL/kg/min

        POLLOCK et al. (1982) Comparative analysis of physiologic responses to three different maximal graded exercise test protocols in healthy women. *American Heart Journal*, 103 (3), p. 363-373

        args:
            time (float): given in minutes

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return 4.38 * time - 3.90

    def bruce_ec(self, time):
        """
        A VO2Max prediction equation for use with cardiac patients and elderly patients when using the Bruce Treadmill protocol.

        Standard Error of Estimation: 4.9 mL/kg/min

        Note: Used only for treadmill walking while holding the handrails

        McConnell, Timothy R.;Clark, Bernard A., "Prediction of Maximal Oxygen Consumption During Handrail-Supported Treadmill Exercise". Journal Of Cardiopulmonary Rehabilitation And Prevention, 1987

        args:
            time (float): given in minutes

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return (2.282 * time) + 8.545

    def leger(self, speed):
        """
        A 20m Shuttle run test developed by Leger and colleagues (1988) to test the aerobic fitness of children, dobs 8-19 years

        Leger, L. A., D. Mercier, C. Gadoury, and J. Lambert. "The Multistage 20 Metre Shuttle Run Test for Aerobic Fitness." Journal of Sports Sciences 6.2 (1988): 93-101. NCBI. Web. 10 Nov. 2016. <https://www.ncbi.nlm.nih.gov/pubmed/3184250>.

        args:
            velocity (float): given in km/hour

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        return 31.025 + (3.238 * speed) - (3.248 * self.age) + 0.1536 * (self.age * speed)

    def gilbert_daniels(self, velocity, time):
        """
        The Glibert-Daniels formula for VO2Max. This formula is used to calculate VO2Max from race results.

        DANIELS, J. (2005) Daniels Running Formula. 2nd Ed. Leeds, UK: Human Kinetics. p. 48

        args:
            velocity (float): given in meters/minute
            time (float): given in minutes

        Returns:
            float: VO2Max, given in mL/kg/min
        """
        numerator = 0.000104 * pow(velocity, 2) + 0.182258 * velocity - 4.6
        denominator= 0.2989558 * exp(- 0.1932605 * time) + 0.1894393 * exp(- 0.012778 * time) + 0.8
        return numerator / denominator
