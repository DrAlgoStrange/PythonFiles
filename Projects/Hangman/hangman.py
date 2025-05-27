import random
word_list=['apple', 'brick', 'chair', 'dance', 'eagle', 'flame', 'grape', 'honey', 'ivory', 'jelly', 'knock', 'lemon', 'mango', 'noble', 'ocean', 'plant', 'queen', 'river', 'stone', 'tiger', 'uncle', 'vivid', 'wheat', 'xenon', 'youth', 'zebra']

choosen_word=random.choice(word_list)
# user_entered_string=choosen_word[0]+("_"*(len(choosen_word)-1))
print(choosen_word)
lives=4
compare_word=list(choosen_word[1:])
updatedstr=[choosen_word[0] if i==0 else "_" for i in range(len(choosen_word))]
print(updatedstr)


while lives!=0 and len(compare_word)!=0:
    print("Lives Left",lives)
    guess_letter=input("guess a letter")
    if guess_letter in compare_word:
        compare_word.remove(guess_letter)
        updatedstr[compare_word.index(guess_letter)]=guess_letter
        compare_word.remove(guess_letter)
    else:
        print("wrong guess")
        lives=lives-1