import pandas

nato_file=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_words=pandas.DataFrame(nato_file)
nato_words_dict={row.letter:row.code for (index,row) in nato_words.iterrows()}
print(nato_words_dict)

word=input("Enter a word: ").upper()
try:
    result=[nato_words_dict[letter] for letter in word]
    print(result)
except KeyError:
    print("Error please enter a singular word with only letters :) ")

