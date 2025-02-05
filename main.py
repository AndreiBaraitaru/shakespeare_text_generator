import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from ngram_model import NGramModel
import random

def generate_text(model, seed, length=50):
    current_ngram = tuple(seed.lower().split())
    generated_text = list(current_ngram)

    for _ in range(length - len(current_ngram)):
        next_word = model.get_next_word(current_ngram)
        if not next_word:
            break
        generated_text.append(next_word)
        current_ngram = tuple(generated_text[-model.n:])

    return ' '.join(generated_text)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "data", "shakespeare.txt")
    
    with open(data_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    model = NGramModel(n=2)
    model.train(text)
    
    seed = "to be"
    generated_text = generate_text(model, seed, length=50)
    print(generated_text)
