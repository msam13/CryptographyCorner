def vigenere_enc(plaintext, keyword,):
  ciphertext=""
  p_text = plaintext.replace(" ", "")
  p_text = p_text.upper()
  p_ind_list = [ord(c) - 65 for c in p_text]
  k_ind_list = [ord(c) - 65 for c in keyword]
  for i in range(len(p_ind_list)):
    ciphertext = ciphertext +  chr((p_ind_list[i] + k_ind_list[i%len(keyword)])%26 +65 )
  return ciphertext

def vigenere_dec(ciphertext, keyword):
  plaintext =""
  c_text = ciphertext.replace(" ", "")
  c_text = c_text.upper()
  c_ind_list = [ord(c) - 65 for c in c_text]
  k_ind_list = [ord(c) - 65 for c in keyword]
  for i in range(len(c_ind_list)):
    plaintext = plaintext +  chr((c_ind_list[i] - k_ind_list[i%len(keyword)])%26 +65)
  return plaintext


if __name__ == "__main__":
  input_str = 'bbbb' 
  input_key = 'abc'                    
  encstr = vigenere_enc(input_str,input_key)
  print("plaintext :%s \nCiphertext :%s\n\n"% (input_str ,encstr))
  decstr = vigenere_dec(encstr,input_key)
  print("Ciphertext :%s \nPlaintext :%s\n\n"% (encstr, decstr))
