from colorama  import Fore, Style

def clean_print(items):
    texts = sorted(items.items(), key = lambda x:x[1], reverse=True)
    max_len = max(len(value) for value, _ in texts)
    
    for key,value in texts:
        print(f"{Fore.GREEN+key.ljust(max_len)+Style.RESET_ALL}:",value)