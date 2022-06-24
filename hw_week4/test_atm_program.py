# TASK 3

import unittest
from atm_program import validate_pin_length, validate_pin_char, \
    validate_withdrawal_amount, validate_withdrawal_multiple


class TestAtmFunction(unittest.TestCase):
    def test_validate_pin_length_happy_path(self):
        expected = 'abcd'
        result = validate_pin_length('abcd')
        self.assertEqual(expected, result)

    def test_validate_pin_length_sad_path(self):
        with self.assertRaises(ValueError) as exception_context:
            validate_pin_length('abcde')
        self.assertEqual(
            str(exception_context.exception), 'PIN must be 4 digits.')

    def test_validate_pin_char_happy_path(self):
        expected = '1234'
        result = validate_pin_char('1234')
        self.assertEqual(expected, result)

    def test_validate_pin_char_sad_path(self):
        with self.assertRaises(TypeError) as exception_context:
            validate_pin_char('abcd')
        self.assertEqual(
            str(exception_context.exception), 'PIN must be digits only.')

    def test_validate_withdrawal_amount_happy_path(self):
        expected = '60'
        result = validate_withdrawal_amount('60')
        self.assertEqual(expected, result)

    def test_validate_withdrawal_amount_sad_path(self):
        with self.assertRaises(ValueError) as exception_context:
            validate_withdrawal_amount('700')
        self.assertEqual(
            str(exception_context.exception), 'Not a correct amount.')

    def test_validate_withdrawal_multiple_happy_path(self):
        expected = '70'
        result = validate_withdrawal_multiple('70')
        self.assertEqual(expected, result)

    def test_validate_withdrawal_multiple_sad_path(self):
        with self.assertRaises(ValueError) as exception_context:
            validate_withdrawal_multiple('22')
        self.assertEqual(
            str(exception_context.exception), 'Not a correct amount.')


if __name__ == '__main__':
    unittest.main()
