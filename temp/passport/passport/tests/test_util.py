"""Tests the util module"""
import passport.util as util
import unittest


class UtilTest(unittest.TestCase):
    """Contains tests for util module"""
    lengths = [0, 1, 2, 5, 10, 15, 20, 23, 30, 35, 40]

    def test_rng_length(self):
        """Test that length return by rng is as required"""
        for length in self.lengths:
            generated = util.generate_random_bytes(length)
            self.assertEqual(length, len(generated))

    def test_xor(self):
        """Test custom left XOR"""
        data = (("0011", "0101", "0110"),
                ("1110", "1001", "0111"),
                ("1100001", "0000000", "1100001"),
                ("11100101010", "1001", "01110101010"),
                ("1100001", "000000001111", "110000101111"))
        for test in data:
            self.assertEqual(util.left_xor(test[0], test[1]), test[2])

    def test_xor_wrong_types(self):
        """Test that custom left XOR fails when provided wrong types"""
        data = (b"1010", True, None, 1, 3.4)
        for test in data:
            self.assertRaises(TypeError, util.left_xor, test, test)

    def test_xor_wrong_data(self):
        """Test that custom left XOR fails when provided wrong data"""
        data = ("102", "10a", "10.", "10A")
        for test in data:
            self.assertRaises(ValueError, util.left_xor, test, test)

    def test_generated_password(self):
        """Tests random password generator for length"""
        for length in self.lengths:
            password = util.generate_password(length)
            self.assertEqual(length, len(password))


