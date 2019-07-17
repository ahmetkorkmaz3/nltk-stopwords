from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

data = input("Please enter sentence: ")

stop_words = set(stopwords.words('english'))

words_token = word_tokenize(data)

words_filtered = []

for w in words_token:
    if w not in stop_words:
        words_filtered.append(w)

print("Words in the sentence")
print(words_token)
print("After filtering")
print(words_filtered)
