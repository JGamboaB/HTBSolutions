def decode_hex_flag(raw_data):
    # Split the raw data into individual "words"
    words = raw_data.split()
    
    decoded_flag = []
    
    for word in words:
        # Remove any '0x' prefix
        word = word.replace('0x', '')
        
        # Split the word into pairs of characters
        pairs = [word[i:i+2] for i in range(0, len(word), 2)]
        
        # Convert each pair from hexadecimal to ASCII
        decoded_word = ''.join([chr(int(pair, 16)) for pair in pairs])
        
        decoded_flag.append(decoded_word)
    
    # Reverse the order of the decoded words
    decoded_flag.reverse()
    
    # Join the words to form the final flag
    flag = ''.join(decoded_flag)
    
    return flag[::-1] # Reverses the flag string to return it in the correct order

# Get raw data from the user
raw_data = input("Enter the raw data: ")

# Decode and print the flag
flag = decode_hex_flag(raw_data)
print("Decoded Flag:", flag)

