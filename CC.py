def CaesarCipher(string, increment):
    alphabet = "1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM ~`?°"
    encrypt = ''

    if increment < 1 or increment > 50:
        print('ENCRYPTION FAILED. Put a number in the (1-50) range.')
    else:
        for char in string:
            if char in alphabet:
                index = (alphabet.index(char) + increment) % len(alphabet)
                encrypt += alphabet[index]
            else:
                encrypt += char

    return encrypt

def hackCaesar(string, increment):
    alphabet = "1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM ~`?°"
    decrypt = ''

    if increment < 1 or increment > 50:
        print('DECRYPTION FAILED. Put a number in the (1-50) range.')
    else:
        for char in string:
            if char in alphabet:
                index = (alphabet.index(char) - increment) % len(alphabet)
                decrypt += alphabet[index]
            else:
                decrypt += char

    return decrypt
    
