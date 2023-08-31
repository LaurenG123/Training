#THE FOLLOWING CODE IS ADAPTED FROM THE SPARTA GLOBAL LEARNING PATHWAY
#CODE FROM MY COMPILER


# Seven lists of letters
letter_list_0 = ['a', 'e', 'i', 'o', 'u']
letter_list_1 = ['b', 'c', 'm', 'p']
letter_list_2 = ['d', 'g']
letter_list_3 = ['f', 'h', 'v', 'w', 'y']
letter_list_4 = ['k']
letter_list_5 = ['j', 'x']
letter_list_6 = ['q', 'z']


def calculate_scrabble_score(word, letter_scores, letter_lists):
    word = word.lower()
    score = sum(letter_scores[letter] for letter in word)

    letter_counts = {}
    for letter in word:
        for i, letters in enumerate(letter_lists):
            if letter in letters:
                if i not in letter_counts:
                    letter_counts[i] = 1
                else:
                    letter_counts[i] += 1
                break

    return score, letter_counts


# Adapted Letter scores to use dictionary format for easy changes
letter_scores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

letter_lists = [letter_list_0, letter_list_1, letter_list_2, letter_list_3, letter_list_4, letter_list_5, letter_list_6]

word = input("Enter a word: ")
score, letter_counts = calculate_scrabble_score(word, letter_scores, letter_lists)

print(f"The score of '{word}' in Scrabble is: {score}")
for i, count in letter_counts.items():
    print(f"Letter group {i}: {count} letters used")