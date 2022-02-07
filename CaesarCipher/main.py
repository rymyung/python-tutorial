

def caesar(text, shift_amount, mode):
    
    new_text = ''
    for letter in text:
        position = alphabet.index(letter)
        
        if mode == 'encode':
            cipher_direction = 1
        elif mode == 'decode':
            cipher_direction = -1
            
        shifted_position = position + (cipher_direction * shift_amount)
        
        if shifted_position > len(alphabet)-1 or shifted_position < 0:
            shifted_position = shifted_position + (-1 * cipher_direction * len(alphabet))
        
        new_text += alphabet[shifted_position]
    
    return new_text
            


if __name__ == '__main__': 
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n')
    if direction not in ['encode', 'decode']:
        print('Please type only \'encode\' or \'decode\'.')
        exit()
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    new_text = caesar(text=text, shift_amount=shift, mode=direction)
    print(f'The {direction}d text is {new_text}')