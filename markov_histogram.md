1. If you build a histogram, how many entries will it have?
    - It depends on the unique words
2. If you build a 1st order markov chain what structures will you need to create and how many?
    - Dictogram, list
3. If build a 2nd order markov chain, how would your structure change?
    - Use tuple (previous, current). Every time a new word is added, the tuple should be updated.
    - Updated tuple: (current, new)
    - The paired value is to keep track of the previous word and current word
4. Approximately how many of these structures will you have?
