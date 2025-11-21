import argparse
import time
from colorama import Fore, Style
from config.cleantext import clean_text
from config.frequencyCounter import count_word_frequency
from config.clean_print import clean_print

def analyze_text(preprocessing,countalgorithm, sample_text:str) -> dict:
     cleaned_text = preprocessing(sample_text)
     return countalgorithm(cleaned_text)

def interactive_mode(preprocessing, countalgorithm):
     print(Fore.CYAN+"Welcome to Word Frequeny Analyzer"+Style.RESET_ALL)
     print(Fore.CYAN+"---------------------------------"+Style.RESET_ALL)
     print("Enter a sentence to check the frequency count for. Enter 0 to exit")

     while True:
       sample_text = input(Fore.LIGHTCYAN_EX+">>> "+Style.RESET_ALL).lower().strip()
       if sample_text == "0":
           print("Exiting...")
           time.sleep(1)
           break

       result = analyze_text(preprocessing,countalgorithm,sample_text)
       print(f"Word Frequencies \n")
       clean_print(result)
       print("-"*40)

def argument_mode(preprocessing,countalgorithm,sample_text):
    result = analyze_text(preprocessing,countalgorithm,sample_text.lower())
    clean_print(result)

       

def main():
    parser = argparse.ArgumentParser(description="Word Frequency Analyzer CLI Tool")

    parser.add_argument(
        "-t","--text",
        type=str,
        help="Sentence to analyze directly (non-interactive mode)"
    )

    args = parser.parse_args()

    if args.text:
        argument_mode(clean_text,count_word_frequency,args.text)

    else:
        interactive_mode(clean_text,count_word_frequency)

if __name__ == "__main__":
    main()
    