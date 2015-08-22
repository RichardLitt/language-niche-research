import nltk
from nltk import bigrams
from nltk import trigrams
from nltk.util import ngrams
from sys import argv
script, filename = argv

text = open(filename)

for n in range (2,7):
  for line in text:
    tokens = nltk.word_tokenize(line)
    tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
    grams = ngrams(tokens, n)
    fdist = nltk.FreqDist(grams)
    print fdist.most_common()
  # for k,v in fdist.items():
  #    print v, k
  # print [(item, tri_tokens.count(item)) for item in sorted(set(tri_tokens))]


# ngrams
# for n in range(0,6):
#   for line in text:
#     for grams in ngrams(line.split(), n):
#       print grams
