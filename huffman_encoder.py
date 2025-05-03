def huffman_scramble(text, codebook):
    
    encoded = ''.join(codebook[char] for char in text)

    padding_length = 8 - len(encoded) % 8
    encoded_padded = encoded + '0' * padding_length  # Add padding (if necessary)

    # Convert the padded binary string into a byte array
    byte_array = bytearray()
    for i in range(0, len(encoded_padded), 8):
        byte_array.append(int(encoded_padded[i:i+8], 2))  # Convert each 8-bit chunk to a byte

    # Decode using latin-1, a safe 1-to-1 mapping
    ansi_like_string = byte_array.decode('latin-1')

    return ansi_like_string

def huffman_unscramble(encoded_text, codebook):

    # Convert the ansi-like string to a byte array
    byte_array = encoded_text.encode('latin-1')

    # Convert the byte array to a padded binary string
    binary_string = ''.join(f'{byte:08b}' for byte in byte_array)

    # Decode the binary string back to characters
    decoded_text = ''
    current_code = ''
    for bit in binary_string:
        current_code += bit
        if current_code in codebook:
            decoded_text += codebook[current_code]
            current_code = ''  # Reset current code after finding a match

    return decoded_text

def huffman_encode(text, codebook):
    
    encoded = ''.join(codebook[char] for char in text)

    padding_length = 8 - len(encoded) % 8
    encoded_padded = encoded + '0' * padding_length  # Add padding (if necessary)

    # Convert the padded binary string into a byte array
    byte_array = bytearray()
    for i in range(0, len(encoded_padded), 8):
        byte_array.append(int(encoded_padded[i:i+8], 2))  # Convert each 8-bit chunk to a byte

    return byte_array

def huffman_decode(binary_string, codebook):
    
    # Convert the byte array to a padded binary string
    # binary_string = ''.join(f'{byte:08b}' for byte in byte_array)

    # Decode the binary string back to characters
    decoded_text = ''
    current_code = ''
    for bit in binary_string:
        current_code += bit
        if current_code in codebook:
            decoded_text += codebook[current_code]
            current_code = ''  # Reset current code after finding a match
    
    return decoded_text