# Word Frequency Analyzer

A simple Python CLI tool that counts how often each word appears in a sentence or text input. This project was built as a basic DSA/Python exercise to practice dictionaries, string processing, and command-line arguments.

---

## Features
- Analyze word frequency from:
  - **Direct text input** using CLI (`--text "your sentence"`)
  - **Interactive input** (when no arguments are provided)
- Clean, minimal output showing each word and its count
- Uses only Python's built-in libraries
- Beginner-friendly and lightweight

---

## Usage

### 1. Analyze a sentence directly from the command line
```bash
python main.py --text "hello world hello"
```

### Output
```bash
hello : 2
world : 1
```

## How It Works

* Splits text by whitespace

* Counts words using a dictionary

* Prints the frequency directly in the terminal

* No punctuation removal, no stopword filtering, and no advanced preprocessing — the project is intentionally simple for learning purposes.

## Future Improvements 

* Convert all words to lowercase

* Remove punctuation

* Sort output by highest frequency

* Add support for reading from a file

* Export results to CSV

