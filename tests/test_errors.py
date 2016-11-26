from .context import ezparse
import unittest


class TestParserErrors(unittest.TestCase):

    def setUp(self):
        self.parser = ezparse.Parser()

    def test(self):
        pass

if __name__ == '__main__':
    unittest.main()
