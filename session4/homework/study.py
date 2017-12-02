type_in_sentence = str(input("Your sentence: "))
sentence = type_in_sentence.lower()

alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alpha)

count = {}

for character in sentence:
    if character in alpha_list:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1

for i in count:
    print(i, count[i])
