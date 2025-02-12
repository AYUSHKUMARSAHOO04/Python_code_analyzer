import unittest
from app import analysis

class TestAnalysis(unittest.TestCase):
    def test_analyze_code(self):
        code = "import os\n\nprint(os.getcwd())"
        results = analysis.analyze_code(code)
        self.assertIsInstance(results, list)

if __name__ == '__main__':
    unittest.main()