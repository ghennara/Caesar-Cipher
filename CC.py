def CesarCypher(string, increment):
    alphabet = "1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM ~`?°"
    encrypt = ''
    index=0
 
    if increment<1 or increment>50:
        print('ENCRYPTION FAILED. Put a number in the (1-50) range, you idiot.')
    else:               
        for i in range(len(string)):
            for j in range(len(alphabet)):
                if string[i] == alphabet[j]:
                    if (j + increment)>(len(alphabet)-1):
                        index = j + increment - len(alphabet)
                        encrypt = encrypt + str(alphabet[index])
                    else:
                        encrypt = encrypt + str(alphabet[j+increment])

        return encrypt


def hackCesar(string, increment):
    alphabet = "1234567890qwertyuiop[]asdfghjkl;zxcvbnm,.!@#$%^&*()_+-=-{}:<>|QWERTYUIOPASDFGHJKLZXCVBNM ~`?°"
    encrypt = ''
 
    if increment<1 or increment>50:
        print('DECRYPTION FAILED. It had to be a number in the (1-50) range, you idiot.')
    else:               
        for i in range(len(string)):
            for j in range(len(alphabet)):
                if string[i] == alphabet[j]:
                    if (j - increment) < 0:
                        index = j + len(alphabet) - increment
                        encrypt = encrypt + str(alphabet[index])
                    else:
                        encrypt = encrypt + str(alphabet[j-increment])

        return encrypt