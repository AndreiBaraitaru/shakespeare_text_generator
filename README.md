# Shakespearean Text Generator

## Overview
This project is an n-gram-based text generator that mimics the writing style of William Shakespeare. It processes Shakespeare's works, learns how words are structured, and generates text by predicting the most likely next word based on prior words.

## How It Works
1. **Reads and Preprocesses Shakespeare's Text**  
   - Converts it to lowercase, removes punctuation, and tokenizes it into words.
   
2. **Builds N-Grams (Word Sequences)**  
   - Creates bigrams (2-grams), trigrams (3-grams), and quadgrams (4-grams) from the text.
   
3. **Counts Word Occurrences**  
   - Tracks how often a word follows a given n-gram.
   
4. **Calculates Probabilities**  
   - Determines the likelihood of each word appearing after an n-gram.
   
5. **Generates Text**  
   - Uses probabilities to predict and generate text based on an input seed phrase.

## Example Output
If trained correctly, running:
```python
generate_text(model, "to be", length=10)
```
Might return:
```
"to be or not to be that is the question"
```

## Applications
✔ **Text prediction** (auto-complete in search engines)  
✔ **Text generation** (imitating Shakespeare or other styles)  
✔ **Analyzing word relationships** (understanding word pairings in literature)  


## Folder Structure
~~~
shakespeare_text_generator/
│── data/
│   └── shakespeare.txt   # The file I am using for the Shakespeare text
│── src/
│   ├── ngram_model.py    # The n-gram model implementation file where we do the preprocessing, build the n-grams and compute the probabilities
│   ├── evaluation.py     # Human evaluation analysis
│   ├── tests.py          # Unit tests file
│── main.py               # Entry point for running the project, run before you run the other files!!
│── README.md             # Project documentation
│── requirements.txt      # Dependencies, no need to install them if you already have the libraries installed locally 
~~~

## Installation
1. Clone the repository:
   
   git clone https://github.com/AndreiBaraitaru/shakespeare_text_generator.git <br>
   cd shakespeare_text_generator
   
3. Install dependencies:
   
   pip install -r requirements.txt
   

## Usage
Run the text generator with python main.py. It's important you first run main.py before running the tests or evaluation.

python main.py


## Testing
Run unit tests using:

python -m unittest src/tests.py


## Evaluation
A survey CSV is generated for human evaluation of the generated text. You need to run evaluation.py for the csv to be generated. Make sure you are in the proper folder.

python -m unittest src/evaluation.py

## Extra
If you have any questions, please reach out to me :D
