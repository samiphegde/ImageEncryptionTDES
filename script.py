from Crypto.Cipher import DES3
from hashlib import md5

while True:
	print("Choose the operation to be executed : \n\t1- Encrypt\n\t2- Decrypt")
	operation = input("Enter your choice : ")
	if operation not in ['1','2']:
		break
	file_path = input("Enter the image's file path : ")
	key = input("Enter the TDES key : ")

	key_hash = md5(key.encode('ascii')).digest() #16-byte key

	tdes_key = DES3.adjust_key_parity(key_hash)
	cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0' )

	with open(file_path, 'rb') as input_file:
		file_bytes = input_file.read()

		if operation == '1':
			new_file_bytes = cipher.encrypt(file_bytes)
		else:
			new_file_bytes = cipher.decrypt(file_bytes)

	with open(file_path, 'wb') as output_file:
		output_file.write(new_file_bytes)
	
	print("Operation Completed!")

	cont = input("Do want to continue? (Y/N) : ")
	if cont == "N" or cont == "n":
		break

