print("CAESAR CYPHER DECRYPT")

#Enter the encrypted letter's corresponding numerical value
encrypted_number = int(input("Input a number from ALPHABET TABLE: "))

#Enter a caesar shift value which will be used to decrypt the letter
caesar_shift = int(input("Input a caesar shift: "))
print() # here the print function is used to adjust the white spacing

#formula for decrypting using a caesar cypher
decrypted_number_left = (encrypted_number - caesar_shift - 2) % 26
decrypted_number = (encrypted_number - caesar_shift) % 26
decrypted_number_right = (encrypted_number - caesar_shift + 2) % 26


#output
print(f"The decrypted entry in ALPHABET TABLE is: {decrypted_number_left}, {decrypted_number}, {decrypted_number_right}")