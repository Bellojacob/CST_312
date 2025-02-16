letter_to_number = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

def caesar_cipher_decrypt(text, shift):
    """Decrypts a given text by shifting letters backwards."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep spaces and punctuation as is
    return result

def load_dictionary(dictionary_file):
    """Loads dictionary words into a set."""
    with open(dictionary_file, "r") as f:
        return set(word.strip().lower() for word in f)

def find_best_shift(ciphertext, dictionary):
    """Tries all shifts and returns the most probable decryption."""
    best_shift = 0
    best_decryption = ""
    max_valid_words = 0
    
    for shift in range(1, 27):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        words = decrypted_text.split()
        valid_word_count = sum(1 for word in words if word.lower().strip(".,!?\"") in dictionary)
        
        if valid_word_count > max_valid_words:
            max_valid_words = valid_word_count
            best_shift = shift
            best_decryption = decrypted_text
    
    return best_decryption, best_shift

def decrypt_file(input_file, output_file, dictionary_file):
    """Reads ciphertexts, decrypts them, and writes output."""
    dictionary = load_dictionary(dictionary_file)
    
    with open(input_file, "r") as f:
        lines = f.readlines()
    
    decrypted_lines = []
    for line in lines:
        plaintext, shift = find_best_shift(line.strip(), dictionary)
        decrypted_lines.append(f"{shift};{plaintext}\n")
        print(f"{shift};{plaintext}")
    
    with open(output_file, "w") as f:
        f.writelines(decrypted_lines)
    
    print(f"Decryption complete! Results saved to {output_file}")

if __name__ == "__main__":
    input_filename = input("Enter the ciphertext file name: ")
    output_filename = "decrypted-messages.txt"
    dictionary_filename = "en-us.dic"
    decrypt_file(input_filename, output_filename, dictionary_filename)
