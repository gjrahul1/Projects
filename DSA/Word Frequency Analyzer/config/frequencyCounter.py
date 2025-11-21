def count_word_frequency(words):
    
    frequency = {}

    for word in words.split():
        frequency[word] = frequency.get(word,0)+1

    return frequency