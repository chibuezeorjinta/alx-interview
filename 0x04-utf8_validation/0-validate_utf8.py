#!/usr/bin/python3
"""check for utf-8"""

def validUTF8(data):
	"""
	1. Convert to binary
	2. Check if the number is self
		contained withing the last 8 bits
	"""
	bit_num = 0
	for bit in data:
		data_to_binary = bin(bit).replace('0b', '').rjust(8, '0')[-8:]
		if bit_num == 0:
			if data_to_binary.startswith('110'):
				bit_num = 1
			if data_to_binary.startswith('1110'):
				bit_num = 2
			if data_to_binary.startswith('11110'):
				bit_num = 3
			if data_to_binary.startswith('10'):
				return False
		else:
			if not data_to_binary.startswith('10'):
				return False
			bit_num -= 1

	if bit_num != 0:
		return False

	return True

