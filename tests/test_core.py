## http://www.mathblog.dk/tools/infix-postfix-converter/
## The above link provides readily available examples for use!
from .context import ezparse
import unittest
import math

# Simple Test.
test1_inf = "(12 - 3 ) / 3^2 + 2 * 3"
test1_rpn = [12, 3, "-", 3, 2, "^", "/", 2, 3, "*", "+"]
test1_fmt = ['(', '12', '-', '3', ')', '/', '3', '^', '2', '+', '2', '*', '3']
test1_ans = 7

# Complex test.
test2_inf = "( ( 1  + 2 ) / 3 ) ^ (4 * 6)"
test2_rpn = [1, 2, "+", 3, "/", 4, 6, "*", "^"]
test2_fmt = ['(', '(', '1', '+', '2', ')', '/', '3', ')', '^', '(', '4', '*',
                 '6', ')']
test2_ans = 1

# Float test.
test3_inf = "( 1 + 2 ) * ( 3 / 4 ) ^ ( 5 + 6 )"
test3_rpn = [1, 2, "+", 3, 4, "/", 5, 6, "+", "^", "*"]
test3_fmt = ['(', '1', '+', '2', ')', '*', '(', '3', '/', '4', ')', '^', '(',
                 '5', '+', '6', ')']
test3_ans = 0.12670540809631348

# Function test.
test4_inf = "max((2 + 3) / 5 * min(5, 2 + 2), 10)"
test4_rpn = [2, 3, "+", 5, "/", 5, 2, 2, "+", "min", "*", 10, "max"]
test4_fmt = ['max', '(', '(', '2', '+', '3', ')', '/', '5', '*', 'min', '(',
                 '5', ',', '2', '+', '2', ')', ',', '10', ')']
test4_ans = 10


class TestParserCore(unittest.TestCase):

    def setUp(self):
        self.parser = ezparse.Parser()

    ## RPN TESTS

    def test_simple_rpn(self):
        self.assertEqual(test1_rpn, self.parser.rpn(test1_inf))

    def test_complex_rpn(self):
        self.assertEqual(test2_rpn, self.parser.rpn(test2_inf))

    def test_float_rpn(self):
        self.assertEqual(test3_rpn, self.parser.rpn(test3_inf))

    def test_function_rpn(self):
        self.assertEqual(test4_rpn, self.parser.rpn(test4_inf))

    ## FORMAT TESTS

    def test_simple_format(self):
        self.assertEqual(test1_fmt, self.parser._format(test1_inf))

    def test_complex_format(self):
        self.assertEqual(test2_fmt, self.parser._format(test2_inf))

    def test_float_format(self):
        self.assertEqual(test3_fmt, self.parser._format(test3_inf))

    def test_function_format(self):
        self.assertEqual(test4_fmt, self.parser._format(test4_inf))

    ## ANSWER TESTS

    def test_simple_answer(self):
        self.assertEqual(test1_ans, self.parser(test1_inf))

    def test_complex_answer(self):
        self.assertEqual(test2_ans, self.parser(test2_inf))

    def test_float_answer(self):
        self.assertAlmostEqual(test3_ans, self.parser(test3_inf))

    def test_function_answer(self):
        self.assertEqual(test4_ans, self.parser(test4_inf))


if __name__ == '__main__':
    unittest.main()
