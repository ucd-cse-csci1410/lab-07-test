"""
test_01_is_prime_numbers.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the is_prime_numbers function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.main import is_prime_numbers



class TestIsPrimeNumbers(unittest.TestCase):
    """Test list_of_prime_numbers() by mocking input() and capturing printed output."""

    # case_01: input 18 → primes 2 3 5 7 11 13 17, composites 4 6 8 9 10 12 14 15 16 18 (with segregation)
    @patch('builtins.input', side_effect=['18'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_01_is_prime_numbers_for_18(self, mock_stdout, mock_input):
        is_prime_numbers()
        output = mock_stdout.getvalue()
        self.assertIn('2 3 5 7 11 13 17', output,
                      msg="Output should contain prime numbers: '2 3 5 7 11 13 17' for input 18. Verify spacing and ascending order.")
        self.assertIn('4 6 8 9 10 12 14 15 16 18', output,
                      msg="Output should contain composite numbers: '4 6 8 9 10 12 14 15 16 18' for input 18. Verify spacing and ascending order.")
  

    # case_02: input 2 → only prime 2
    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_02_prime_only_for_2(self, mock_stdout, mock_input):
        is_prime_numbers()
        output = mock_stdout.getvalue()
        self.assertIn('2', output,
                      msg="Output should contain prime numbers: '2' for input 2. Verify spacing and ascending order.")
        self.assertIn('There are no composite numbers in the range', output,
                      msg="Output should contain 'There are no composite numbers in the range' for input 2. Verify spacing and ascending order.")
  

    # case_03: invalid input then valid (e.g. 1 then 5)
    @patch('builtins.input', side_effect=['1', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_03_error_then_valid_input(self, mock_stdout, mock_input):
        is_prime_numbers()
        output = mock_stdout.getvalue()
        self.assertIn('Input Error: Number be greater than or equal to 2', output,
                      msg="Should print error when input is less than 2.")
        self.assertIn('2 3 5', output,
                      msg="Output should contain prime numbers: '2 3 5' for input 5. Verify spacing and ascending order.")
        self.assertIn('4', output,
                      msg="Output should contain composite numbers: '4' for input 5.")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestIsPrimeNumbers)
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)
