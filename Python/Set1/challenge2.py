#!/usr/bin/python3

def performXOR(byteArray1,byteArray2):
	result = bytearray()
	for idx,byte in enumerate(byteArray1):
		result.extend(byte ^ byteArray2[idx])
	return result
	
