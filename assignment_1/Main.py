letter_to_number = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}


with open("sample-secret-message-caesar-ciphertext.txt", "r") as file:

    
# print(content)

    # iterate through each line in the specified txt file given
    for line in file:
        print("LINE: " + line)
        
        # from each line, separate each word in a list called word_list
        word_list = line.split()
        # now for each word in the word list, lets get the length of the word
        for word in word_list:
            # convert string to lowercase
            word = word.lower()
            # print(word)
            word_len = len(word)
            # print(word_len)
            
            # lets open the dictionary, and check for words that have the same length as our word above
            with open ("en-US.dic", "r") as dict_file:
                for term in dict_file:
                    term = term.strip().lower()
                    # term = term.replace("'", "")
                    # when we find a word with the same length, we want to break that word down character by character
                    if len(term) == word_len:
                        # print("This word matches our length requirement: " ,term)
                        # make a list of chars from the word from the dictionary
                        dict_word = list(term)
                        
                        
                        # we also break down the word from the text file
                        our_word = list(word)
                        # print("Our word:" , our_word)
                        
                        
                        # now lets take the first character, figure out the shift amount, apply that to the second character,
                        # if it doesn't match then we know this isn't the right word
                        cipher_index = letter_to_number.get(our_word[0], -1)
                        plain_index = letter_to_number.get(dict_word[0], -1)
                        # print("Cipher Index:", (cipher_index))
                        # print("Plain Index:", (plain_index))


                        if cipher_index == -1 or plain_index == -1:
                            continue  # Skip if characters aren't found

                        #for letter, number in letter_to_number.items():
                        #    if cipher_index != letter:
                        #        break
                        
                        #shift_amount = plain_index - cipher_index
                        shift_amount = (plain_index - cipher_index) % 26
                        
                        # print("Shift Amount: ", shift_amount)
                        
                        # now that we have a shift amount, lets shift every letter in our word and then check if that word exists
                        new_list = []
                        for char in our_word:
                            if char in letter_to_number:
                                temp = (letter_to_number[char] + shift_amount) % 26
                                temp = 26 if temp == 0 else temp  # Ensure it remains in 1-26 range
                                new_list.append([k for k, v in letter_to_number.items() if v == temp][0])
                            else:
                                new_list.append(char)  # If it's punctuation, keep it as is

                        new_word = "".join(new_list)
                        print("Decoded word:", new_word)
                        
                        
                            
        
                            
                        
            