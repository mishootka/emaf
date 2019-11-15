import unittest
from parser import EMAFParser
from .fixtures import PARSER_TEST_DATA

class ParserTest(unittest.TestCase):

    def test_parser(self):

        for TEST_TOKEN in PARSER_TEST_DATA:
            test_line = TEST_TOKEN[0]   # source line
            test_parsed = TEST_TOKEN[1] # expected dict

            parser = EMAFParser(test_line)
            parsed = parser.get_parsed()
            record_type = parsed.get("record_type")

            # testing each field of the expected dict
            # against the actual parsed dict
            for key in test_parsed.keys():
                value = str(parsed.get(key))
                expected = str(test_parsed.get(key))
                error_message = "Record type {} key '{}' mismatch: {} != {}".format(
                    record_type, key, value, expected
                )
                self.assertEquals(value, expected, error_message)




if __name__ == '__main__':
    unittest.main()
