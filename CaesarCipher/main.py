

def caesar(text, shift_amount, mode):
    
    new_text = ''
    
    if mode == 'encode':
        cipher_direction = 1
    elif mode == 'decode':
        cipher_direction = -1
    
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
                
            shifted_position = position + (cipher_direction * shift_amount)
            
            if shifted_position > len(alphabet)-1 or shifted_position < 0:
                shifted_position = shifted_position + (-1 * cipher_direction * len(alphabet))
            
            new_text += alphabet[shifted_position]
            
        else:
            new_text += letter
        
    return new_text
            


if __name__ == '__main__': 
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    is_stop = False
    while not is_stop:
        direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n')
        
        if direction not in ['encode', 'decode']:
            print('Please type only \'encode\' or \'decode\'.')
            exit()
            
        text = input('Type your message:\n').lower()
        shift = int(input('Type the shift number:\n')) % 26

        new_text = caesar(text=text, shift_amount=shift, mode=direction)
        print(f'The {direction}d text is {new_text}')
        
        answer = input('ㅅType \'yes\' if you want to do again. Otherwise type \'no\': ').lower()
        if answer == 'no':
            print('Goodbye.')
            is_stop = True
        elif answer == 'yes':
            continue
        else:
            print('Wrong input.')
            is_stop = True