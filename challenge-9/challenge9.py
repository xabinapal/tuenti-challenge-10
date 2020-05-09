def parse_ciphered(cipher_text):
    split_text = []
    for index in range(0, len(cipher_text), 2):
        split_text.append(cipher_text[index : index + 2])
    cipher_nums = [int(x, 16) for x in split_text]
    return cipher_nums

def get_key():
    text = "514;248;980;347;145;332"
    ciphered = "3633363A33353B393038383C363236333635313A353336"

    cipher_nums = parse_ciphered(ciphered)

    key_nums = []
    for i in range(len(text)):
        k = ord(text[i]) ^ cipher_nums[i]
        key_nums.append(k)

    return (''.join(str(x) for x in key_nums))[::-1]

def decipher(cipher, key):
    cipher_nums = parse_ciphered(cipher)
    deciphered = ""
    for x in range(len(cipher_nums)):
        deciphered += chr(cipher_nums[x] ^ int(key[len(key) - 1 - x]))
    return deciphered

key = get_key()

ciphered = "3A3A333A333137393D39313C3C3634333431353A37363D"
print(decipher(ciphered, key))
