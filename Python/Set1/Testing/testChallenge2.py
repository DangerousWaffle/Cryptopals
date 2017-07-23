#!/usr/bin/python3
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Modules'))
import ConvertEncoding
import XOR

def test2():
	hex1 = "1c0111001f010100061a024b53535009181c"
	hex2 = "686974207468652062756c6c277320657965"
	expected = "746865206b696420646f6e277420706c6179"

	result = XOR.performXOR(ConvertEncoding.convertHexToBytes(hex1),ConvertEncoding.convertHexToBytes(hex2))
	print(result)
	if (ConvertEncoding.convertBytesToHex(result) == expected):
		return True
	else:
		return False

if __name__ == "__main__":
	if test2():
		print("Challenge 2 success!")
	else:
		print("Challenge 2 fail")

