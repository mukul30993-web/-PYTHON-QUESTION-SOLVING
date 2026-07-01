import string


def count_letters(text):
    letters = {}

    for ch in text.lower():
        if ch.isalpha():
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1

    return letters


def remove_punctuation(text):
    result = ""

    for ch in text:
        if ch not in string.punctuation:
            result += ch

    return result


def longest_word(sentence):
    words = sentence.split()

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def word_frequency(sentence):
    freq = {}

    words = sentence.lower().split()

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def replace_word(sentence, old, new):
    return sentence.replace(old, new)


def unique_words(sentence):
    words = sentence.split()
    return list(set(words))


text = input("Enter a paragraph: ")

clean = remove_punctuation(text)

print("Letter Count:")
print(count_letters(clean))

print()

print("Longest Word:")
print(longest_word(clean))

print()

print("Word Frequency:")
print(word_frequency(clean))

old = input("Word to Replace: ")
new = input("New Word: ")

print(replace_word(clean, old, new))

print("Unique Words:")
print(unique_words(clean))

print()

print("Total Characters:", len(clean))
print("Total Words:", len(clean.split()))

try:
    num = int(input("Enter Number: "))
    print(100 / num)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Finished")