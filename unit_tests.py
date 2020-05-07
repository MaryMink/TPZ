from test_lab_1 import Formuls, NonPositiveIncorrect entry
import unittest

class TestFormuls(unittest.TestCase):

    def test_first_calculation1(self):
        F = Formuls(1)
        res = F.formul_1()
        self.assertEqual(res, 5.324)

    def test_first_calculation2(self):
        F = Formuls(1)
        res = F.formul_2()
        self.assertEqual(res, 5.454000000000001)

    def test_first_calculation3(self):
        F = Formuls(1)
        res = F.formul_3()
        self.assertEqual(res, 3.9059999999999997)

    def test_first_calculation4(self):
        F = Formuls(1)
        res = F.formul_4()
        self.assertEqual(res, 6.364)

    def test_second_calculation1(self):
        F = Formuls(0.1)
        res = F.formul_1()
        self.assertEqual(res, 0.414437)

    def test_second_calculation2(self):
        F = Formuls(0.1)
        res = F.formul_2()
        self.assertEqual(res, 0.5120100000000001)

    def test_second_calculation3(self):
        F = Formuls(0.1)
        res = F.formul_3()
        self.assertEqual(res, 0.26091)

    def test_second_calculation4(self):
        F = Formuls(0.1)
        res = F.formul_4()
        self.assertEqual(res, 0.6364000000000001)

    def test_third_calculation1(self):
        F = Formuls(0)
        res = F.formul_1()
        self.assertEqual(res, 0.0)

    def test_third_calculation2(self):
        F = Formuls(0)
        res = F.formul_2()
        self.assertEqual(res, 0.0)

    def test_third_calculation3(self):
        F = Formuls(0)
        res = F.formul_3()
        self.assertEqual(res, 0.0)

    def test_third_calculation4(self):
        F = Formuls(0)
        res = F.formul_4()
        self.assertEqual(res, 0.0)

    def test_fourth_calculation1(self):
        F = Formuls(2)
        res = F.formul_1()
        self.assertEqual(res, 66.078)

    def test_fourth_calculation2(self):
        F = Formuls(2)
        res = F.formul_2()
        self.assertEqual(res, 24.456000000000003)

    def test_fourth_calculation3(self):
        F = Formuls(2)
        res = F.formul_3()
        self.assertEqual(res, 10.693999999999999)

    def test_fourth_calculation4(self):
        F = Formuls(2)
        res = F.formul_4()
        self.assertEqual(res, 12.728)

    def test_fifth_calculation1(self):
        F = Formuls(58)
        res = F.formul_1()
        self.assertEqual(res, 42862423.574)

    def test_fifth_calculation2(self):
        F = Formuls(58)
        res = F.formul_2()
        self.assertEqual(res, 646619.496)

    def test_fifth_calculation3(self):
        F = Formuls(58)
        res = F.formul_3()
        self.assertEqual(res, 4990.494000000001)

    def test_fifth_calculation4(self):
        F = Formuls(58)
        res = F.formul_4()
        self.assertEqual(res, 369.11199999999997)

    def test_sixth_calculation1(self):
        F = Formuls(1000)
        res = F.formul_1()
        self.assertEqual(res, 3752266653653.0)

    def test_sixth_calculation2(self):
        F = Formuls(1000)
        res = F.formul_2()
        self.assertEqual(res, 3366669420.0)

    def test_sixth_calculation3(self):
        F = Formuls(1000)
        res = F.formul_3()
        self.assertEqual(res, 1443465.0)

    def test_sixth_calculation4(self):
        F = Formuls(1000)
        res = F.formul_4()
        self.assertEqual(res, 6364.0)

    def test_seventh_calculation1(self):
        F = Formuls(199)
        res = F.formul_1()
        self.assertEqual(res, 5898590745.674)

    def test_seventh_calculation2(self):
        F = Formuls(199)
        res = F.formul_2()
        self.assertEqual(res, 26426588.274)

    def test_seventh_calculation3(self):
        F = Formuls(199)
        res = F.formul_3()
        self.assertEqual(res, 57555.57600000001)

    def test_seventh_calculation4(self):
        F = Formuls(199)
        res = F.formul_4()
        self.assertEqual(res, 1266.436)

    def test_eighth_calculation1(self):
        F = Formuls(192.3)
        res = F.formul_1()
        self.assertEqual(res, 5143964060.866511)

    def test_eighth_calculation2(self):
        F = Formuls(192.3)
        res = F.formul_2()
        self.assertEqual(res, 23842145.218350004)

    def test_eighth_calculation3(self):
        F = Formuls(192.3)
        res = F.formul_3()
        self.assertEqual(res, 53761.17639000001)

    def test_eighth_calculation4(self):
        F = Formuls(192.3)
        res = F.formul_4()
        self.assertEqual(res, 1223.7972)

    def test_ninth_calculation1(self):
        F = Formuls(200)
        res = F.formul_1()
        self.assertEqual(res, 6017962890.6)

    def test_ninth_calculation2(self):
        F = Formuls(200)
        res = F.formul_2()
        self.assertEqual(res, 26827644.0)

    def test_ninth_calculation3(self):
        F = Formuls(200)
        res = F.formul_3()
        self.assertEqual(res, 58133.0)

    def test_ninth_calculation4(self):
        F = Formuls(200)
        res = F.formul_4()
        self.assertEqual(res, 1272.8)

    def test_tenth_calculation1(self):
        F = Formuls(300)
        res = F.formul_1()
        self.assertEqual(res, 30435863805.9)

    def test_tenth_calculation2(self):
        F = Formuls(300)
        res = F.formul_2()
        self.assertEqual(res, 90691386.0)

    def test_tenth_calculation3(self):
        F = Formuls(300)
        res = F.formul_3()
        self.assertEqual(res, 130429.5)

    def test_tenth_calculation4(self):
        F = Formuls(300)
        res = F.formul_4()
        self.assertEqual(res, 1909.2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
    def test_eleventh_calculation1(self):
        F = Formuls("-2")
        res = F.formul_1()
        self.assertEqual(res, NonPositiveIncorrect entry)

    def test_eleventh_calculation2(self):
        F = Formuls("0")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_eleventh_calculation3(self):
        F = Formuls("-1")
        res = F.formul_3()
        self.assertEqual(res, NonPositiveIncorrect entry)

    def test_eleventh_calculation4(self):
        F = Formuls("-199")
        res = F.formul_4()
        self.assertEqual(res, NonPositiveIncorrect entry)

    def test_twelfth_calculation1(self):
        F = Formuls("151")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twelfth_calculation2(self):
        F = Formuls("2df02")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twelfth_calculation3(self):
        F = Formuls("15dffdff1")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twelfth_calculation4(self):
        F = Formuls("-151")
        res = F.formul_4()
        self.assertEqual(res, NonPositiveIncorrect entry)

    def test_thirteenth_calculation1(self):
        F = Formuls("0-")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_thirteenth_calculation2(self):
        F = Formuls("0-")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_thirteenth_calculation3(self):
        F = Formuls("0-")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_thirteenth_calculation4(self):
        F = Formuls("0-")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_fourteenth_calculation1(self):
        F = Formuls("=1")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_fourteenth_calculation2(self):
        F = Formuls("=1")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_fourteenth_calculation3(self):
        F = Formuls("=1")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_fourteenth_calculation4(self):
        F = Formuls("=1")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_fifteenth_calculation1(self):
        F = Formuls("k0771+")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_fifteenth_calculation2(self):
        F = Formuls("k0771+")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_fifteenth_calculation3(self):
        F = Formuls("k0771+")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_fifteenth_calculation4(self):
        F = Formuls("k0771+")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_sixteenth_calculation1(self):
        F = Formuls("lkj")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_sixteenth_calculation2(self):
        F = Formuls("lkj")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_sixteenth_calculation3(self):
        F = Formuls("lkj")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_sixteenth_calculation4(self):
        F = Formuls("lkj")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_seventeenth_calculation1(self):
        F = Formuls("*5+")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_seventeenth_calculation2(self):
        F = Formuls("*5+")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_seventeenth_calculation3(self):
        F = Formuls("*5+")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_seventeenth_calculation4(self):
        F = Formuls("*5+")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_eighteenth_calculation1(self):
        F = Formuls("98u")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_eighteenth_calculation2(self):
        F = Formuls("98u")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_eighteenth_calculation3(self):
        F = Formuls("98u")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_eighteenth_calculation4(self):
        F = Formuls("98u")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_nineteenth_calculation1(self):
        F = Formuls("  `")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_nineteenth_calculation2(self):
        F = Formuls("  `")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_nineteenth_calculation3(self):
        F = Formuls("  `")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_nineteenth_calculation4(self):
        F = Formuls("  `")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twentieth_calculation1(self):
        F = Formuls("/74k")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twentieth_formul_2(self):
        F = Formuls("/74k")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twentieth_calculation3(self):
        F = Formuls("/74k")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twentieth_calculation4(self):
        F = Formuls("/74k")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_first_calculation1(self):
        F = Formuls("одisd")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_first_calculation2(self):
        F = Formuls("одisd")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_first_calculation3(self):
        F = Formuls("одisd")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_first_calculation4(self):
        F = Formuls("одisd")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_second_calculation1(self):
        F = Formuls("sd484")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_second_calculation2(self):
        F = Formuls("sd484")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_second_calculation3(self):
        F = Formuls("sd484")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_second_calculation4(self):
        F = Formuls("sd484")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_third_calculation1(self):
        F = Formuls("ada84вм")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_third_calculation2(self):
        F = Formuls("ada84вм")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_third_calculation3(self):
        F = Formuls("ada84вм")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_third_calculation4(self):
        F = Formuls("ada84вм")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fourth_calculation1(self):
        F = Formuls("фвісы2ыс15")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fourth_calculation2(self):
        F = Formuls("фвісы2ыс15")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fourth_calculation3(self):
        F = Formuls("фвісы2ыс15")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fourth_calculation4(self):
        F = Formuls("фвісы2ыс15")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fifth_calculation1(self):
        F = Formuls("48увсdv84")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fifth_calculation2(self):
        F = Formuls("48увсdv84")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fifth_calculation3(self):
        F = Formuls("48увсdv84")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_fifth_calculation4(self):
        F = Formuls("48увсdv84")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_sixth_calculation1(self):
        F = Formuls("lka462")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_sixth_calculation2(self):
        F = Formuls("lka462")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_sixth_calculation3(self):
        F = Formuls("lka462")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_sixth_calculation4(self):
        F = Formuls("lka462")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_seventh_calculation1(self):
        F = Formuls("*5+a4сі")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_seventh_calculation2(self):
        F = Formuls("*5+a4сі")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_seventh_calculation3(self):
        F = Formuls("*5+a4сі")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_seventh_calculation4(self):
        F = Formuls("*5+a4сі")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_eighth_calculation1(self):
        F = Formuls("9a4841ccd8u")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_eighth_calculation2(self):
        F = Formuls("9a4841ccd8u")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_eighth_calculation3(self):
        F = Formuls("9a4841ccd8u")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_eighth_calculation4(self):
        F = Formuls("9a4841ccd8u")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_ninth_calculation1(self):
        F = Formuls("511`  `")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_ninth_calculation2(self):
        F = Formuls("511`  `")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_ninth_calculation3(self):
        F = Formuls("511`  `")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_twenty_ninth_calculation4(self):
        F = Formuls("511`  `")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")

    def test_thirtieth_calculation1(self):
        F = Formuls("/74dac826k")
        res = F.formul_1()
        self.assertEqual(res, "Incorrect entry")

    def test_thirtieth_calculation2(self):
        F = Formuls("/74dac826k")
        res = F.formul_2()
        self.assertEqual(res, "Incorrect entry")

    def test_thirtieth_calculation3(self):
        F = Formuls("/74dac826k")
        res = F.formul_3()
        self.assertEqual(res, "Incorrect entry")

    def test_thirtieth_calculation4(self):
        F = Formuls("/74dac826k")
        res = F.formul_4()
        self.assertEqual(res, "Incorrect entry")


if __name__ == '__main__':
    unittest.main()
