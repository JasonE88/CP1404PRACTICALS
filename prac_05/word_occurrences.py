"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""


def main():
    text = input("Text: ")
    count_word_occurrences(text)


def count_word_occurrences(text):
    words = text.split()
    word_counts = {}
    max_word_length = 0

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        max_word_length = max(max_word_length, len(word))

    sorted_word_counts = sorted(word_counts.items())

    for word, count in sorted_word_counts:
        print(f"{word:{max_word_length}} : {count}")


main()
