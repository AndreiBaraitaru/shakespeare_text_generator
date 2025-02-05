import re
import random
from collections import defaultdict

class NGramModel:
    def __init__(self, n=2):
        self.n = n
        self.ngram_counts = defaultdict(lambda: defaultdict(int))
        self.ngram_probs = defaultdict(dict)
    
    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z\\s]', '', text)
        tokens = text.split()
        return tokens
    
    def build_ngrams(self, tokens):
        for i in range(len(tokens) - self.n):
            ngram = tuple(tokens[i:i + self.n])
            next_token = tokens[i + self.n]
            self.ngram_counts[ngram][next_token] += 1
    
    def compute_probabilities(self):
        for ngram, next_words in self.ngram_counts.items():
            total_count = sum(next_words.values())
            self.ngram_probs[ngram] = {word: count / total_count for word, count in next_words.items()}
    
    def train(self, text):
        tokens = self.preprocess_text(text)
        self.build_ngrams(tokens)
        self.compute_probabilities()
    
    def get_next_word(self, ngram):
        if ngram not in self.ngram_probs:
            return None
        words, probs = zip(*self.ngram_probs[ngram].items())
        return random.choices(words, weights=probs, k=1)[0]
