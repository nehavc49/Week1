text = open('sample.txt', 'r', encoding='utf-8').read().lower()
for ch in '.,!?': text = text.replace(ch, '')
word_counts = {}
for word in text.split(): word_counts[word] = word_counts.get(word, 0) + 1
for word, count in word_counts.items(): print(f"{word}: {count}")
