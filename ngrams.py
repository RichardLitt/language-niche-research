from nltk.util import ngrams
from sys import argv
script, filename = argv

txt = open(filename)
n = 6

for line in txt:
  sixgrams = ngrams(line.split(), n)
  for grams in sixgrams:
    print grams
