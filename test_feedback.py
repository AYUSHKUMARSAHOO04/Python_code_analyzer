import unittest
from app import feedback

class TestFeedback(unittest.TestCase):
    def test_generate_feedback(self):
        analysis_results = [{'line': 1, 'message': 'Unused import os'}]
        results = feedback.generate_feedback(analysis_results)
        self.assertIsInstance(results, list)
        self.assertEqual(results[0]['suggestion'], 'Consider removing the unused import statement.')

if __name__ == '__main__':
    unittest.main()