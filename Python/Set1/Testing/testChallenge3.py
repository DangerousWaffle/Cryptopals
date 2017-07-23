#!/usr/bin/python3

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Modules'))
import ConvertEncoding
import VigenereDecoder

def test3():
	inputString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

	print(VigenereDecoder.decodeString(ConvertEncoding.convertHexToBytes(inputString)).decode("utf-8")) 

if __name__ == "__main__":
	test3()