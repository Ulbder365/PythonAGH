import re
from collections import Counter


def prepare_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:  # przesłonięcie symbolu wbudowanego
        text = file.read().lower()  # zły pomysł; proszę to zrobić z Wikipedią
        text = re.sub('[^\w\sąćęłńóśźż]+', '', text, flags=re.UNICODE)
        return text.split()


def count_words(filename, number):
    text = prepare_text(filename)
    positions = []
    counts = Counter(text)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    max_count = sorted_counts[number - 1][1]
    for count in sorted_counts:
        if count[1] >= max_count:
            positions.append(count)
    return positions


def count_ngrams(filename, number):
    text = prepare_text(filename)
    ngrams = []
    for i in range(len(text) - number + 1):
        ngram = ' '.join(text[i:i + number])
        ngrams.append(ngram)
    counts = Counter(ngrams)
    return len(counts)


textfile = 'potop.txt'
n = 10

words = count_words(textfile, n)
print(f" The top {n} most frequent words and their occurrences in text file {textfile}:")
for i, word in enumerate(words, 1):
    print(f"{i}. {word}")

n = 2
ngrams_count = count_ngrams(textfile, n)
print(f" Number of {n}-grams in text file {textfile}: {ngrams_count} ")

n = 3
ngrams_count = count_ngrams(textfile, n)
print(f" Number of {n}-grams in text file {textfile}: {ngrams_count} ")
