# shakespeare_text_generator

# Shakespearean Text Generator

## Overview
This project implements an n-gram-based text generator to mimic the style of Shakespeare. It supports bigrams, trigrams, and quadgrams to generate text based on a given seed phrase.

## Folder Structure
```
shakespeare_text_generator/
│── data/
│   └── shakespeare.txt   # Shakespeare's works
│── src/
│   ├── ngram_model.py    # N-gram model implementation
│   ├── evaluation.py     # Human evaluation analysis
│   ├── tests.py          # Unit tests
│── main.py               # Entry point for running the project
│── README.md             # Project documentation
│── requirements.txt      # Dependencies
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/AndreiBaraitaru/shakespeare_text_generator.git
   cd shakespeare_text_generator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the text generator with:
```sh
python main.py
```

## Testing
Run unit tests using:
```sh
python -m unittest src/tests.py
```

## Evaluation
A survey CSV is generated for human evaluation of the generated text. You need to run evaluation.py for the csv to be generated. Make sure you are in the proper folder.
```sh
python -m unittest src/evaluation.py
```

## Extra
If you have any questions, please reach out to me :D