import unittest
import subprocess
from main import model

class TestCcwc(unittest.TestCase):

    def setUp(self) -> None:
        self.path = ["test_data/big.txt","test_data/test1.txt"]
        result =  subprocess.run(["wc","test_data/big.txt"],capture_output="True",encoding='utf-8')

        self.metric = [int(results) for results in result.stdout.split(" ")[-4:-1]]

    def test_all_without_argument(self):
        self.assertEqual(model.number_of_lines(self.path[0]),self.metric[0],"number of lines")
        self.assertEqual(model.number_of_words(self.path[0]),self.metric[1],"number of words")
        self.assertEqual(model.number_of_chars(self.path[0]),self.metric[2],"number of chars")

    def test_number_of_lines(self):
        self.assertEqual(model.number_of_lines(self.path[0]),self.metric[0],"number of lines")

    def test_number_of_words(self):
        self.assertEqual(model.number_of_words(self.path[0]),self.metric[1],"number of words")
    
    def test_number_of_chars(self):
        self.assertEqual(model.number_of_chars(self.path[0]),self.metric[2],"number of chars")

if __name__== "__main__":
    unittest.main()