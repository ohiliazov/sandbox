from pathlib import Path

words_path = Path(__file__).parent / "words.txt"

with words_path.open() as file:
    words = [line.strip() for line in file.readlines()]

# cheatcodes:
# - collections.Counter
# - collections.defaultdict

counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1

print(counter)
