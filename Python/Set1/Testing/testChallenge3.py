#!/usr/bin/python3

import challenge1
import challenge3

def test3():
	inputString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

	print(challenge3.decodeString(challenge1.convertHexToBytes(inputString)).decode("utf-8")) 

if __name__ == "__main__":
	test3()