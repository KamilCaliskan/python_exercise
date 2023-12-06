'''
Consider that vowels in the alphabet are a, e, i, o, u and y.

Function score_words takes a list of lowercase words as an argument and returns a score as follows:

The score of a single word is
if the word contains an even number of vowels. Otherwise, the score of this word is

The score for the whole list of words is the sum of scores of all words in the list.

Debug the given function score_words such that it returns a correct score
'''

def is_vowel(letter):
    return letter in 'aeiouy'

def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum(1 for letter in word if is_vowel(letter))
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

# Sample Input
n = int(input().strip())
words = input().split()

# Output the result
print(score_words(words))
