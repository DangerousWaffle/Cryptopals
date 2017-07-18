#!/usr/bin/python3

def performXOR(byteArray1,byteArray2):
	result = bytearray()

	if len(byteArray1) >= len(byteArray2):
		for idx,byte in enumerate(byteArray1):
			result.append(byte ^ byteArray2[idx%len(byteArray2)])
	else:
		for idx,byte in enumerate(byteArray2):
			result.append(byte ^ byteArray1[idx%len(byteArray1)])

	return result
	
