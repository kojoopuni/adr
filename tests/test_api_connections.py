"""
Tests for API connections
"""
import unittest
from unittest.mock import patch
from src.tools.amazon.junglescout import JungleScoutTool
from src.tools.ai.gpt4 import GPT4Tool
from src.tools.search.perplexity import PerplexityTool

class TestAPIConnections(unittest.TestCase):
    def setUp(self):
        self.junglescout = JungleScoutTool()
        self.gpt4 = GPT4Tool()
        self.perplexity = PerplexityTool()

    def test_junglescout_connection(self):
        with patch('src.tools.amazon.junglescout.JungleScoutTool._run') as mock_run:
            mock_run.return_value = "Success"
            result = self.junglescout._run("test query")
            self.assertEqual(result, "Success")

    def test_gpt4_connection(self):
        with patch('src.tools.ai.gpt4.GPT4Tool._run') as mock_run:
            mock_run.return_value = "Success"
            result = self.gpt4._run("test query")
            self.assertEqual(result, "Success")

    def test_perplexity_connection(self):
        with patch('src.tools.search.perplexity.PerplexityTool._run') as mock_run:
            mock_run.return_value = "Success"
            result = self.perplexity._run("test query")
            self.assertEqual(result, "Success")

if __name__ == '__main__':
    unittest.main()
