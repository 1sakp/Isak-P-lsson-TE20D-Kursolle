alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
index = []

word = input("Write a word to encrypt:  ")
shift_num = input("Shift by num:    ")

word_split = list(word)



def encrypt():
    for i in range(len(word_split)):
        temp_var = alphabet.index(word_split[i])
        temp_var += int(shift_num)
        index.append(alphabet[temp_var])
    print(index)
    print(shift_num)
        

        
        
encrypt()