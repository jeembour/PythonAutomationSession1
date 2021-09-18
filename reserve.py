import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input_string = "Let us make it now or never"
        expected_result = "never or now it make us Let"

        output = self.reserve_string(input_string)
        self.assertEqual(expected_result, output)  # add assertion here

    def reserve_string(self, input_string: str):
        return " ".join(list(reversed(input_string.split())))

if __name__ == '__main__':
     unittest.main()
