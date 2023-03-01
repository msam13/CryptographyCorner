def caesar_str_enc(plain_text, k):
    plain_text=plain_text.upper()
    ciphertext = ""
    for i in plain_text:
      if(i.isalpha()):
        ciphertext+= chr((ord(i)+k - 65)%26 + 65)
    return ciphertext

def caesar_str_dec(ciphertext, k):
  ciphertext=ciphertext.upper()
  plaintext = ""
  for i in ciphertext:
      if(i.isalpha()):
        plaintext+=chr((ord(i) - 65 -k)%26 + 65)
  return plaintext

if __name__ == "__main__":
    input_str = 'test string'
    k = 3
    encstr = caesar_str_enc(input_str, k)
    print("plaintext :%s \nCiphertext :%s\n\n"% (input_str ,encstr))
    decstr = caesar_str_dec(encstr, k)
    print("Ciphertext :%s \nPlaintext :%s\n\n"% (encstr, decstr))