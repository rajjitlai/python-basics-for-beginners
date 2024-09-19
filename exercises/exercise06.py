# Letter frequency checker

def frequency(sentence):
    freq = {}
    
    for letter in sentence:
        if letter.isalpha():
            letter = letter.lower()
            freq[letter] = freq.get(letter, 0) + 1
        else: 
            print("Not a letter")
        
    return freq
    
sentence = input("Write something in your mind: ")
letter_dict = frequency(sentence)
letters = sorted(letter_dict)

for letter in letters:
    print(letter, letter_dict[letter])
    
print("Code ran with 0 errors")