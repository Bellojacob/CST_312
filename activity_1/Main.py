# Jacob Bello
# CST 312
# Assignment 1, Frequency Analysis

with open("ciphertext.txt", "r") as file:
    content = file.read()
    
characters = list(content)

print("ORIGINAL TEXT")
print(content)
# print(characters)

print("DECRYPTED TEXT")
for i in range (len(characters)):
    
    # pretty sure
    if characters[i] == 'y':
        characters[i] = "t"
        
    elif characters[i] == 't':
        characters[i] = 'h'
        
    elif characters[i] == 'n':
        characters[i] = 'e'
        
    # not so sure
    
    elif characters[i] == 'v':
        characters[i] = 'a'
        
    elif characters[i] == 'u':
        characters[i] = 'n'
        
    elif characters[i] == 'p':
        characters[i] = 'd'
        
    elif characters[i] == 'x':
        characters[i] = 'o'
        
    elif characters[i] == 'q':
        characters[i] = 's'
        
    elif characters[i] == 'a':
        characters[i] = 'c'
        
    elif characters[i] == 'h':
        characters[i] = 'r'
        
    elif characters[i] == 'd':
        characters[i] = 'y'
        
    elif characters[i] == 'z':
        characters[i] = 'u'

    elif characters[i] == 'l':
        characters[i] = 'w'
        
    elif characters[i] == 'm':
        characters[i] = 'i'
        
    elif characters[i] == 'c':
        characters[i] = 'm'
        
    elif characters[i] == 'g':
        characters[i] = 'b'
        
    elif characters[i] == 'r':
        characters[i] = 'g'
        
    elif characters[i] == 'b':
        characters[i] = 'f'
    elif characters[i] == 'i':
        characters[i] = 'l'
    elif characters[i] == 'f':
        characters[i] = 'v'
    elif characters[i] == 'e':
        characters[i] = 'p'
    elif characters[i] == 'j':
        characters[i] = 'q'
    elif characters[i] == 'o':
        characters[i] = 'j'
    elif characters[i] == 'k':
        characters[i] = 'x'
    elif characters[i] == 's':
        characters[i] = 'k'
newText = "".join(characters)
print(newText)

with open("cracked-code.txt", "w") as decrypted_file:
    decrypted_file.write(newText)