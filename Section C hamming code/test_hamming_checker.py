import unittest
import hamming_code_2


class test_hamming_checker(unittest.TestCase):

    value = ['0100100100010010', '0011011010100110', '0010101011111111', '0101011000111110', '0101101101101111',
             '0011110101010111', '0010000001001100', '0110000111001000', '0010001011010010', '0100110010100110',
             '0010101111000101', '0000111010101101', '0101101010100100', '0100111100111101', '0110111111000000']

    expected = ['0100100000010010', '0010011010100110', '0010101011111111', '0101011000111111', '0101001101101111',
                '0011110100010111', '0010000001101100', '0110000110001000', '0010001011010010', '0000110010100110',
                '0010001111000101', '0000111010111101', '0101101010100101', '0100111100111111', '0100111111000000']

    corr_bit = ['7', '3', 'No corrupted bit', '15', '4', '9', '10',
                '9', 'No corrupted bit', '1', '4', '11', '15', '14', '2']

    def test_hamm(self):
        for i in range(15):
            self.assertEqual(hamming_code_2.hamming_checker(
                test_hamming_checker.value[i]), test_hamming_checker.expected[i], 'The corrupted bit is in position '+test_hamming_checker.corr_bit[i])


if __name__ == '__main__':
    unittest.main()
