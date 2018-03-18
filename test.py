import unittest
import pyfit.cardio.cardiac as cardiac
import pyfit.cardio.energy as energy
import pyfit.composition as composition
import pyfit.mets as mets
import pyfit.model as models
import pyfit.strength as strength
import pyfit.anthropometry as anthropometry
from pyfit.enums import Gender, PAL

gender = Gender.Male
weight = 65.77 # kg
height = 1.778 # meters
age = 26.5 # years

# body composition variables
body_height = 177.8
femurLength = 0.48 # meters
lean_body_mass = 44.4521 # kg
waist_circumference = 0.8128 # meters
hip_circumference = 0.84 # meters
vertical_trunk_circumference = 0.9 # meters
body_surface_area = 1.9 # meters^2


# 1-RM variables
reps = 7
weightLifted = 54 # kg

# aerobic model variables
performance5k = {"distance": 5000, "time": 920}

class Anthropometry(unittest.TestCase):

    def test_bodyheight(self):
        segment = anthropometry.Segment(body_height)
        self.assertEqual(segment.height_eyes(), 166.4208 )
        self.assertEqual(segment.height_head(), 154.686)
        self.assertEqual(segment.height_shoulders(), 145.4404)
        self.assertEqual(segment.height_chest(), 128.016)
        self.assertEqual(segment.height_elbow(), 112.01400000000001)
        self.assertEqual(segment.height_wrist(), 86.233)
        self.assertEqual(segment.height_fingertip(), 67.0306)
        self.assertEqual(segment.height_hips(), 94.23400000000001)
        self.assertEqual(segment.height_buttocks(), 86.233)
        self.assertEqual(segment.height_knee(), 50.673)
        self.assertEqual(segment.height_ankle(), 6.934200000000001)
        self.assertEqual(segment.head_height(), 23.114)
        self.assertEqual(segment.shoulder_distance(), 22.936200000000003)
        self.assertEqual(segment.shoulder_width(), 46.050200000000004)
        self.assertEqual(segment.hips_width(), 33.9598)
        self.assertEqual(segment.nipple_width(), 30.9372)
        self.assertEqual(segment.foot_width(), 9.779)
        self.assertEqual(segment.foot_length(), 27.0256)
        self.assertEqual(segment.humerus_length(), 33.0708)
        self.assertEqual(segment.forearm_length(), 25.9588)
        self.assertEqual(segment.hand_length(), 19.2024)
        self.assertEqual(segment.upperbody_length(), 92.456)

    def test_segment(self):
        pass


# Cardio module tests
class Cardiac(unittest.TestCase):
    def test_map(self):
        self.assertEquals(cardiac.mean_arterial_pressure(80, 120), 93.0)

    def test_karvonen(self):
        self.assertEquals(cardiac.karvonen(0.5, 60, 180), 120.0)

    def test_zoladz(self):
        self.assertEquals(cardiac.zoladz(180, 50), 130.0)

class MaxHR(unittest.TestCase):
    def setUp(self):
        self.astrand = cardiac.Astrand()
        self.hf = cardiac.HF()
        self.gellish = cardiac.Gellish()
        self.gulati = cardiac.Gulati()
        self.lm = cardiac.LM()
        self.miller = cardiac.Miller()
        self.nes = cardiac.Nes()
        self.oaklandL = cardiac.OaklandL()
        self.oaklandNL1 = cardiac.OaklandNL1()
        self.oaklandNL2 = cardiac.OaklandNL2()
        self.rl = cardiac.RL()
        self.tms = cardiac.TMS()

    def tearDown(self):
        del self.astrand
        del self.hf
        del self.gellish
        del self.gulati
        del self.lm
        del self.miller
        del self.nes
        del self.oaklandL
        del self.oaklandNL1
        del self.oaklandNL2
        del self.rl
        del self.tms

    def test_astrand(self):
        self.assertEquals(self.astrand.predict(age), 194.34)

    def test_hf(self):
        self.assertEquals(self.hf.predict(age), 193.5)

    def test_gellish(self):
        self.assertEquals(self.gellish.predict(age), 188.45)

    def test_gulati(self):
        self.assertEquals(self.gulati.predict(age), 182.68)

    def test_lm(self):
        self.assertEquals(self.lm.predict(age), 187.45850000000002)

    def test_miller(self):
        self.assertEquals(self.miller.predict(age), 194.475)

    def test_nes(self):
        self.assertEquals(self.nes.predict(age), 194.04)

    def test_oaklandL(self):
        self.assertEquals(self.oaklandL.predict(age), 189.145)

    def test_oaklandNL1(self):
        self.assertEquals(self.oaklandNL1.predict(age), 190.0955)

    def test_oaklandNL2(self):
        self.assertEquals(self.oaklandNL2.predict(age), 181.0995)

    def test_rl(self):
        self.assertEquals(self.rl.predict(age), 187.6475)

    def test_tms(self):
        self.assertEquals(self.tms.predict(age), 189.45)

class BMR(unittest.TestCase):
    def setUp(self):
        self.hb = energy.HB(gender)
        self.revisedHB = energy.RevisedHB(gender)
        self.msj = energy.MSJ(gender)

    def tearDown(self):
        del self.hb
        del self.revisedHB
        del self.msj

    def test_hb(self):
        self.assertEquals(self.hb.predict(age, weight, height), 800.8040994)

    def test_revisedHB(self):
        self.assertEquals(self.revisedHB.predict(age, weight, height), 827.574812)

    def test_msj(self):
        self.assertEquals(self.msj.predict(age, weight, height), 542.7747999999999)

class RMR(unittest.TestCase):
    def setUp(self):
        self.rmr = energy.RMR(gender, age, weight, height)

    def tearDown(self):
        del self.rmr

    def test_quick(self):
        self.assertEquals(self.rmr.quick(), 1591.6339999999998)

    def test_bsa(self):
        self.assertEquals(self.rmr.bsa(body_surface_area), 1732.8)

class TEE(unittest.TestCase):
    def setUp(self):
        self.child = energy.ChildTEE(gender, PAL.Sedentary)
        self.adult = energy.AdultTEE(gender, PAL.Sedentary)

    def tearDown(self):
        del self.child
        del self.adult

    def test_adult(self):
        self.assertEquals(self.adult.predict(age, weight, height), 2415.3179999999998)

    def test_child(self):
        self.assertEquals(self.child.predict(age, weight, height), 1809.743)

    def test_fromActivity(self):
        self.assertEquals(self.child.fromActivity(weight, 8.0), 9.207799999999999)

class Energy(unittest.TestCase):

    def setUp(self):
        self.terrain = energy.Terrain(65.2, 1.38582, 40.0)

    def tearDown(self):
        del self.terrain

    def test_cunningham(self):
        self.assertEquals(energy.cunningham(lean_body_mass), 1477.9462)

    def test_kma(self):
        self.assertEquals(energy.kma(lean_body_mass), 1330.16536)

    def test_terrain(self):
        grade = 1.3
        self.assertEquals(self.terrain.pandolf(1.0,grade), 527.4256573224053 )
        self.assertEquals(self.terrain.santee(1.0,grade), 476.69467709470246)



# Composition Module tests
class Composition(unittest.TestCase):
    def test_daily_water_intake(self):
        self.assertEquals(composition.daily_water_need(weight), 2.17041)

class Index(unittest.TestCase):
    def setUp(self):
        self.index = composition.Index(weight, height)

    def tearDown(self):
        del self.index

    def test_bai(self):
        value = self.index.bai(hip_circumference)
        self.assertEquals(value, 17.43085650680662)

    def test_bmi(self):
        value = self.index.bmi()
        self.assertEquals(value, 20.804837528042402)

    def test_bmi_prime(self):
        value = self.index.bmi_prime()
        self.assertEquals(value, 0.8032755802332974)

    def test_bsi(self):
        value = self.index.bsi(waist_circumference)
        self.assertEquals(value, 1.0838010645501324)

    def test_corpulence(self):
        value = self.index.corpulence()
        self.assertEquals(value, 11.701258452217322)

    def test_sbsi(self):
        value = self.index.sbsi(body_surface_area, vertical_trunk_circumference, waist_circumference)
        self.assertEquals(value, 1.039766081871345)

    def test_WHR(self):
        value = self.index.whr(waist_circumference, hip_circumference)
        self.assertEquals(value, 0.9676190476190476)

    def test_whtr(self):
        value = self.index.whtr(waist_circumference)
        self.assertEquals(value, 0.45714285714285713)

class SurfaceArea(unittest.TestCase):
    def setUp(self):
        self.sa = composition.SurfaceArea(gender, age, weight, height)

    def tearDown(self):
        del self.sa

    def test_boyd(self):
        value = self.sa.boyd()
        self.assertEquals(value, 1.8661444964284422)

    def test_costeff(self):
        value = self.sa.costeff()
        self.assertEquals(value, 1.7338383514155487)

    def test_dubois(self):
        value = self.sa.dubois()
        self.assertEquals(value, 1.820659283833425)

    def test_fujimoto(self):
        value = self.sa.fujimoto()
        self.assertEquals(value, 1.7679451154824195)

    def test_gehan_george(self):
        value = self.sa.gehan_george()
        self.assertEquals(value, 1.807417314977944)

    def test_haycock(self):
        value = self.sa.haycock()
        self.assertEquals(value, 1.7971677529555214)

    def test_mosteller(self):
        value = self.sa.mosteller()
        self.assertEquals(value, 1.8023060844990295)

    def test_schlich(self):
        value = self.sa.schlich()
        self.assertEquals(value, 1.753087770492256)

    def test_shuter_aslani(self):
        value = self.sa.shuter_aslani()
        self.assertEquals(value, 1.789459160601124)

    def test_takahira(self):
        value = self.sa.takahira()
        self.assertEquals(value, 1.8351049379507)

class Stature(unittest.TestCase):
    def setUp(self):
        self.stature = composition.Stature(gender, weight, height)

    def tearDown(self):
        del self.stature

    def test_universal(self):
        value = self.stature.universal()
        self.assertEquals(value, 1.6348217999999997)

    def test_american_white(self):
        value = self.stature.american_white(femurLength)
        self.assertEquals(value, 1.7689)

    def test_american_black(self):
        value = self.stature.american_black(femurLength)
        self.assertEquals(value, 1.7302000000000002)

    def test_stride_length(self):
        value = self.stature.stride_length()
        self.assertEquals(value, 0.73787)

# METs module tests
class METs(unittest.TestCase):
    def test_karvonen(self):
        self.assertEquals(mets.karvonen(8.0, 0.65), 5.55)

    def test_from_vo2(self):
        self.assertEquals(mets.from_vo2(72.3), 20.657142857142855)

    def test_to_kcal(self):
        self.assertEquals(mets.to_kcal(8.0, weight), 9.207799999999999)

    def test_target(self):
        self.assertEquals(mets.target(72.3, 0.65), 13.777142857142856)

# Models module tests
class Aerobic(unittest.TestCase):
    def setUp(self):
        self.cameron = models.aerobic.Cameron( performance5k["distance"], performance5k["time"])
        self.riegel = models.aerobic.Riegel( performance5k["distance"], performance5k["time"])

    def tearDown(self):
        del self.cameron
        del self.riegel

    def test_cameron(self):
        self.assertEquals( self.cameron.time(3200), 569.8930999989254)

    def test_riegel(self):
        self.assertEquals( self.riegel.time(3200), 573.2427882846001)
        self.assertEquals( self.riegel.distance(260), 1517.82078410174)



# Strength module tests
class RM1(unittest.TestCase):
    def setUp(self):
        self.abadie = strength.Abadie(reps)
        self.baechle = strength.Baechle(reps)
        self.brzycki = strength.Brzycki(reps)
        self.epley = strength.Epley(reps)
        self.landers = strength.Landers(reps)
        self.lombardi = strength.Lombardi(reps)
        self.mayhew = strength.Mayhew(reps)
        self.mcGlothin = strength.McGlothin(reps)
        self.oconnor = strength.OConnor(reps)
        self.reynoldsCP = strength.ReynoldsCP(reps)
        self.reynoldsLP = strength.ReynoldsLP(reps)
        self.wathan = strength.Wathan(reps)

        self.rm = strength.RM(gender, age)

    def tearDown(self):
        del self.abadie
        del self.baechle
        del self.brzycki
        del self.epley
        del self.landers
        del self.lombardi
        del self.mayhew
        del self.mcGlothin
        del self.oconnor
        del self.reynoldsCP
        del self.reynoldsLP
        del self.wathan

        del self.rm

    def test_abadie(self):
        self.assertEquals(self.abadie.predict(weightLifted), 63.940000000000005)

    def test_baechle(self):
        self.assertEquals(self.baechle.predict(weightLifted), 66.474)

    def test_brzycki(self):
        self.assertEquals(self.brzycki.predict(weightLifted), 64.81036965914546)

    def test_epley(self):
        self.assertEquals(self.epley.predict(weightLifted), 66.474)

    def test_landers(self):
        self.assertEquals(self.landers.predict(weightLifted), 65.37420254065944)
        self.assertEquals(self.landers.percent(), 0.8260139)

    def test_lombardi(self):
        self.assertEquals(self.lombardi.predict(weightLifted), 65.59995837810962)

    def test_mayhew(self):
        self.assertEquals(self.mayhew.predict(weightLifted), 66.9054765496236)
        self.assertEquals(self.mayhew.percent(), 0.8071088165697222)

    def test_mcGlothin(self):
        self.assertEquals(self.mcGlothin.predict(weightLifted), 65.37420254065943)

    def test_oConnor(self):
        self.assertEquals(self.oconnor.predict(weightLifted), 63.45)
        self.assertEquals(self.oconnor.percent(weightLifted), 63.45)

    def test_reynoldsCP(self):
        self.assertEquals(self.reynoldsCP.predict(weightLifted), 61.757600000000004)

    def test_reynoldsLP(self):
        self.assertEquals(self.reynoldsLP.predict(weightLifted), 73.49422)

    def test_wathan(self):
        self.assertEquals(self.wathan.predict(weightLifted), 66.97618046223116)

    def test_ymca_upper_body(self):
        self.assertEquals(self.rm.ymca_upper_body(reps), 48.75)

    def test_female_middle_age(self):
        self.assertEquals(self.rm.female_middle_age(reps, weightLifted), 52.59)

    def test_female_older(self):
        self.assertEquals(self.rm.female_older(reps, weightLifted), 46.18)


class Strength(unittest.TestCase):
    def test_relative(self):
        self.assertEquals(strength.relative(weight, weightLifted), 0.821043028736506)

if __name__ == '__main__':
    unittest.main()
