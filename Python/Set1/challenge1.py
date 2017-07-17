#!/usr/bin/python3
import base64

def convertHexToBase64(hexString):
	#Convert to byte array
	byteA = bytearray.fromhex(hexString)
	print (byteA)
	return base64.b64encode(byteA).decode("utf-8")

#Testing
def testChallenge1():
	toDecode = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
	decoded = convertHexToBase64(toDecode)
	if (decoded == expected):
		return True
	else:
		return False


if __name__ == "__main__":
	if (testChallenge1()):
		print("Program 1 success");
	else:
		print("Failure");