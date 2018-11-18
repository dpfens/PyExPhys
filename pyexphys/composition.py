from math import pow, log10, sqrt
from pyexphys.enums import Gender


def _inches_over_ft(value, upper_bound):
    inches = value * 39.3701
    upper_bound_inches = upper_bound * 39.3701
    return inches % upper_bound_inches


def daily_water_need(weight):
    """
    The amount of water needed daily by the body based on body weight

    args:
        weight (float): body weight, given in kilograms

    Returns:
        float: estimated daily water need (in Liters)
    """
    return 0.033 * weight


class Index(object):
    """
    """

    def __init__(self, weight, height):
        """
        args:
            weight (float): body weight, given in kilograms
            height (float): body height, given in meters
        """
        self.weight = weight
        self.height = height

    def bai(self, hip_circumference):
        """
        The *body adiposity index* (**BAI**) is a method of measuring the amount of body fat in humans. The BAI uses the hip circumference (in centimeters) and the height of the participant to estimate body fat. BAI is approximately equal to the percentage of body fat for adult men and women of differing ethnicities.

        "A Better Index of Body Adiposity". Obesity - A Research Journal. Retrieved 7 March 2011.

        args:
            hip_circumference (float): hip circumference, given in meters

        Returns:
            float: The body adiposity index
        """
        numerator = 100 * hip_circumference
        denominator = self.height * sqrt(self.height)
        return (numerator / denominator) - 18

    def bmi(self):
        """
        According to the CDC:
        ..
        Body Mass Index (BMI) is a person's weight in kilograms divided by the square of height in meters. A high BMI can be an indicator of high body fatness. BMI can be used to screen for weight categories that may lead to health problems but it is not diagnostic of the body fatness or health of an individual.

        Used by the WHO as the standard for recording obesity statistics since the early 1980s, BMI is suitable for recognizing trends within sedentary or overweight individuals because there is a smaller margin of error.

        Returns:
            float: BMI
        """
        return self.weight / (self.height * self.height)

    def bmi_prime(self, upper_limit=25.9):
        """
        *BMI Prime* is the ratio of actual BMI to upper limit optimal BMI, which is the actual BMI expressed as a proportion of upper limit optimal. The ratio of actual body weight to body weight for upper limit optimal BMI is equal to BMI Prime. BMI Prime is a dimensionless number meaning that it does not have units.

        Individuals with BMI Prime less than 0.74 are underweight; those with between 0.74 and 1.00 have optimal weight; and those at 1.00 or greater are overweight. BMI Prime is useful clinically because it shows by what ratio a person deviates from the maximum optimal BMI.

        Gadzik, James (2006). "'How much should I weigh?' Quetelet's equation, upper weight limits, and BMI prime". Connecticut Medicine. 70 (2): 81\u201488. PMID 16768059

        args:
            upper_limit (float):  The upper limit of optimal BMI

        Returns:
            float: BMI Prime ratio
        """
        return self.bmi() / upper_limit

    def bsi(self, waist_circumference):
        """
        *Body Shape Index* (**BSI**) is a metric for assessing the health implications of a given human body based on height, mass and waist circumference. Including waist circumference is believed to make the BSI a better indicator of the health risks from excess weight than the standard Body Mass Index.

        Also called the *aBSI*

        "Doctors expose BMI shortcomings". London Evening Standard. Evening Standard Limited. 2006-01-18. Retrieved 2013-09-12.

        Krakauer, Nir Y.; Jesse C. Krakauer (2012-07-18). "A New Body Shape Index Predicts Mortality Hazard Independently of Body Mass Index". PLOS ONE. 7: e39504. doi:10.1371/journal.pone.0039504. Retrieved 2013-09-12.

        args:
            waist_circumference (float): waist circumference, given in meters

        Returns:
            float: BSI
        """
        return waist_circumference / pow(self.bmi(), 2 / 3) * pow(self.height, 0.5)

    def corpulence(self):
        """
        The **Corpulence measure** or **Ponderal Index** is a measure of leanness (corpulence) of a person. Like BMI, the corpulence measure is based on mass and height of an individual. Also called **Rohrer's Index**.

        The Corpulence index is known to have a number of benefits over Body Mass Index (BMI):
        - yields valid results even for very short and very tall persons
        - shown to have a lower false positive rate in athletes
        - shown to have higher sensitivity, specificity, positive predictive value, and negative predictive value than BMI

        Foods and Nutrition Encyclopedia, Audrey H. Ensminger, Marion Eugene Ensminger. p. 1645

        Babar, Sultan (March 2015). "Evaluating the Performance of 4 Indices in Determining Adiposity". Clinical Journal of Sports Medicine. Lippincott Williams & Wilkins). 25 (2): 183

        Returns:
            float: corpulence
        """
        return self.weight / pow(self.height, 3)

    def sbsi(self, bsa, vertical_trunk_circumference, waist_circumference):
        """
        The *Surface-based Body Shape Index* (**SBSI**) outperforms BMI, waist to height ratio (WHtR), waist-to-hip ratio (WHR) and Body Shape Index (BSI) at mortality hazard prediction. SBSI has a generally linear relationship with age and increases with mortality.

        "A New Potential Replacement for Body Mass Index | RealClearScience". www.realclearscience.com. Retrieved 2015-12-31.

        Rahman, Syed Ashiqur; Adjeroh, Donald (2015). "PLOS ONE: Surface-Based Body Shape Index and Its Relationship with All-Cause Mortality". PLoS ONE. 10 (12): e0144639. Bibcode:2015PLoSO..1044639R. doi:10.1371/journal.pone.0144639. PMID 26709925.

        args:
            bsa (float): body surface area, given in meters:superscript:`2`
            vertical_trunk_circumference (float): vertical_trunk_circumference, given in centimeters
            waist_circumference (float): waist_circumference, given in centimeters

        Returns:
            float: SBSI
        """
        return (pow(self.height, 7 / 4) * pow(waist_circumference, 5 / 6)) / (bsa * vertical_trunk_circumference)

    def whr(self, waist_circumference, hip_circumference):
        """
        The *waist-to-hip ratio* (**WHR**) has been used as an indicator or measure of health, and the risk of developing serious health conditions. WHR correlates with fertility (with different optimal values for males and females).

        According to the World Health Organization(WHO), abdominal obesity is defined as a waist\u2014hip ratio above 0.90 for males and above 0.85 for females, or a body mass index (BMI) above 30.0.[5] The National Institute of Diabetes, Digestive and Kidney Diseases (NIDDK) states that women with waist\u2014hip ratios of more than 0.8, and men with more than 1.0, are at increased health risk because of their fat distribution.

        WHR has been found to be a more efficient predictor of mortality in older people (75+ years of age) than waist circumference or BMI.

        "Waist Circumference and Waist-Hip Ratio, Report of a WHO Expert Consultation" `PDF <http://apps.who.int/iris/bitstream/10665/44583/1/9789241501491_eng.pdf>`__. World Health Organization. 8\u201411 December 2008. Retrieved March 21, 2012.

        args:
            waist_circumference (float)
            hip_circumference (float)

        Returns:
            float: waist-to-hip ratio
        """
        return waist_circumference / hip_circumference

    def whtr(self, waist_circumference):
        """
        The *waist-to-height ratio* (**WHtR**) is a measure of the distribution of body fat. Higher values of WHtR indicate higher risk of obesity-related cardiovascular diseases; it is correlated with abdominal obesity.

        A 2010 study that followed 11,000 subjects for up to eight years concluded that WHtR is a much better measure of the risk of heart attack, stroke or death than the more widely used body mass index.

        CM Lee, Huxley RR, Wildman RP, Woodward M (July 2008). "Indices of abdominal obesity are better discriminators of cardiovascular risk factors than BMI: a meta-analysis'". Journal of Clinical Epidemiology. 61 (7): 646\u2014653. doi:10.1016/j.jclinepi.2007.08.012. PMID 18359190.

        Schneider; et al. (2010). "The predictive value of different measures of obesity for incident cardiovascular events and mortality.". The Journal of Clinical Endocrinology & Metabolism. 95 (4): 1777\u20141785. doi:10.1210/jc.2009-1584. PMID 20130075.

        args:
            waist_circumference (float): waist circumference, given in meters

        Returns:
            float: waist-to-height ratio
        """
        return waist_circumference / self.height


class Mass(object):

    def __init__(self, gender, age, weight, height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height

    def ffm_child(self, resistance, reactance):
        """
        Tested white boys and girls 8-15 years of age

        Lohman, T.G., 1992. Advanced in body composition assessment. Current issues in exercise science series. Monograph no. 3 Champaign, IL: Human Kinetics.

        args:
            resistance (float):
            reactance (float):

        Returns:
            float: fat-free mass, given in kilograms
        """
        cm = self.height * 100
        return (0.62 * (pow(cm, 2) / resistance)) + (0.21 * self.weight) + (0.1 * reactance) + 4.2

    def ffm_adolescent(self, resistance, reactance):
        """
        Tested white boys and girls 10-19 years of age

        Houtkooper, L.B, Goinng, S.G., Lohman, T.G, Roche, A.F., and VanLoan, M. 1992. Bioelectrical impedance estimation of fat-free body mass in children and youth: A cross-validation study. Journal of Applied Physiology 72: 366-373.

        args:
            resistance (float):
            reactance (float):

        Returns:
            float: fat-free mass, given in kilograms
        """
        cm = self.height * 100
        return (0.61 * (pow(cm, 2) / resistance)) + (0.25 * self.weight) + 1.31

    def ffm_adult_lean(self, resistance, reactance):
        """
        Tested American Indian, black, Hispanic and white men and women, 17-62 years of age For body fat percentages less than 20% in males, 30% in females. Age group

        Segal, K.R., Van Loan, M., Fitzgerald, P.I., Hodgdon, J.A., and Van Itallie, T.B. 1988. Lean body mass estimation by bioelectrical impedance analysis: A four-site cross-validation study. *American Journal of Clinical Nutrition* 47: 7-14.

        args:
            resistance (float):
            reactance (float):

        Returns:
            float: fat-free mass, given in kilograms
        """
        cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.000646 * pow(cm, 2)) - (0.014 * resistance) + (0.421 * self.weight) + 10.4
        return (0.00066360 * pow(cm, 2)) - (0.02117 * resistance) + (0.62854 * self.weight) - (0.12380 * self.age) + 9.33285

    def ffm_adult_obese(self, resistance, reactance):
        """
        Tested American Indian, black, Hispanic and white men and women, 17-62 years of age For body fat percentages greater than 20% in males, 30% in females

        Segal, K.R., Van Loan, M., Fitzgerald, P.I., Hodgdon, J.A., and Van Itallie, T.B. 1988. Lean body mass estimation by bioelectrical impedance analysis: A four-site cross-validation study. *American Journal of Clinical Nutrition* 47: 7-14.

        args:
            resistance (float):
            reactance (float):

        Returns:
            float: fat-free mass, given in kilograms
        """
        cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.00091186 * pow(cm, 2)) - (0.1466 * resistance) + (0.29990 * self.weight) - (0.07012 * self.age) + 9.37938
        return (0.00088580 * pow(cm, 2)) - (0.02999 * resistance) + (0.42688 * self.weight) - (0.07002 * self.age) + 14.52435

    def ffm_adult_athlete(self, resistance, reactance):
        """
        Tested female athletes 18-27 years of age Tested male athletes from 19-40 years of age

        Female Fornetti, W.C., Pivarnik, J.M., Foley, J.M., and Fiechtner, J.J. 1999. Reliability and validity of composition measures in female athletes. Journal of Applied Physiology 87:1114-1234.

        Male Oppliger, R.A., Nielsen, D.H., and Vance, C.G. 1991. Wrestlers' minimal weight: Anthropometry, bioimpedance, and hydrostatic weighing compared. *Medicine & Science in Sports and Exercise* 23: 247-253/

        args:
            resistance (float):
            reactance (float):

        Returns:
            float: fat-free mass, given in kilograms
        """
        cm = self.height * 100
        if self.gender == Gender.Female:
            return (0.282 * cm) + (0.415 * self.weight) - (0.037 * resistance) + (0.096 * reactance) - 9.734
        return (0.186 * (pow(cm, 2) / resistance)) + (0.701 * self.weight) + 1.949


class Density(object):
    """
    Estimations of body density, or body fat percentage based on skinfold measurements
    """

    def __init__(self, gender, age, height, weight):
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

    def db_at_rv(self, body_density):
        """
        Standard Error of Estimation = 0.0067g/cc (males)
        Standard Error of Estimation = 0.0061g/cc (females)

        Donnelly, Joseph E., Thomas E. Brown, Richard G. Israel, Stephanie Smith-Sintek, Kevin F. O??brien, and Bret Caslavka. "Hydrostatic Weighing without Head Submersion: Description of a Method." Medicine & Science in Sports & Exercise 20.1 (1988): 66-69. NCBI. Web. 24 Nov. 2016. https://www.ncbi.nlm.nih.gov/pubmed/3343920.

        Returns:
            float: Body density, given in g/cc
        """
        if self.gender == Gender.Female:
            return 0.4745 * body_density + 0.5173
        return 0.5829 * body_density + 0.4059

    def skinfold_child(self, sum2skf):
        """
        For use with black/white boys and girls 6-17 years old

        Slaughter, M.H., Lohman, T.G, Boileau, R.A., Horswill, C.A., Stilman, R.J, Van Loan, M.D., and Bemben, D.A. 1988. Skinfold equation for estimation of body fatness in children and youth. *Human Biology* 60: 709-723.

        args:
            sum2skf (float): sum of skinfold measurements (triceps + calf)

        Returns:
            float: Body fat percentage
        """
        if self.gender == Gender.Female:
            return (0.610 * sum2skf) + 5.1
        return (0.735 * sum2skf) + 1.0

    def skinfold_bhf(self, sum7skf):
        """
        For use with African-American or Hispanic Females

        Jackson, A.S., Pollock, M.L., and Ward, A. 1980. Generalized equations for predicting body density of women. Medicine & Science in Sports & Exercise 12: 175-182.

        args:
            sum3skf (float): sum of skinfold measurements (chest + abdomen + thigh + triceps + subscapular + suprailiac + midaxilla)

        Returns:
            float: Body density, given in g/cc
        """
        if self.gender == Gender.Female:
            return 1.0970 - (0.00046971 * sum7skf) + (0.00000056 * pow(sum7skf, 2)) - (0.00012828 * self.age)
        return 1.112 - (0.00043499 * sum7skf) + (0.00000055 * pow(sum7skf, 2)) - (0.00028826 * self.age)

    def skinfold_wm(self, sum3skf):
        """
        For use with white males 18-61 years old

        Jackson, A.S., and Pollock, M.L. 1978. Generalized equations for predicting body density of men. British Journal of Nutrition 40: 497-504.

        args:
            sum3skf (float): sum of skinfold measurements (chest + abdomen + thigh)

        Returns:
            float: Body density, given in g/cc
        """
        return 1.10938 - (0.0008267 * sum3skf) + (0.0000016 * pow(sum3skf, 2)) - (0.0002574 * self.age)

    def skinfold_fa(self, sum3skf):
        """
        For use with white or anorexic females

        Jackson, A.S., Pollock, M.L., and Ward, A. 1980. Generalized equations for predicting body density of women. Medicine & Science in Sports & Exercise 12: 175-182.

        args:
            sum3skf (float): sum of skinfold measurements (triceps + suprailiac + thigh)

        Returns:
            float: Body density, given in g/cc
        """
        return 1.0994921 - (0.0009929 * sum3skf) + (0.0000023 * pow(sum3skf, 2)) - (0.00001392 * self.age)

    def skinfolf_athlete(self, sumskf):
        """
        For use with female athletes 19-29 years old and male athletes 18-61 years old

        Female Athletes Jackson, A.S., Pollock, M.L., and Ward, A. 1980. Generalized equations for predicting body density of women. Medicine & Science in Sports & Exercise 12: 175-182.

        Male Athletes Jackson, A.S., and Pollock, M.L. 1978. Generalized equations for predicting body density of men. British Journal of Nutrition 40: 497-504.

        args:
            sumskf (float): The sum of skinfold measurements, for Males (chest + abdomen + thigh + triceps + subscapular + suprailiac + midaxilla), for Females (triceps + anterior suprailiac + abdomen + thigh)

        Returns:
            float: Body density, given in g/cc
        """
        if self.gender == Gender.Female:
            return 1.096095 - (0.0006952 * sumskf) + (0.0000011 * pow(sumskf, 2)) - (0.0000714 * self.age)
        return 1.112 - (0.00043499 * sumskf) + (0.00000055 * pow(sumskf, 2)) - (0.00028826 * self.age)

    def skinfold_cab(self, sum3skf):
        """
        For use with African-American collegiate male and female athletes

        Evans, E.M., Rowe, D.A., Misic, M.M., Prior, B.M., and Arngrimsson, S.A. 2005. Skinfold prediction equation for athletes developed using a four-component model. Medicine & Science in Sports & Exercise 37: 2006-2011.

        args:
            sumskf (float): sum of skinfold measurements (abdomen + thigh + triceps)

        Returns:
            float: body fat percentage
        """
        if self.gender == Gender.Female:
            return 8.997 + (0.2468*sum3skf) - 1.998
        return 8.997 + (0.2468*sum3skf) - (6.343 * 1) - (1.998)

    def skinfold_caw(self, sum3skf):
        """
        For use with white collegiate male and female athletes

        Evans, E.M., Rowe, D.A., Misic, M.M., Prior, B.M., and Arngrimsson, S.A. 2005. Skinfold prediction equation for athletes developed using a four-component model. Medicine & Science in Sports & Exercise 37: 2006-2011.

        args:
            sum3skf (float):
        """
        if self.gender == Gender.Female:
            return 8.997 + (0.2468*sum3skf)
        return 8.997 + (0.2468*sum3skf) - (6.343 * 1)

    def body_volume(self, underwater_weight, residual_volume, gastrointestinal_volume, water_density=1.0):
        """
        args:
            underwater_weight (float): body weight underwater, given in kilograms
            residual_volume (float): residual volume of the lungs, given in Liters
            gastrointestinal_volume (float): volume of the gastrointestines, given in Liters
            water_density (float): density of water
        """
        return ((self.weight - underwater_weight)/ water_density) - (residual_volume - gastrointestinal_volume)


class BodyFat(object):
    """
    Used to estimate body fat percentages
    """

    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def brozek(self, body_density):
        """
        estimates body fat percentage

        Bro\u017ek, Josef; Grande, Francisco; Anderson, Joseph T.; Keys, Ancel (2006). "Densitometric Analysis of Body Composition: Revision of Some Quantitative Assumptions*". Annals of the New York Academy of Sciences. 110: 113\u201440. doi:10.1111/j.1749-6632.1963.tb17079.x. PMID 14062375.

        args:
            body_density (float): body density, given in g/cc

        Returns:
            float: body fat percentage
        """
        return (4.832 / body_density) - 4.369

    def ortiz(self, body_density):
        """
        estimates body fat percentage for African American females

        Ortiz O, Russell M, Daley TL, Baumgartner RN, Waki M, Lichtman S, et al. Differences in skeletal muscle and bone mineral mass between black and white females and their relevance to estimates of body composition. *American Journal of Clinical Nutrition*. 1992;55:8\u201413.

        args:
            body density (float): body density, given in g/cc

        Returns:
            float: body fat percentage
        """
        return (4.832 / body_density) - 4.369

    def schutte(self, body_density):
        """
        estimates body fat percentage for African American males

        Schutte JE, Townsend EJ, Hugg J, Shoup RF, Malina RM, Blomqvist CG. Density of lean body mass is greater in blacks than in whites. Journal of Applied Physiology. 1984;56(6):167\u20141649.

        args:
            body density (float): body density, given in g/cc

        Returns:
            float: body fat percentage
        """
        return (4.374 / body_density) - 3.928

    def siri(self, body_density):
        """
        estimates body fat percentage

        Siri WE (1961). "Body composition from fluid spaces and density: Analysis of methods". In Brozek J, Henzchel A. Techniques for Measuring Body Composition. Washington: National Academy of Sciences. pp. 224\u2014244.

        args:
            body density (float): body density, given in g/cc

        Returns:
            float: body fat percentage
        """
        return (4.95 / body_density) - 4.5

    def wagner(self, body_density):
        """
        estimates body fat percentage for African American males

        Wagner DR, Heyward VH. Validity of two-component models for estimating body fat of black men. Journal of Applied Physiology. 2001;90:649\u201456.

        args:
            body density (float): body density, given in g/cc

        Returns:
            float: body fat percentage
        """
        return (4.86 / body_density) - 4.39

    def child_bmi(self, weight, height):
        """
        BMI to body fat percentage formula, Deurenberg, Paul; Weststrate, Jan A.; Seidell, Jaap C. (2007). "Body mass index as a measure of body fatness: Age- and sex-specific prediction formulas". British Journal of Nutrition. 65 (2): 105\u201414. doi:10.1079/BJN19910073. PMID 2043597.

        args:
            weight (float): body weight, given in kilograms
            height (float): body_height, given in meters

        Returns:
            float: body fat percentage
        """
        bmi = weight / pow(height, 2)
        if self.gender == Gender.Female:
            return ((1.51 * bmi) - (0.70 * self.age) + 1.4) / 100
        return ((1.51 * bmi) - (0.70 * self.age) - (3.6) + 1.4) / 100

    def adult_bmi(self, weight, height):
        """
        BMI to body fat percentage formula, Deurenberg, Paul; Weststrate, Jan A.; Seidell, Jaap C. (2007). "Body mass index as a measure of body fatness: Age- and sex-specific prediction formulas". British Journal of Nutrition. 65 (2): 105\u201414. doi:10.1079/BJN19910073. PMID 2043597.

        args:
            weight (float): body weight, given in kilograms
            height (float): body_height, given in meters

        Returns:
            float: body fat percentage
        """
        bmi = weight / pow(height, 2)
        if self.gender == Gender.Female:
            return ((1.20 * bmi) - (0.23 * self.age) - 5.4) / 100
        return ((1.20 * bmi) - (0.23 * self.age) - (10.8) - 5.4) / 100

    def waist(self, weight, waist_circumference):
        weightLb = weight * 2.2
        waistCircumferenceInches = waist_circumference * 39.3701
        if self.gender == Gender.Female:
            return 100*(-76.76 + 4.15 * waistCircumferenceInches - 0.082 * weightLb) / weightLb
        return 100 * (-98.42 + 4.15 * waistCircumferenceInches - 0.082 * weightLb) / weightLb


class Ideal(object):
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

    def hamwi(self):
        inches_over_5ft = _inches_over_ft(self.height, 1.524)
        if self.gender == Gender.Female:
            return 45.5 + (2.3 * inches_over_5ft)
        return 50 + (2.3 * inches_over_5ft)

    def devine(self):
        inches_over_5ft = _inches_over_ft(self.height, 1.524)
        if self.gender == Gender.Female:
            return 45.5 + (2.2 * inches_over_5ft)
        return 48 + (2.7 * inches_over_5ft)

    def robinson(self):
        inches_over_5ft = _inches_over_ft(self.height, 1.524)
        if self.gender == Gender.Female:
            return 49 + (1.7 * inches_over_5ft)
        return 52 + (1.9 * inches_over_5ft)

    def miller(self):
        inches_over_5ft = _inches_over_ft(self.height, 1.524)
        if self.gender == Gender.Female:
            return 53.1 + (1.36 * inches_over_5ft)
        return 56.2 + (1.41 * inches_over_5ft)

    def lemmens(self):
        return 22 * pow(self.height, 2)

    def willoughby(self):
        height_inches = self.height * 39.3701
        return pow(height_inches, 3) / 1906

    def willoughby_waist(self):
        height_inches = self.height * 39.3701
        return height_inches * 0.4584


class SurfaceArea(object):
    """
    Renal clearance is usually divided by the BSA i.e. per 1.73 m:superscript:`2` to gain an appreciation of the true glomerular filtration rate (GFR); The cardiac index is a measure of cardiac output divided by the BSA, giving a better approximation of the effective cardiac output; Chemotherapy is often dosed according to the patient's BSA. Glucocorticoid dosing is also expressed in terms of BSA for calculating maintenance doses or to compare high dose use with maintenance requirement.
    """

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

    def boyd(self):
        """
        Boyd E. The growth of the surface area of the human body. Minneapolis: University of Minnesota Press, 1935. (From: http://www.ispub.com/journals/IJA/Vol2N2/bsa.htm)
        """
        cm = self.height * 100
        g = self.weight * 1000
        return 0.0003330 * pow(g, (0.7285 - (0.0188 * log10(g)))) * pow(cm, 0.3)

    def costeff(self):
        """
        The Costeff formula is a weight-based formula proposed in 1966, was recently validated for use in pediatrics.

        Costeff H, "A simple empirical formula for calculating approximate surface area in children.," Arch Dis Child, vol. 41, no. 220, pp. 681\u2014683, Dec. 1966.
        """
        return (4 * self.weight + 7) / (90 + self.weight)

    def dubois(self):
        """
        DuBois and DuBois's formula has been shown to be equally as effective in estimating body fat in obese and non-obese patients

        DuBois D, DuBois EF. A formula to estimate the approximate surface area if height and weight be known. Arch Med 1916 17:863-71.
        """
        cm = self.height * 100
        return 0.007184 * pow(self.weight, 0.425) * pow(cm, 0.725)

    def fujimoto(self):
        """
        Fujimoto S, Watanabe T, Sakamoto A, Yukawa K, Morimoto K. Studies on the physical surface area of Japanese. 18. Calculation formulae in three stages over all ages. Nippon Eiseigaku Zasshi 1968;5:443\u201450.
        """
        cm = self.height * 100
        return 0.008883 * pow(self.weight, 0.444) * pow(cm, 0.663)

    def gehan_george(self):
        """
        Gehan EA, George SL. Estimation of human body surface area from height and weight. Cancer Chemother Rep 1970 54:225-35.
        """
        cm = self.height * 100
        return 0.0235 * pow(self.weight, 0.51456) * pow(cm, 0.42246)

    def haycock(self):
        """
        Haycock GB, Schwartz GJ, Wisotsky DH. Geometric method for measuring body surface area: A height weight formula validated in infants, children and adults. The Journal of Pediatrics 1978 (93):1:62-66.
        """
        cm = self.height * 100
        return 0.024265 * pow(self.weight, 0.5378) * pow(cm, 0.3964)

    def mosteller(self):
        """
        Along with Boyd, considered to be more accurate formula for body surface area than other formulas. Maintained the most clinically acceptable and fairly constant degree of bias as children's age increases.

        Mosteller RD. Simplified Calculation of Body Surface Area. N Engl J Med. 1987 Oct 22;317(17):1098. (letter)
        """
        return sqrt(self.weight * self.height) / 6

    def schlich(self):
        """
        Schlich, E; Schumm, M; Schlich, M (2010). "3-D-Body-Scan als anthropometrisches Verfahren zur Bestimmung der spezifischen K\xf6rperoberfl\xe4che". Ern\xe4hrungs Umschau. 57: 178\\u2014183.
        """
        cm = self.height * 100
        if self.gender == Gender.Female:
            return 0.000975482 * pow(self.weight, 0.46) * pow(cm, 1.08)
        return 0.000579479 * pow(self.weight, 0.38) * pow(cm, 1.24)

    def shuter_aslani(self):
        """
        Shuter, B; Aslani, A (2000). "Body surface area: Du bois and Du bois revisited". European Journal of Applied Physiology. 82 (3): 250\u2014254. doi:10.1007/s004210050679.
        """
        cm = self.height * 100
        return 0.00949 * pow(self.weight, 0.441) * pow(cm, 0.655)

    def takahira(self):
        """
        Fujimoto S, Watanabe T, Sakamoto A, Yukawa K, Morimoto K. Studies on the physical surface area of Japanese. 18. Calculation formulae in three stages over all ages. Nippon Eiseigaku Zasshi 1968;5:443\u201450.
        """
        cm = self.height * 100
        return 0.007241 * pow(self.weight, 0.425) * pow(cm, 0.725)


class Stature(object):

    def __init__(self, gender, age, height):
        self.gender = gender
        self.age = age
        self.height = height

    def universal(self):
        """

        Standard Error of Estimation = .0222 cm

        Raxter, Michelle H., Benjamin M. Auerbach, and Christopher B. Ruff. "Revision of the Fully Technique for Estimating Statures." American Journal of Physical Anthropology 130.3 (2006): 374-84. Web.

        args:
            femur_length: femur length, given in meters

        Returns:
            float: living stature, given in meters
        """
        height_cm = self.height * 100
        stature = 1.009 * height_cm - 0.426 * self.age + 12.1
        return stature / 100

    def american_white(self, femur_length):
        """
        Trotter, Mildred, and Goldine C. Gleser. "Estimation of Stature from Long Bones of American Whites and Negroes." Am. J. Phys. Anthropol. American Journal of Physical Anthropology 10.4 (1952): 463-514. Web.

        Trotter, Mildred, and Goldine C. Gleser. "A Re-evaluation of Estimation of Stature Based on Measurements of Stature Taken during Life and of Long Bones after Death." Am. J. Phys. Anthropol. American Journal of Physical Anthropology 16.1 (1958): 79-123. Web.

        args:
            femur_length: femur length, given in meters

        Returns:
            float: living stature, given in meters
        """
        femur_length_cm = femur_length * 100
        if self.gender == Gender.Female:
            stature = 2.47 * femur_length_cm + 54.10
        else:
            stature = 2.32 * femur_length_cm + 65.53
        return stature / 100

    def american_black(self, femur_length):
        """

        Trotter, Mildred, and Goldine C. Gleser. "Estimation of Stature from Long Bones of American Whites and Negroes." Am. J. Phys. Anthropol. American Journal of Physical Anthropology 10.4 (1952): 463-514. Web.

        Trotter, Mildred, and Goldine C. Gleser. "A Re-evaluation of Estimation of Stature Based on Measurements of Stature Taken during Life and of Long Bones after Death." Am. J. Phys. Anthropol. American Journal of Physical Anthropology 16.1 (1958): 79-123. Web.

        args:
            femur_length: femur length, given in meters

        Returns:
            float: living stature, given in meters
        """
        femur_length_cm = femur_length * 100
        if self.gender == Gender.Female:
            stature = 2.28 * femur_length_cm + 59.76
        else:
            stature = 2.10 * femur_length_cm + 72.22
        return stature / 100

    def stride_length(self):
        """
        Returns:
            float: stride length, given in feet
        """
        height_cm = self.height * 100
        if self.gender == Gender.Female:
            length = 0.413 * height_cm
        else:
            length = 0.415 * height_cm
        return length / 100
