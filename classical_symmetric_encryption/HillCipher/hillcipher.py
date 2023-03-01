import numpy as np

def hill_enc(M, plaintext):
  c = ""
  plaintext = plaintext.replace(" ", "")
  k=[]
  p_ind_list = [ord(c) - 65 for c in plaintext]
  for i in range(0,len(p_ind_list), 3):
    c_arr = p_ind_list[i:i+3]
    c_val = np.matmul(c_arr, M)%26
    k+=[chr(c + 65) for c in c_val]
  c="".join(k)
  return c

def hill_dec(M, ciphertext):
  p=""
  ciphertext = ciphertext.replace(" ", "")
  c_ind_list = [ord(c) for c in ciphertext]
  invM= np.linalg.inv(M)
  k =[ ]
  for i in range(0, len(c_ind_list,), 3):
    c_arr = c_ind_list[i:i+3]
    p_val = np.matmul(c_arr, M)%26
    k+=[chr(c + 65) for c in p_val]
  p = "".join(k)
  return p

if __name__ == "__main__":
  input_matrix = np.array([[5,6,7],[6,7,3],[17,12,15]]) 
  input_plaintext = 'secret'                    
  ciphertext = hill_enc(input_matrix,input_plaintext)
  print("Ciphertext:", ciphertext)
  plaintext = hill_dec(input_matrix, ciphertext)
  print("plaintext", plaintext)