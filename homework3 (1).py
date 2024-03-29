# -*- coding: utf-8 -*-
"""homework3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PPnveIdwnp0T2oqyw8cUv9HPv16Jz1-v
"""

UID = 118551449
Last_Name = 'MURALI' 
First_Name = 'SAMRIDHA' 

from Crypto.Cipher import DES
from Crypto.Cipher import AES

def des_input_av_test(inputblock, key, bitlist):
    cipher = DES.new(key, DES.MODE_ECB)
    originalcipher = cipher.encrypt(inputblock)
    results = []
    for bit_position in bitlist:
        newinput = bytearray(inputblock)
        pos1 = bit_position//8
        pos2 = 7- bit_position%8
        newinput[pos1] ^= (1 << pos2)
        newcipher = cipher.encrypt(bytes(newinput))
        num_bit_diff = sum(bin(a ^ b).count('1') for a, b in zip(originalcipher, newcipher))
        results.append(num_bit_diff)
    return results

def des_key_av_test(inputblock, key, bitlist):
    cipher = DES.new(key, DES.MODE_ECB)
    originalcipher = cipher.encrypt(inputblock)
    results = []
    for bit_position in bitlist:
        newkey = bytearray(key)
        pos1 = bit_position//8
        pos2 = 7- bit_position%8
        newkey[pos1] ^= (1 << pos2)
        cipher2 = DES.new(bytes(newkey), DES.MODE_ECB)
        newcipher = cipher2.encrypt(inputblock)
        num_bit_diff = sum(bin(a ^ b).count('1') for a, b in zip(originalcipher, newcipher))
        results.append(num_bit_diff)
    return results

def aes_input_av_test(inputblock, key, bitlist):
    cipher = AES.new(key, AES.MODE_ECB)
    originalcipher = cipher.encrypt(inputblock)
    results = []
    for bit_position in bitlist:
        new_input = bytearray(inputblock)
        pos1 = bit_position//8
        pos2 = 7- bit_position%8
        new_input[pos1] ^= (1 << pos2)
        newcipher = cipher.encrypt(bytes(new_input))
        num_bit_diff = sum(bin(a ^ b).count('1') for a, b in zip(originalcipher, newcipher))
        results.append(num_bit_diff)
    return results

def aes_key_av_test(inputblock, key, bitlist):
    cipher = AES.new(key, AES.MODE_ECB)
    originalcipher = cipher.encrypt(inputblock)
    results = []
    for bit_position in bitlist:
        newkey = bytearray(key)
        pos1 = bit_position//8
        pos2 = 7-bit_position%8
        newkey[pos1] ^= (1 << pos2)
        cipher2 = AES.new(bytes(newkey), AES.MODE_ECB)
        newcipher = cipher2.encrypt(inputblock)
        num_bit_diff = sum(bin(a ^ b).count('1') for a, b in zip(originalcipher, newcipher))
        results.append(num_bit_diff)
    return results