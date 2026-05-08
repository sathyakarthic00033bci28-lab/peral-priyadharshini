def count_unique_words(sentence):
 words = sentence.lower().split()
  unique_words = set(words)
   return len(unique_words)
