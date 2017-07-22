#!/usr/bin/python3
from ..Modules import ConvertEncoding

toDecode = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def testChallenge1():
        decoded = challenge1.convertHexToBase64(toDecode)
        if (decoded == expected):
                return True
        else:
                return False

def testChallenge1Rev():
	encoded = challenge1.convertBase64ToHex(expected)
	if (encoded == toDecode):
		return True
	else:
		return False

if __name__ == "__main__":
        if (testChallenge1()):
                print("Challenge 1 success");
        else:
                print("Challenge 1 Failure");

        if (testChallenge1Rev()):
                print("Challenge 1 reversed success");
        else:
                print("Challenge 1 reversed Failure");
