import unittest
from ngram_model import NGramModel

class TestNGramModel(unittest.TestCase):
    def setUp(self):
        self.text = "to be or not to be that is the question"
        self.model = NGramModel(n=2)
        self.model.train(self.text)
    
    def test_preprocessing(self):
        tokens = self.model.preprocess_text(self.text)
        self.assertEqual(tokens, ["to", "be", "or", "not", "to", "be", "that", "is", "the", "question"])
    
    def test_ngram_counts(self):
        self.assertIn(("to", "be"), self.model.ngram_counts)
        self.assertGreaterEqual(self.model.ngram_counts[("to", "be")]["or"], 1)
    
    def test_probability_distribution(self):
        self.model.compute_probabilities()
        self.assertAlmostEqual(sum(self.model.ngram_probs[("to", "be")].values()), 1.0)
    
    def test_generate_next_word(self):
        word = self.model.get_next_word(("to", "be"))
        self.assertIsInstance(word, str)

if __name__ == "__main__":
    unittest.main()