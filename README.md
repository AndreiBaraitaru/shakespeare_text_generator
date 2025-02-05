# Shakespearean Text Generator

## Overview
This project implements an n-gram-based text generator to mimic the style of Shakespeare. It supports bigrams, trigrams, and quadgrams to generate text based on a given seed phrase.

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
