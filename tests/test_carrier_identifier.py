# tests/test_carrier_identifier.py

import unittest
from nambazasimu.carrier_identifier import identify_carrier

class TestCarrierIdentifier(unittest.TestCase):

    def test_airtel_numbers(self):
        self.assertEqual(identify_carrier("+255684567890"), "Airtel")
        self.assertEqual(identify_carrier("255685567890"), "Airtel")
        self.assertEqual(identify_carrier("0684567890"), "Airtel")
        self.assertEqual(identify_carrier("+255784567890"), "Airtel")
        self.assertEqual(identify_carrier("255785567890"), "Airtel")
        self.assertEqual(identify_carrier("0784567890"), "Airtel")
        self.assertEqual(identify_carrier("+255694567890"), "Airtel")
        self.assertEqual(identify_carrier("255695567890"), "Airtel")
        self.assertEqual(identify_carrier("0694567890"), "Airtel")

    def test_vodacom_numbers(self):
        self.assertEqual(identify_carrier("+255754567890"), "Vodacom")
        self.assertEqual(identify_carrier("255755567890"), "Vodacom")
        self.assertEqual(identify_carrier("075567890"), "Vodacom")
        self.assertEqual(identify_carrier("+255764567890"), "Vodacom")
        self.assertEqual(identify_carrier("255765567890"), "Vodacom")
        self.assertEqual(identify_carrier("076567890"), "Vodacom")
        self.assertEqual(identify_carrier("+255744567890"), "Vodacom")
        self.assertEqual(identify_carrier("255745567890"), "Vodacom")
        self.assertEqual(identify_carrier("074567890"), "Vodacom")

    def test_tigo_numbers(self):
        self.assertEqual(identify_carrier("+255714567890"), "Tigo")
        self.assertEqual(identify_carrier("255715567890"), "Tigo")
        self.assertEqual(identify_carrier("071567890"), "Tigo")
        self.assertEqual(identify_carrier("+255654567890"), "Tigo")
        self.assertEqual(identify_carrier("255655567890"), "Tigo")
        self.assertEqual(identify_carrier("065567890"), "Tigo")
        self.assertEqual(identify_carrier("+255674567890"), "Tigo")
        self.assertEqual(identify_carrier("255675567890"), "Tigo")
        self.assertEqual(identify_carrier("067567890"), "Tigo")

    def test_zantel_numbers(self):
        self.assertEqual(identify_carrier("+255774567890"), "Zantel")
        self.assertEqual(identify_carrier("255775567890"), "Zantel")
        self.assertEqual(identify_carrier("077567890"), "Zantel")

    def test_halotel_numbers(self):
        self.assertEqual(identify_carrier("+255624567890"), "Halotel")
        self.assertEqual(identify_carrier("255625567890"), "Halotel")
        self.assertEqual(identify_carrier("062567890"), "Halotel")

    def test_ttcl_numbers(self):
        self.assertEqual(identify_carrier("+255734567890"), "TTCL")
        self.assertEqual(identify_carrier("255735567890"), "TTCL")
        self.assertEqual(identify_carrier("073567890"), "TTCL")

    def test_smile_numbers(self):
        self.assertEqual(identify_carrier("+255664567890"), "Smile")
        self.assertEqual(identify_carrier("255665567890"), "Smile")
        self.assertEqual(identify_carrier("066567890"), "Smile")

    def test_unknown_numbers(self):
        self.assertEqual(identify_carrier("+255804567890"), "Unknown")
        self.assertEqual(identify_carrier("255805567890"), "Unknown")
        self.assertEqual(identify_carrier("080567890"), "Unknown")

if __name__ == '__main__':
    unittest.main()