# Input sentence
sentence = input("Enter a sentence: ")
# Split into words
words = sentence.split()
# Create dictionary
freq = {}
# Count frequency
for word in words:
    freq[word] = freq.get(word, 0) + 1
# Display result
print(freq)