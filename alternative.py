# program to make a users sentence alternate each letter between lowercase and uppercase
# also alternates every other word between lowercase and uppercase- both new sentences are printed

# defined function
def alternate_Uppercase_word(s):
    i = 0
    word_list = s.split(' ')
    alternate_upper = []
    for w in word_list:
        if i:
            alternate_upper.append(w.upper())
        else:
            alternate_upper.append(w)
        i = 1 - i
    return " ".join(alternate_upper)

# input variable
input_sentence = input("Enter a sentence: ")

# check for user error- if nothing is entered
if not input_sentence:
    print("Nothing has been entered!")
else:
    # main process sentence entered
    altered_sentence = ""
    i = 0
    for char in input_sentence:
        if i % 2 == 0:
            altered_sentence += char.upper()
        else:
            altered_sentence += char
        i += 1

    print("The sentence you entered looks like this with every other letter capitalized:")
    print(altered_sentence)

    print("The sentence you entered looks like this with every other word capitalized:")
    print(alternate_Uppercase_word(input_sentence))