# КасимовТР

import unittest
import main

# Программа должна работать с любым вводом в переменную input_text
input_text = 'text'


class TestMain(unittest.TestCase):


    def test_input_not_none(self):
        txt = main.get_params(input_text)
        self.assertIsNotNone(txt)


if __name__ == '__main__':
    unittest.main()
