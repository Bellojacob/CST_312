# Jacob Bello
# CST 312
# 2/12/25
# Assignment 1

letter_to_number = {chr(i + 96): i for i in range(1, 27)}   # create a list of chars, each letter mapped to a number
number_to_letter = {v: k for k, v in letter_to_number.items()}  # added a mapping in reverse so we can search by num


def read_dict(dict_file):
    # open the en-US file as file
    with open(dict_file, "r") as file:
        # then for every word in the file, strip white space, and convert to lowercase
        return set(word.strip().lower() for word in file)
    
# this function will decrypt text based on a shift amount given
def decrypt(text, shift):
    result = ""
    for char in text:
        # check to see if every char is an ABC letter
        if char.isalpha():
            # so if it is then figure out what the shift is for that character
            shift_amount = (letter_to_number[char] - shift) % 26
            shift_amount = 26 if shift_amount == 0 else shift_amount  # ensure valid shift
            # we'll return that char
            result += number_to_letter[shift_amount]
        else:
            result += char  
    return result
    
# figure out what the best shift amount is
def get_shift(cipher, dictionary):
    best_shift = 0
    best_decryption = ""
    max_valid_words = 0
    
    # try all possible shift amounts and use the decrypt function from above
    for shift_iteration in range(1, 27):
        decrypted_text = decrypt(cipher, shift_iteration)
        words = decrypted_text.split()
        # count the number of words the are valid and in the dictionary file
        valid_word_count = sum(1 for word in words if word.lower().strip(".,!?\"") in dictionary)
        
        # determine if best shift amount, update best shift to shift the correct way and stay valid
        if valid_word_count > max_valid_words:
            max_valid_words = valid_word_count
            best_shift = shift_iteration
            best_shift = (26 - best_shift) % 26 if best_shift != 0 else 26
            best_decryption = decrypted_text
    
    return best_decryption, best_shift 

# decrypt the entire file, take parameters for file names, input, output, and the dictionary file
def decrypt_file(input_file, output_file, dict_file):
    dictionary_file = read_dict(dict_file)
    
    # open ciphertext
    with open(input_file, "r") as file:
        lines = file.readlines()
        
    decrypted_lines = []
    
    # for each line in the cipher, run method to get best shift, which will run our decryption as well, and then
    # with it decrypted, append to the list and print out to console as required
    for line in lines:
        plaintext, shift = get_shift(line.strip(), dictionary_file)
        decrypted_lines.append(f"{shift};{plaintext}\n")
        print(f"{shift};{plaintext}")
        
    # write to output file
    with open(output_file, "w") as file2:
        file2.writelines(decrypted_lines)
    
# our main method to enter the program
if __name__ == "__main__":
    input_file = input("Enter the ciphertext file name: ")
    output_file = "output.txt"
    dict_file = "en-US.dic"
    decrypt_file(input_file, output_file, dict_file)
