import random #This library permit to get random words from us data.txt list.
import os

def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper()) # ".strip()" Remove spaces at the beginning and at the end of the string. ".upper()" change each letter in capital letter.
    return words

def run():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word = random.choice(data) #Here we chose the word randomly.
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list) #Here we assing underscores to each letter of the chosen word.
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system("clear") #If you are in Unix Max or Linuex use clear, if you are in windoes use cls.
        print("Guess a word!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Write a letter: ").strip().upper()
        assert letter.isalpha(), "Please, only use letters"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        if "_" not in chosen_word_list_underscores:
            os.system("clear")
            print("Yu WON! The word is", chosen_word)
            break

if __name__ == "__main__":
    run()