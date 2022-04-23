#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def encryption(text,key):
    '''
    This is the Caesar encryption function that takes a text we want to encrypt and return it cipher
    Arguments: 
        text: the text you like to chiper.
        key: number of shifts you want the text be ciphered by. 
    '''
    encrypt = ''
    for char in text:
        if char.isupper():     # Ciphering the upper-case letters. 
            encrypt += chr((ord(char)+int(key)-65)%26 + 65)
        elif char.islower():  # Ciphering the lower-case letters.
            encrypt += chr((ord(char)+int(key)-97)%26 + 97)
        else:                # Ciphering the rest of characters.
            encrypt += chr((ord(char)+int(key)-32)%26 + 32)
    return encrypt
     

def decryption(text,key=False):
    '''
    This is the Caesar decryption function that takes a ciphered text we want to decrypt and return it original text.
    Arguments:
        text: the cipher you would like to Decrypt.
        key: (optional) the key used in encrypting; if the user doen't know it, the function will help.
    '''
    decrypt = ''
    if key:      # In the case of knowing what the key is, use this code.
        for char in text:
            if char.isupper():   # Decrypting the upper-case letters.
                decrypt += chr((ord(char)-int(key)-65)%26 + 65)
            elif char.islower(): # Decrypting the lower-case letters.
                decrypt += chr((ord(char)-int(key)-97)%26 + 97)
            else:               # Decrypting the rest of characters.
                decrypt += chr((ord(char)-int(key)-32)%26 + 32)
        return decrypt
    
    else:     # If the user doesn't know what the key is.
        print("If you don't know what the key is. No problem, We will help you!")
        print("we will try all the possible keys and it's your turn to decide which one looks like a human readable language \n")
        
        for key in range(26):
            print('{}- For Key = ({}), The first  100 characters in the original text would look like: '.format(key+1,key))
            for char in text[0:101]:
                if char.isupper():
                    decrypt += chr((ord(char)-int(key)-65)%26 + 65)
                elif char.islower():
                    decrypt += chr((ord(char)-int(key)-97)%26 + 97)
                else:
                    decrypt += chr((ord(char)-int(key)-32)%26 + 32) 
            print(decrypt+'\n----------------------------------------------------------------------------')
            decrypt = ''       



def caesar_cipher():
    '''
    This Function is a function used for cryptograpy, it uses Caesar-Cipher as the idea of ciphering.
    this function has the cababilities of both Encryption and Decryption.
    it first asks the user for the purpose of using the function:
        1- Encryption.
        2- Decryption.
    then Askes for the text and the key for Cophering.
    '''
    purpose = input('Please select the desired action to use this function: 1=Encryption, 2=Decryption: ')
    
    if purpose == '1':
        text = input('Please write down the text : ')
        key = int(input("Please select a key: "))
        return encryption(text,key)
    elif purpose == '2':
        text = input('Please write down the text : ')
        key = int(input("Please select a key, if you don't know it write (0): "))
        return decryption(text,key)
    else:
        print('Please you have to select between (1 & 2)')
        return
    
    
if __name__ == "__main__":
    caesar_cipher()

