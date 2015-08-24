import nltk
from sys import argv
script, filename = argv

# Open a text file
corpus_file = open(filename, 'rU')
print "Opened file", filename

# Read the file in as a string
# Note that for huge files, there are better ways to
# do this
text = corpus_file.read()

print "Loaded text (first 50 chars):"
print repr(text[:50])
print

# Tokenize the input
print "Tokenizing..."
raw_tokens = nltk.word_tokenize(text)

# Tokenization doesn't do anything to clean up the tokens
print "Tokenizer output (first 50), note the capitalization:"
print raw_tokens[:50]
print

# Let's normalize all the tokens for case
# Calling .lower() on a string returns a lowercase
# version of it
# lower_tokens = [token.lower() for token in raw_tokens]
# print "Lowercased tokens (first 50):"
# print lower_tokens[:50]
# print

# Now let's take punctuation out of the mix by
# filtering the list comprehension
# .isalpha() returns false if a string contains
# non-alphabetic characters
clean_tokens = [token.lower() for token in raw_tokens if token.isalpha()]
print "Alphabetic tokens (first 50), note no punctuation:"
print clean_tokens[:50]
print

# Now let's compute some statistics
# Build a frequency distribution from the clean tokens
fd = nltk.FreqDist(clean_tokens)
print "Corpus statistics:"

# How many tokens are there?
# .N() gives us the total number of outcomes recorded
# .B() gives us the unique outcomes (Bins)
print "Token count:", fd.N()
print "Type count:", fd.B()

# We can get the frequency of a word by treating the
# FreqDist as a dict and looking up a word
# print "Occurences of 'darcy':", fd['darcy']
# print "Occurences of 'love':", fd['love']
# print "Occurences of 'money':", fd['money']
# print "Occurences of 'pounds':", fd['pounds']

# Find out how many tokens end in -ed
# We just ask for the length of the list of tokens
# that end in -ed
print "Tokens that end in -ed:", len([token for word in clean_tokens if word.endswith('ed')])

# If we want the number of types, we can use the keys of the
# FreqDist
print "Tokens that end in -ed:", len([token for word in fd if word.endswith('ed')])

# For the grand finale, plot the frequencies of the top tokens
fd.plot(75)











