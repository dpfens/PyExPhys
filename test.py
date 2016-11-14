import unittest
import pyfit.cardio.cardiac as cardiac
import pyfit.cardio.energy as energy
import pyfit.composition as composition
import pyfit.mets as mets
import pyfit.model as models
import pyfit.strength as strength
from pyfit.enums import Gender, PAL

gender = Gender.Male
weight = 65.77 # kg
height = 1.778 # meters
age = 26.5 # years

# body composition variables
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
        self.assertEquals(self.astrand.predict(age), 194.33999633789062)

    def test_hf(self):
        self.assertEquals(self.hf.predict(age), 189.4499969482422)

    def test_gellish(self):
        self.assertEquals(self.gellish.predict(age), 188.4499969482422)

    def test_gulati(self):
        self.assertEquals(self.gulati.predict(age), 182.67999267578125)

    def test_lm(self):
        self.assertEquals(self.lm.predict(age), 187.45849609375)

    def test_miller(self):
        self.assertEquals(self.miller.predict(age), 194.47500610351562)

    def test_nes(self):
        self.assertEquals(self.nes.predict(age), 194.0399932861328)

    def test_oaklandL(self):
        self.assertEquals(self.oaklandL.predict(age), 189.14500427246094)

    def test_oaklandNL1(self):
        self.assertEquals(self.oaklandNL1.predict(age), 190.0955047607422)

    def test_oaklandNL2(self):
        self.assertEquals(self.oaklandNL2.predict(age), 181.09950256347656)

    def test_rl(self):
        self.assertEquals(self.rl.predict(age), 187.6475067138672)

    def test_tms(self):
        self.assertEquals(self.tms.predict(age), 189.4499969482422)

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
        self.assertEquals(self.hb.predict(age, weight, height), 800.8040771484375)

    def test_revisedHB(self):
        self.assertEquals(self.revisedHB.predict(age, weight, height), 800.8040771484375)

    def test_msj(self):
        self.assertEquals(self.msj.predict(age, weight, height), 542.7747802734375)

class RMR(unittest.TestCase):
    def setUp(self):
        self.rmr = energy.RMR(gender, age, weight, height)

    def tearDown(self):
        del self.rmr

    def test_quick(self):
        self.assertEquals(self.rmr.quick(), 1591.6339111328125)

    def test_bsa(self):
        self.assertEquals(self.rmr.bsa(body_surface_area), 1732.7999267578125)

class TEE(unittest.TestCase):
    def setUp(self):
        self.child = energy.ChildTEE(gender, PAL.Sedentary)
        self.adult = energy.AdultTEE(gender, PAL.Sedentary)

    def tearDown(self):
        del self.child
        del self.adult

    def test_adult(self):
        self.assertEquals(self.adult.predict(age, weight, height), 2415.31787109375)

    def test_child(self):
        self.assertEquals(self.child.predict(age, weight, height), 1809.742919921875)

    def test_fromActivity(self):
        self.assertEquals(self.child.fromActivity(weight, 8.0), 9.207799911499023)

class Energy(unittest.TestCase):
    def test_cunningham(self):
        self.assertEquals(energy.cunningham(lean_body_mass), 1477.9461669921875)

    def test_kma(self):
        self.assertEquals(energy.kma(lean_body_mass), 1330.165283203125)

# Composition Module tests
class Composition(unittest.TestCase):
    def test_daily_water_intake(self):
        self.assertEquals(composition.dailyWaterNeed(weight), 2.170409917831421)

class Index(unittest.TestCase):
    def setUp(self):
        self.index = composition.Index(weight, height)

    def tearDown(self):
        del self.index

    def test_bai(self):
        value = self.index.bai(hip_circumference)
        self.assertEquals(value, 17.430858612060547)

    def test_bmi(self):
        value = self.index.bmi()
        self.assertEquals(value, 20.80483627319336)

    def test_bmi_prime(self):
        value = self.index.bmi_prime()
        self.assertEquals(value, 0.8032755255699158)

    def test_bsi(self):
        value = self.index.bsi(waist_circumference)
        self.assertEquals(value, 1.083801031112671)

    def test_corpulence(self):
        value = self.index.corpulence()
        self.assertEquals(value, 11.701257705688477)

    def test_sbsi(self):
        value = self.index.sbsi(body_surface_area, vertical_trunk_circumference, waist_circumference)
        self.assertEquals(value, 1.0397660732269287)

    def test_WHR(self):
        value = self.index.WHR(waist_circumference, hip_circumference)
        self.assertEquals(value, 0.9676190614700317)

    def test_WHtR(self):
        value = self.index.WHtR(waist_circumference)
        self.assertEquals(value, 0.4571428596973419)

class SurfaceArea(unittest.TestCase):
    def setUp(self):
        self.sa = composition.SurfaceArea(gender, age, weight, height)

    def tearDown(self):
        del self.sa

    def test_boyd(self):
        value = self.sa.boyd()
        self.assertEquals(value, 1.8661445379257202)

    def test_costeff(self):
        value = self.sa.costeff()
        self.assertEquals(value, 1.733838438987732)

    def test_dubois(self):
        value = self.sa.dubois()
        self.assertEquals(value, 1.8206592798233032)

    def test_fujimoto(self):
        value = self.sa.fujimoto()
        self.assertEquals(value, 1.7679450511932373)

    def test_gehangeorge(self):
        value = self.sa.gehangeorge()
        self.assertEquals(value, 1.8074172735214233)

    def test_haycock(self):
        value = self.sa.haycock()
        self.assertEquals(value, 1.7971676588058472)

    def test_mosteller(self):
        value = self.sa.mosteller()
        self.assertEquals(value, 1.802306056022644)

    def test_schlich(self):
        value = self.sa.schlich()
        self.assertEquals(value, 1.7530877590179443)

    def test_shuterAslani(self):
        value = self.sa.shuterAslani()
        self.assertEquals(value, 1.7894591093063354)

    def test_takahira(self):
        value = self.sa.takahira()
        self.assertEquals(value, 1.8351049423217773)

class Stature(unittest.TestCase):
    def setUp(self):
        self.stature = composition.Stature(gender, weight, height)

    def tearDown(self):
        del self.stature

    def test_universal(self):
        value = self.stature.universal()
        self.assertEquals(value, 1.6348217725753784)

    def test_americanWhite(self):
        value = self.stature.americanWhite(femurLength)
        self.assertEquals(value, 1.7689000368118286)

    def test_americanBlack(self):
        value = self.stature.americanBlack(femurLength)
        self.assertEquals(value, 1.7302000522613525)

    def test_strideLength(self):
        value = self.stature.strideLength()
        self.assertEquals(value, 0.7378700375556946)

# METs module tests
class METs(unittest.TestCase):
    def test_karvonen(self):
        self.assertEquals(mets.karvonen(8.0, 0.65), 5.549999713897705)

    def test_fromVO2(self):
        self.assertEquals(mets.fromVO2(72.3), 20.65714454650879)

    def test_toKCal(self):
        self.assertEquals(mets.toKCal(8.0, weight), 9.207799911499023)

    def test_target(self):
        self.assertEquals(mets.target(72.3, 0.65), 13.777143478393555)

# Models module tests
class Aerobic(unittest.TestCase):
    def setUp(self):
        self.cameron = models.aerobic.Cameron( performance5k["distance"], performance5k["time"])
        self.riegel = models.aerobic.Riegel( performance5k["distance"], performance5k["time"])

    def tearDown(self):
        del self.cameron
        del self.riegel

    def test_cameron(self):
        self.assertEquals( self.cameron.time(3200), 569.8930864235182)

    def test_riegel(self):
        self.assertEquals( self.riegel.time(3200), 573.2427747028469)
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
        self.assertEquals(self.abadie.predict(weightLifted), 63.939998626708984)

    def test_baechle(self):
        self.assertEquals(self.baechle.predict(weightLifted), 66.4739990234375)

    def test_brzycki(self):
        self.assertEquals(self.brzycki.predict(weightLifted), 64.81037139892578)

    def test_epley(self):
        self.assertEquals(self.epley.predict(weightLifted), 66.4739990234375)
    
    def test_landers(self):
        self.assertEquals(self.landers.predict(weightLifted), 65.37419891357422)
        self.assertEquals(self.landers.percent(), 0.8260138630867004)

    def test_lombardi(self):
        self.assertEquals(self.lombardi.predict(weightLifted), 65.59996032714844)

    def test_mayhew(self):
        self.assertEquals(self.mayhew.predict(weightLifted), 66.90547943115234)
        self.assertEquals(self.mayhew.percent(), 0.8071088194847107)

    def test_mcGlothin(self):
        self.assertEquals(self.mcGlothin.predict(weightLifted), 65.37419891357422)

    def test_oConnor(self):
        self.assertEquals(self.oconnor.predict(weightLifted), 63.45000076293945)
        self.assertEquals(self.oconnor.percent(weightLifted), 63.45000076293945)

    def test_reynoldsCP(self):
        self.assertEquals(self.reynoldsCP.predict(weightLifted), 61.757598876953125)

    def test_reynoldsLP(self):
        self.assertEquals(self.reynoldsLP.predict(weightLifted), 73.49421691894531)

    def test_wathan(self):
        self.assertEquals(self.wathan.predict(weightLifted), 66.97618103027344)

    def test_ymcaUpperBody(self):
        self.assertEquals(self.rm.ymcaUpperBody(reps), 48.75)

    def test_femaleMiddleAge(self):
        self.assertEquals(self.rm.femaleMiddleAge(reps, weightLifted), 52.59000015258789)

    def test_femaleOlder(self):
        self.assertEquals(self.rm.femaleOlder(reps, weightLifted), 46.18000030517578)


class Strength(unittest.TestCase):
    def test_relative(self):
        self.assertEquals(strength.relative(weight, weightLifted), 0.821043074131012)

if __name__ == '__main__':
    unittest.main()
